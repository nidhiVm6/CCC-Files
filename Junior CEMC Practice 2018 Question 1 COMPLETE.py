## Junior CEMC 2018 ##
## Question One ##

print("Welcome to the Concerned Citizens of Commerce")
print("Our program will tell you to ignore the phone if a telemarketer is calling, or answer it otherwise\n")

programDone = input("Press 'Space' if you have a number to check\nThen press 'Enter'\n")

while (programDone == " "):
    fourDigits = []

    for x in range (1, 5):

        if (x == 1):
            place = "first"

        elif (x == 2):
            place = "second"

        elif (x == 3):
            place = "third"

        elif (x == 4):
            place = "fourth"

        print("Please enter the", place, " digit: ")
        digit = int(input(""))
        print("\n")
        fourDigits.append(digit)

    if (fourDigits[0] ==  8) or (fourDigits[0] == 9):
        st = fourDigits[1]

        if (fourDigits[2] == st):

            if (fourDigits[3] == 8) or (fourDigits[3] == 9):
                print("IGNORE\n")

            else:
                print("ANSWER\n")

        else:
            print("ANSWER\n")

    else:
        print("ANSWER\n")

    programDone = input("Press 'Space' if you have another number to check\nThen press 'Enter'\n")

print("Thank you for using our program\nSee you soon")
