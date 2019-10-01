num = int(input())
for i in range(1,num+1):
    food_wg = float(input())
    count=0
    while food_wg > 1.0:
        food_wg /= 2
        count +=1
    print(count,"days")

