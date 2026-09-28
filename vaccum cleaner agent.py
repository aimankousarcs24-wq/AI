room_A = input("Enter status of Room A (DIRTY/CLEAN): ")
room_B = input("Enter status of Room B (DIRTY/CLEAN): ")
position = input("Enter vacuum position (A/B): ")
room_A = room_A.upper()
room_B = room_B.upper()
position = position.upper()
if position == "A":
    if room_A == "DIRTY":
        print("Room A is DIRTY")
        print("SUCK")
        room_A = "CLEAN"
        print("MOVE RIGHT")
    if room_B == "DIRTY":
        print("Room B is DIRTY")
        print("SUCK")
        room_B = "CLEAN"
elif position == "B":
    if room_B == "DIRTY":
        print("Room B is DIRTY")
        print("SUCK")
        room_B = "CLEAN"
    print("MOVE LEFT")
    if room_A == "DIRTY":
        print("Room A is DIRTY")
        print("SUCK")
        room_A = "CLEAN"
print("Final State:")
print("Room A =", room_A)
print("Room B =", room_B)
print("STOP")
