t = int(input())
for j in range(t):
    s = input()

    for i in s:
        if (
                i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
            print(i,end="")
    print("\n")
    for i in s:
        if (
                i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u' and i != 'A' and i != 'E' and i != 'I' and
                i !=
                'O' and i != 'U'):
                print(i,end="")









