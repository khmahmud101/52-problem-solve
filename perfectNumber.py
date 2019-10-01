#check perfect number in specefic interval
t = int(input())
for i in range(1,t+1):

    n1 = int(input("Enter any number: "))
    for j in range(1,n1+1):
        sum = 0
        for num in range(1,j):
            if j % num == 0:
                sum = sum + num
        if sum == j:
            print(j)





