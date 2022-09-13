inmin = int(input("Enter the number of minutes you would like to check: "))
arithmetic = 0

loopDone = False

while loopDone != True:

    if inmin < 720:
        loopDone = True

    else:
        loopDone = False
        inmin = inmin - 720

hours = str(inmin/60)
hours, discard = hours.split(".")
hours = int(hours)

minutes = inmin - (hours * 60)
time = 1159

for x in range(0, inmin + 1):

    time = str(time)
    length = len(time)

    if time[length-1] == "9":

        if time[length-2] == "5":

            if length == 4:
            
                if (time[1] != "2") or (time[0] != "1"):
                    time = int(time)
                    time = time + 41

                elif (time[1] == "2") and (time [0] == "1"):
                    time = int(time)
                    time = time - 1159

            elif length == 3:
                time = int(time)
                time = time + 41

        else:
            time = int(time)
            time = time + 1

    else:
        time = int(time)
        time = time + 1

    time = str(time)
    length = len(time)

    if length == 4:
        
        digA = int(time[0])
        digB = int(time[1])
        digC = int(time[2])
        digD = int(time[3])

        difference = digA - digB

        if digB - digC == difference:

            if digC - digD == difference:

                arithmetic = arithmetic + 1

    elif length == 3:

        digA = int(time[0])
        digB = int(time[1])
        digC = int(time[2])

        difference = digA - digB

        if digB - digC == difference:

            arithmetic = arithmetic + 1

print("The number of minutes from 12:00 to", inmin, "minutes later that form an arithmetic sequence is", arithmetic)
