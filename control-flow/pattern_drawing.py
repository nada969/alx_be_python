num = int(input("Enter the size of the pattern:"))
x=num
while x:
    for i in range(1,num):
        print("*", end="")
    print(" \t")
    x -=1