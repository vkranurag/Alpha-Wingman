n=int(input())
a=[]
for i in range(0,n):
    b=input().split()
    if b[0]=="insert":
        a.insert(int(b[2]),int(b[1]))
    elif(b[0]=="print"):
        print(a)
    elif (b[0]=="remove"):
        a.remove(int(b[1]))
    elif(b[0]=="append"):
        a.append(int(b[1]))
    elif(b[0]=="sort"):
        a.sort()
    elif(b[0]=="pop"):
        a.pop()
    elif(b[0]=="reverse"):
        a.reverse()
    
