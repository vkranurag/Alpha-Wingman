#Q1(a)
n=int(input("Enter a no:"))
for i in range(n):
    for j in range(i+1):
        print('*',end='')
    print('\n')
#Q1(b)
n=int(input("Enter a no:"))
for i in range(n):
    for j in range(0,n-i):
            print(" ",end='')
    for j in range(i+1):
        print('*',end='')
    print('\n')
#Q1(c)
n=int(input("Enter a no:"))
a=1
for i in range(n):
        for j in range(n-1-i):
            print(" ",end='')
        for j in range(a):
            print('*',end='')
        a+=2
        print('\n')
#Q1(d)
n=int(input("Enter a no:"))
print("Enter a no:3")
a=n
for i in range(n+1):
    if(i%2!=0):
        for j in range((i+1)//2,0,-1):
            print(" ",end='')
        for k in range(a):
            print('*',end='')
        a-=2
        print('\n')

#Q1(e)
n=int(input("Enter a no:"))
for i in range(1,n+1):
    for j in range(5):
        print(i,end='')
    print('\n')
#Q1(f)
n=int(input("Enter a no:"))
for i in range(1,n+1):
    for j in range(i,i+5):
        print(j,end='')
    print('\n')
#Q1(g)
n=int(input("Enter a no:"))
for i in range(1,n+1):
    for j in range(i):
        print(i,end='')
    print('\n')
#Q1(h)
n=int(input("Enter a no:"))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end='')
    print('\n')

#Q1(i)
n=int(input("Enter a no:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end='')
    if(i==j):
        for j in range(0,(n-i)):
            print("  ",end='')
    for j in range(i,0,-1):
        print(j,end='')
    print('\n')
#Q1(j)
n=int(input("Enter a no:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end='')
    print('\n')
    if(j==n):
        while(n!=0):
            for j in range(1,n):
                print(j,end='')
            print('\n')
            n-=1
#Q1(k)
n=int(input("Enter a no:"))
for i in range(1,n+n):
    if(i%2!=0):
        for j in range(1,i+1):
            print(j,end='')
        print('\n')
        if(j==n+n-1):
            while(n!=0):
                #if(n%2!=0):
                    for j in range(1,n+n-2):
                        print(j,end='')
                    print('\n')
                    n-=1
#Q1(l)
n=int(input("Enter a no:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end='')
    if(i==j):
        for j in range(i-1,0,-1):
            print(j,end='')
        print('\n')
n-=1
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end='')
    if(i==j):
        for j in range(i-1,0,-1):
            print(j,end='')
        print('\n')

#Q1(m)
n=int(input("Enter a no:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end='')
    print('\n')
    if(j==n):
        while(n!=0):
            for j in range(1,n):
                print('*',end='')
            print('\n')
            n-=1
#Q1(n)
n=int(input("Enter a no:"))
for i in range(n):
    for j in range(0,n-i):
            print(" ",end='')
    for j in range(i+1):
        print('*',end='')
    print('\n')
n-=1
for i in range(n):
    for j in range(i+2):
            print(" ",end='')
    for j in range(n-i,0,-1):
        print('*',end='')
    print('\n')

#Q1(o)
n=int(input("Enter a no:"))
for i in range(n+1):
    if(i%2!=0):
        for j in range(0,(n-i)//2):
            print(" ",end='')
        for j in range(i):
            print('*',end='')
        print('\n')
n-=2
for i in range(n+1):
    if(i%2!=0):
        for j in range((i+1)//2,0,-1):
            print(" ",end='')
        for j in range(n-i+1):
            print('*',end='')
        print('\n')
#Q1(p)
n=int(input("Enter a no:"))
print("*\n")
for i in range(1,n+1):
    print('*',end='')
    for j in range(1,i+1):
        print(j,end='')
    if(i==j):
        for j in range(i-1,0,-1):
            print(j,end='')
        print('*','\n')
n-=1
for i in range(n,0,-1):
    print('*',end='')
    for j in range(1,i+1):
        print(j,end='')
    if(i==j):
        for j in range(i-1,0,-1):
            print(j,end='')
        print('*','\n')
print("*")
#Q2
n=int(input("Enter a no:"))
for i in range(1,n+1):
    print("Multiplication Table of ",i," is:")
    for j in range(1,11):
        print(j,"X",i,"=",j*i,"\n")
    print("\n")
#Q3(a)
n=int(input("Enter a no:"))
s,p=0,0
for i in range(1,n+1):
    for j in range(1,i+1):
        p+=j
    s+=p
    p=0
print(s)
#Q3(b)
n=int(input("Enter a no:"))
s,p=0,1
for i in range(1,n+1):
    for j in range(1,i+1):
        p=p*j
    s+=1/p
print(s)
            
             


      
                


        


    
        
