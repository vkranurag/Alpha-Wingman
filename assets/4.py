a=input().split(' ')
b=[]
c=0
for x in range(-1,-(len(a)+1),-1):
    b.append(a[x])
    c+=1
a=b
print(a)
