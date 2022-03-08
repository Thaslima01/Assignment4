x=[]
s=int(input("enter the size"))
sum=0
for i in range(s):
    x.insert(i,int(input("enter the number")))
max(x)
min(x)
sum=min(x)+max(x)
print(f"{min(x)}+{max(x)}={sum}")

