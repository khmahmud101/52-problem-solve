# Python program to display all the prime numbers within an interval


t = int(input())
for i in range(1,t+1):
    n1 = int(input())
    n2 = int(input())

    for num in range(n1,n2+1):
        if num >1:
            for j in range(2,num):
                if num % j == 0:
                    break
            else:
                print(num)
        else:
            print("Not prime")


