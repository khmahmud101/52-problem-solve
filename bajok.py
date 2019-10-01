
t = int(input("Enter number:"))
for i in range(1,t+1):

    n = int(input())
    print("case {}:".format(i),end="")
    for j in range(1,n+1):

        if n%j==0:

            print(" ",j, end="")
    print("\n")




















