import math
t = int(input())
for i in range(t):
    n = int(input())
    sqr = math.sqrt(n)
    if sqr*sqr == n:
        print("yes")
    else:
        print("no")


