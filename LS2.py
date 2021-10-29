'''#Q1
x=int(input("Enter a no:"))
print(x*x)
#Q2
print("%d+%d=%d"%(2,3,2+3))
print("The square of the no %d is %d"%(2,2**2))
#Q3
w,x,y,z=10,15,20,25
print(w,x,y,z)
print(w,x,y,z,sep=',')
print(w,x,y,z,sep='')
print(w,x,y,z,sep=':')
print(w,x,y,z,sep='-----')
#Q4
x='''
'''1-----2
|     |
|     |
|     | 
3-----4
A parallelogram has 4 corners
'''
'''print(x)
#Q5
r=2
rp=50
s=3
sp=40
print("Total price=",(r*rp)+(s*sp))
#Q6
r=5
h=10
print("Vol=",3.14*r*r*h)
print("Area=",(2*3.14*r)*(r+h))
#Q7
a=5
h=6
b=8
print("Area=",(a+b)*(h/2))
#Q8
#(a)
n=233
s=n%10
n=n//10
s+=n%10
n=n//10
s+=n%10
#(b)
n=4589
s=n%10
n=n//10
s+=n%10
n=n//10
s+=n%10
n=n//10
s+=n%10
print(s)
#(c)
n=4589
s=n%10
n=n//10
s+=n%10
n=n//10
s+=n%10
n=n//10
s+=n%10
n=n//10
s+=n%10
print(s)
#Q9
#(1)
print(3/2)
#(2)
print(3//2)
#(3)
print(2<3)
#(4)
print(2<3<4)
#(5)
print(4<5<2)
#(6)
x=2
y=3
z=4
print(x=y=z)
#(7)
x=2
y=3
z=4
print(x=y+z)'''
'''#(8)
x=-3
print(+x)
#(9)
x=-3
print(-x)
#(10)
x=1
print(not x)
#(11)
print(1%4+2%4+3%4+4%4)
#(l2)
#(a)
x=2
y=2
print(x and y)
#(b)
x=2
y=0
print(x and y)
#(c)
x=True
y=True
print(x and y)
#(d)
x=False
y=True
print(x and y)
#(e)
x=False
y=False
print(x and y)
#(13)
print(2**4*3)
#(14)
print(2+(3-2))
#(15)
print(12/3/2)
#(16)
print("python">"java")
#(17)
print('5'+'10')
#Q10
#Python program to print the list of all Keywords
#importing the module
import keyword
print("Python keywords are:")
print(keyword.kwlist)
#Q11
#Python program to print the built
#in functions
import builtins
print(dir(builtins))
#Q12
n=int(input("Enter the no:"))
p=int(input("Enter the power:"))
print(n**p)
#Q13
a=int(input("Enter the no:"))
b=int(input("Enter the numeric character:"))
print(a+b)
#Q14
a=int(input("Enter the 1st no:"))
b=int(input("Enter the 2nd no:"))
s=+(a-b)
print(s/(a+b))
#Q15
r=int(input("Enter Indian rupees amt:"))
c=input("Enter the conversion rate of Euro:")
s=c*r
print("Amt in Euro=",s)'''
#Q16
a=int(input("Enter the 1st mark:"))
b=int(input("Enter the 2nd mark:"))
c=int(input("Enter the 3rd mark:"))
d=int(input("Enter the 4th mark:"))
e=int(input("Enter the 5th mark:"))
s=a+b+c+d+e
print("Avg=",s/5)
#Q17
n=int(input("Enter the no:"))
print(((n+1)*(n))/2)


