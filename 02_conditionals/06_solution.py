# Transport Mode Selection
distance = int(input("Enter distance: "))

if distance < 0:
    print("Invalid Distance")
    exit()

if distance < 3:
    transport = 'Walk'
elif distance <= 15:
    transport = 'Bike'
else:
    transport = 'Car'

print('AI recommends you the transport of:', transport)