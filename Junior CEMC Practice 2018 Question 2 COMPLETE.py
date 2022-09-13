## Junior CEMC 2018 ##
## Question Two ##

print("Welcome to our Parking Occupancy Program\n")
lineOne = int(input("Enter the value of N: "))
lineTwo = input("Enter the line of yesterday's parking occupancy:\n")
lineThree = input("Enter the line of today's parking occupancy:\n")

print("\n")

match = 0

for x in range(0, lineOne):
    if (lineTwo[x] == "C") or (lineTwo[x] == "c"):
        if (lineThree[x] == "C") or (lineThree[x] == "c"):
            match = match + 1

print("There are ", match, " occupancy matches\n\nThank you for using our program")
