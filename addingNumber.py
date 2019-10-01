t = int(input())
for i in range(1,t+1):

    n = int(input("Enter any number: "))
    sum = 0
    for j in range(1,n):
        if n % j == 0:
            sum = sum + j
    if sum == n:
        print("yes", n, "is perfect number")
    else:
        print(n,"is Not perfect")





