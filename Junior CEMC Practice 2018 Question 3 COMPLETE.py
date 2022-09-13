## Junior CEMC 2018 ##
## Question Three ##

print("Welcome to my distance program\n")
consecDist = input("Enter the four consectutive distances separated by spaces:\n")
a, b, c, d = consecDist.split(" ")

a = int(a)
b = int(b)
c = int(c)
d = int(d)

## Line 1 ##
print("0 ", a, " ", a + b, " ", a + b + c, " ", a + b + c + d)

## Line 2 ##
print(a, " 0 ", b, " ", b + c, " ", b + c + d)

## Line 3 ##
print(a + b, " ", b, " 0 ", c, " ", c + d)

## Line 4 ##
print(a + b + c, " ", b + c, " ", c, " 0 ", d)

## Line 5 ##
print(a + b + c + d, " ", b + c + d, " ", c + d, " ", d, " 0")
