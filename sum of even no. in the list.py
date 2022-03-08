x=[]
s=int(input("enter the size"))
sum=0
for i in range(s):
    x.insert(i,int(input("enter the number")))
    if (x[i]%2==0):
        sum=sum+x[i]
print(sum)
