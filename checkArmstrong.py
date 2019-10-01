num = int(input())
temp = num
sum = 0
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10


if num == sum:
    print("Armstrong number")

else:
    print("Not Armstrong number")
