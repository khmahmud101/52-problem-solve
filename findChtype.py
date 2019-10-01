t = int(input())
for i in range(1,t+1):
    ch = input()
    if ch>= "a" and ch<= "z":
        print("Lower Case Character")
    elif ch>= "A" and ch<= "Z":
        print("Upper Case Character")
    elif ch >= "0" and ch <= "9":
        print("Numerical Character")
    else:

        print("special Character")
