def sort(y):
    return y[1]
n=int(input())
a=[]
for i in range(n):
    name=input()
    mark=float(input())
    a.append([name,mark])
a.sort(key=sort)
b=a[0][1]
for x in range(0,len(a)-1):
    if a[x][1]>b:
        b=a[x][1]
        break
c=[]
for x in range(1,len(a)-1):
    if a[x][1]==b:
        c.append(a[x][0])
c.sort()
for x in c:
    print(x)
