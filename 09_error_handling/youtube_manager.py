
import json

fileName = 'youtube.json'

def load_data():
    try:
        with open(fileName, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open(fileName, 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    if (not videos):
        print("No Data available")
        return
    print("\n")
    print("*" * 70,)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video["name"]}, Duration: {video["time"]}")
        print("*" * 70)

def add_video(videos):
    name = input("Enter video name: ").strip()
    time = input("Enter video time: ").strip()
    if (not name or not time):
        print("One or more field is/are missing")
        return add_video(videos)
    videos.append({"name": name, "time": time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    video_number_to_update = int(input("Enter the video number to update: "))
    if video_number_to_update < 1 or video_number_to_update > len(videos):
        print("Invalid video number!")
        return update_video(videos)
    while(True):
        new_name = input("Enter the new video name: ")
        new_time = input("Enter the new video time: ")
        if not new_name or not new_time:
            print("One or more fields is missing!")
        else:
            break
    videos[video_number_to_update - 1] = {"name": new_name, "time": new_time}
    save_data_helper(videos)
    print("Updated Successfully")

    

def delete_video(videos):
    list_all_videos(videos)
    video_number_to_delete = int(input("Enter the video number to delete: "))
    if video_number_to_delete < 1 or video_number_to_delete > len(videos):
        print("Invalid video number!")
        return delete_video(videos)
    del videos[video_number_to_delete - 1]
    save_data_helper(videos)
    print("Deleted Successfully")



def main():
    videos = load_data()

    while True:
        print("\n Youtube Manager | Choose an option:")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")

        choice = input("Enter your choice: ")
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                print("Exiting app")
                break
            case _:
                print("Invalid Choice!")

if __name__ == "__main__":
    main()
# __ is called as dunder