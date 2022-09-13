rows = int(input(""))
columns = int(input(""))
strokes = int(input(""))
myList = []
subList = []

for x in range(rows):
    for y in range(columns):
        subList.append("B")
    myList.append(subList)
    subList = []

for z in range(0, strokes-1):
    newStroke = input("")
    direction, rcNum = newStroke.split(" ")
    rcNum = int(rcNum)

    if direction == "R":
        for i in range(columns):
            if myList[rcNum-1][i-1] == "B":
                myList[rcNum-1][i-1] = "G"
            else:
                myList[rcNum-1][i-1] = "B"

    if direction == "C":
        for j in range(rows):
            if myList[j-1][rcNum-1] == "B":
                myList[j-1][rcNum-1] = "G"
            else:
                myList[j-1][rcNum-1] = "B"

for x in range