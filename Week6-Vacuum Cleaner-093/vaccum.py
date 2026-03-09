def vacuum_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Right"
    elif location == "B":
        return "Left"

roomA = input("Enter status of Room A (Clean/Dirty): ")
roomB = input("Enter status of Room B (Clean/Dirty): ")

rooms = {"A": roomA, "B": roomB}

location = input("Enter starting location of agent (A/B): ")
print("\nInitial State:", rooms)

for i in range(5):
    status = rooms[location]
    action = vacuum_agent(location, status)

    print("\nAgent Location:", location)
    print("Room Status:", status)
    print("Action:", action)

    if action == "Suck":
        rooms[location] = "Clean"

    elif action == "Right":
        location = "B"

    elif action == "Left":
        location = "A"

print("\nFinal State:", rooms)
