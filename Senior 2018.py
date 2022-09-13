games = int(input(""))

stringA = input("")
stringB = input("")

sumA = 0
sumB = 0

matchFound = False

for x in range (games-1):
    firstA, stringA = stringA.split(" ",1)
    firstA = int(firstA)
    sumA = sumA + firstA
    firstB, stringB = stringB.split(" ",1)
    firstB = int(firstB)
    sumB = sumB + firstB
    if sumA == sumB:
        print(x+1)
        matchFound = True
        break

if matchFound is False:
    print("0")