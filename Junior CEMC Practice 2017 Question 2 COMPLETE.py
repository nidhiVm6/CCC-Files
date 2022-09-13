## Junior CEMC Practice 2017 ##
## Question 2 ##

N = int(input("Enter the value of N: "))
k = int(input("Enter the value of k: "))

val = N

for x in range (0, k):
    N = N * 10
    val = val + N

print("The shifty sum is ", val)
