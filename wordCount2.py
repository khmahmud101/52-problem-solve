t = int(input())
for i in range(t):
    s = input()
    count = 0
    for j in s:
        if j == " ":
            count= count+1
print(count+1)
