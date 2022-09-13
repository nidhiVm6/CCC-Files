## Junior CEMC Practice 2017 ##
## Question 1 ##

xCo = int(input("Enter the x coordinate of your point: "))
yCo = int(input("Enter the y coordinate of your point: "))

if (xCo < 0):
    if (yCo < 0):
        quadrant = 3
    elif (yCo > 0):
        quadrant = 2
elif (xCo > 0):
    if (yCo < 0):
        quadrant = 4
    elif (yCo > 0):
        quadrant = 1

print("The point belongs in quadrant ", quadrant)
        
        
