n=int(input("enter the number"))
m=int(input("enter the number"))
for i in range(0,n+1,1):
    for j in range(0,m-i):
        print(end=" ")
    for j in range(0,i):
            print("* ",end="")
    print( )
