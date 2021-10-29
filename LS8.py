#Q1
'''A funtion can be defined as a block of code that runs only when its called.It is reusable.'''
#Q2
'''The keyword def introduces a function definition. It must be followed by function name and paranthesised list of formal parameters.
Eg:
def Sum(a,b):
   s=a+b
   return s'''
#Q3
'''Once the basic structure of a function is finalized, you can execute it by calling it from another function or directly from Python.
Eg:
x=Sum(1,2)
print(x)
Output:
3'''
#Q4
def fac(n):
    p=1
    while (n>0):
        p=p*n
        n-=1
    print("Factorial=",p)  
n=int(input("Enter a integer:"))
fac(n)
#Q5
def fib(n):
    f=0
    s=1                                         
    if (n<=0):
        print("The requested series is",f)
    else:
        print("The requested series is",f,s,end=" ")
        for x in range(2,n):
            a=f+s
            print(a,end=" ")
            f=s
            s=a
n=int(input("Enter the no:"))
fib(n)
#Q6
def pal(n):
    a=n
    s=0
    while(a!=0):
        s=(s*10)+a%10
        a=a//10
    if(s==n):
        return 1
    else:
        return 0
n=int(input("\nEnter the no:"))
s=pal(n)
if(s==1):
    print("Palindrome")
else:
    print("Not Palindrome")
#Q7
def big(a,b,c):
    if(a>=b) and (a>=c):
        p=a
    elif(b>=a) and (b>=c):
        p=b
    else:
        p=c
    print("Largest no:",p)
a=int(input("Enter the 1st no:"))
b=int(input("Enter the 2nd no:"))
c=int(input("Enter the 3rd no:"))
big(a,b,c)
#Q8
def cvt(a):
    b=ord(a)-32
    print(chr(b))
a=input("Enter a lowercase letter:")
cvt(a)
#Q9
def fac(n):
    i,s=1,0
    while (i<n):
        if(n%i==0):
            s+=i
        i+=1
    return s
n=int(input("Enter a integer:"))
s=fac(n)
if(s==n):
    print("Yes")
else:
    print("No")
#Q10
def tri(n):
    j=1
    for k in range (1,n+1):
        for i in range (0,k):
            print(j,end=" ")
            j+=1
        print('\n')        
n=int(input("Enter a integer:"))
tri(n)
#Q11
'''Any input parameters placed within the parentheses of a function are called its arguments.
Eg:
def Sum(a,b)
Here, the inputed values of a and b are the arguments of the function Sum'''
#Q12
'''The statement return exits a function, optionally passing back an expression to the caller.
Eg:
def Sum(a,b):
   s=a+b
   return s
p=Sum(a,b)
Here, the value in variable s after computaion gets passed to p, the caller variable'''
#Q13
'''
Step 1:Here, the number whose factorial is to be found is stored in n.
Step 2:A variable p is initialized with value 1.
Step 3:We check if n is negative, zero or positive using while statement.
Step 4:If the number is positive, we use the loop to mutiply the value in p successively to calculate the factorial.
Step 5:p is displayed as the output.'''
#Q14
def fac(n):
    p=1
    while (n>0):
        p=p*n
        n-=1
    return p   
n=int(input("Enter a integer:"))
p=fac(n)
print("Factorial=",p)
#Q15
def big(a,b,c):
    if(a>=b) and (a>=c):
        p=a
    elif(b>=a) and (b>=c):
        p=b
    else:
        p=c
    return p
a=int(input("Enter the 1st no:"))
b=int(input("Enter the 2nd no:"))
c=int(input("Enter the 3rd no:"))
s=big(a,b,c)
print("Largest no:",s)
