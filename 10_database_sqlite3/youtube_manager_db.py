import sqlite3

conn = sqlite3.connect("youtube_videos.db")

cursor = conn.cursor() # This cursor can direclty interact with database

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL   
    )
''')


def list_videos():
    cursor.execute("SELECT * FROM videos ORDER BY id")
    result = cursor.fetchall()
    if not result:
        print("No Data available!")
        return
    for row in result:
        print("Video ID:", row[0], "| Video Title:", row[1], "| Video Time:", row[2])
    
def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES(?, ?)", (name, time))
    conn.commit()

def update_video(name, time, video_id):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()

def take_user_input():
    while True:
        name = input("Enter the video name: ").strip()
        time = input("Enter the video time: ").strip()
        if name and time:
            return (name, time)
        print("One or more fields are missing.")

def take_videoid_input():
    while True:
        video_id = input("Enter the video ID: ").strip()
        if not video_id:
            print("Enter a valid id")
        try :
            video_id = int(video_id)
        except ValueError:
            print("Enter a numberic ID.")
            continue
        
        # Checking if the user_id is valid
        cursor.execute("SELECT * FROM videos WHERE id = ?", (video_id,))
        if not cursor.fetchone():
            print("Enter a valid id")
            continue
        return video_id

def number_of_entries():
    cursor.execute("SELECT COUNT(*) FROM videos")
    return cursor.fetchone()[0]

def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Exit App")
        choice = input("Enter your choice: ")
        print()
        match choice:
            case "1":
                list_videos()
            case "2":
                name, time = take_user_input()
                add_video(name, time)
            case "3":
                list_videos()
                if number_of_entries() == 0:
                    continue
                video_id = take_videoid_input()
                name, time = take_user_input()
                update_video(name, time, video_id)
            case "4": 
                list_videos()
                if number_of_entries() == 0:
                    continue
                video_id = take_videoid_input()
                delete_video(video_id)
            case "5":
                print("Exiting App")
                break
            case _:
                print("Invalid Option!")

    # Closing the connection
    conn.close()


if __name__ == "__main__":
    main()