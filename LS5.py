'''#Q1
n=int(input("Enter a integer:"))
i=1
while (i<=n):
    print(i)
    i+=1
#Q2
n=int(input("Enter a integer:"))
for i in range (1,n+1):
    print(i)
#Q3
n=int(input("Enter a integer:"))
while (n>0):
    print(n)
    n-=1
#Q4
n=int(input("Enter a integer:"))
for i in range (n,0,-1):
    print(i)
#Q5
n=int(input("Enter a integer:"))
for i in range (2,n+1,2):
    print(i)
#Q6
n=int(input("Enter a integer:"))
for i in range (1,n+1):
    if(i%2==0):
        continue
    else:
        print(i,'\t')
#Q7
n=int(input("Enter a integer:"))
s=0
for i in range (2,n+1,2):
    s+=i
print("Sum=",s)
#Q8
n=int(input("Enter a integer:"))
s=0
for i in range (1,n+1,2):
    s+=i
print("Sum=",s)
#Q9
n=int(input("Enter a integer:"))
s,p,i=0,1,1
while (n!=0):
    a=n%10
    n=n//10
    if(i==1):
        p=p*a
        i=0
    else:
        s+=a
        i=1
print("Sum of even nos=",s)
print("Product of odd nos=",p)
#Q10
n=int(input("Enter a integer:"))
p=1
while (n>0):
    p=p*n
    n-=1
print("Factorial=",p)'''
#Q11
n=int(input("Enter the no:"))
f=0
s=1                                         
if (n<=0):
    print("The requested series is",f)
else:
    print(f,s,end=" ")
    for x in range(2,n):
        a=f+s                           
        print(a,end=" ")
        f=s
        s=a
'''#Q12
n=int(input("Enter a integer:"))
s,i=0,1
while (n!=0):
    a=n%10
    n=n//10
    s+=a
print("Sum of digits=",s)
#Q13
n=int(input("Enter a integer:"))
i=1
print("Factors are=")
while (i<n):
    if(n%i==0):
        print(i,'\t')
    i+=1
#Q14
n=int(input("Enter a integer:"))
p=int(input("Enter the power:"))
i=1
a=n
while(i<p):
    n=n*a
    i+=1
print("Result=",n)
#Q15
n=int(input("Enter a integer:"))
a=n
s=0
while(a!=0):
    s=(s*10)+a%10
    a=a//10
if(n==s):
    print("Palindrome")
else:
    print("Not Palindrome")
#Q16
n=int(input("Enter no of originals:"))
p=int(input("Enter no of copies:"))
o,c=1,0
while(o<n):
    o+=1
    c+=1
if(c==p):
    print("Yes")
elif(c<p):
    while(c<p):
        c+=2
    if(c==p):
        print("Yes")
    else:
        print("No")
else:
    print("No")'''
    
    
    


    
    


    
    
