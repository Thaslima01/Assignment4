n=int(input("enter the number"))
m=int(input("enter the number"))
for i in range(n):
    for j in range(m):
        if (i>=j):
            print("* ",end="")
    print(end="\n")
