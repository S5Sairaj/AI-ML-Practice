

vehicle_type = input("Enter vehicle type (car/truck/bike): ").strip().lower()
speed = int(input("Enter vehicle speed (mph): "))

speed_limit = 60
fine = 0

over_speed = speed - speed_limit

if over_speed > 0:
    if 1 <= over_speed <= 10:
        fine = 50
    elif 11 <= over_speed <= 20:
        fine = 100
    elif over_speed > 20:
        fine = 200

    if vehicle_type == "truck":
        fine *= 2
    elif vehicle_type == "bike":
        fine /= 2
    print(f"Fine: {fine} rupees")
else:
    print("No fine. Drive safe!")
