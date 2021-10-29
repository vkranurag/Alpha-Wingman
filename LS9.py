#Q1
def pal(s,a,b):
    if (a==b):
        return 1
    if (s[a]!= s[b]):
        return 0
    if (b<a+1):
        return pal(s,a-1,b+1)
    return 1
s=input("Enter the string:")
if pal(s,len(s)-1,0) or len(s)==0:
    print("Palindrome")
else:
    print("Not Palindrome")
#Q2
def strlen(s): 
    if s=='': 
        return 0
    else: 
        return 1 + strlen(s[1:])
s=input("Enter string")
print(strlen(s))
#Q3
def even(a,n,k):
   if (n==0):
      return 0
   else:
      if ((a[k])%2==0):
         print(a[k])
      even(a,n-1,k+1)

n=list(map(int,input().split()))
k=0
even(n,len(n),k)
#Q4
def pal(a,n,s):
    if a[n]!=a[s]:
        return 0
    if(n==s):
        return 1
    if s<n+1:
        return pal(a,n-1,s+1)
    return 1
  
a=input('Enter the characters as a Sentence:')
for i in range(0,len(a)+1):
    for j in range(0,len(a)+1):
        p=a[i:j]
        if len(p)>1:
            if pal(p,len(p)-1,0):
                print(p)

#Q5
def permutation(a,b,c,d):
    if d==0:
        if b not in s:
            s.append(b) 
        return 0
    for i in range(c): 
        y=b+a[i] 
        permutation(a,y,c,d-1)
s=[]
x=''
a=list(input('Enter the character string:'))
d=int(input('Enter the length:'))
permutation(a,x,len(a),d)
for y in s:
    temp=y
    temp=list(temp)
    temp=set(temp)
    if len(y)==len(temp):
        print(y)
#Q6
def choose(a,b,n,k):
   if (k==0):
      print(b)
      return
   else:
      for i in range(n):
         p=b+a[i]
         choose(a,p,n,k-1)
print("Enter the string")
a=list(map(str,input().split()))
k=int(input("Enter the no of characters"))
n=len(a)
b=""
choose(a,b,n,k)
#Q7
def atoi(n, num): 
    if len(n) == 1: 
        return int(n)+(num*10) 
    num = int(n[0:1])+(num*10) 
    return atoi(n[1:],num)
    
n=input("Enter n")
print(atoi(n,0))

#Q8
def fact(n):
    ans=1
    for i in range(0,n):
        ans*=(i+1)
    return ans
def combination(n,i):
    ans=fact(n)
    ans/=fact(i)
    ans/=fact(n-i)
    return ans
def count(n):
    ans=0
    for i in range(0,n+1):
        ans+=combination(n,i)**2
    return int(ans)

n=int(input('Enter n:'))
print(count(n))
#Q9
def toh(n,f,t,a):
    if (n==1):
        print("Move disk 1 from rod",f,"to rod",t)
        return
    toh(n-1,f,a,t)
    print("Move disk",n,"from rod",f,"to rod",t)
    toh(n-1,a,t,f)
         
n=int(input())
toh(n,'A','C','B') 
