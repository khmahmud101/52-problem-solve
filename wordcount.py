t = int(input())
for j in range(t):
    first_line = input()
    second_line = input()
    count = 0
    for i in first_line:
        if second_line[0] == i:
            count +=1
    if count != 0:
        print("Occurence of",second_line,"in",first_line,"=",count)
    else:
        print( second_line, "is not present")