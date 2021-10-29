#Q1
a=(2+(3//2))
print(a)
a=(2+(3/2))
print(a)
#Q2
#(a)
a=1+2+3/2
print(a)
#(b)
a=3/(2+1+2)
print(a)
#(c)
expr=10+20*30
print(expr)
#(d)
a=2<3
print(a)
#(e)
a=2>3
print(a)
#(f)
a=2<3 or 2>3
print(a)
#(g)
a=2<3 and 2>3
print(a)
#(h)
a=2<1 or 2>3 or 4<5 or 5>2
print(a)
#(i)
a=5>1 or 2>3 or 4>5 or 5<2
print(a)
#(j)
a=2<1 and 2<3 or 4<5 or 5>2
print(a)
#(k)
a=5>1 or 2>3 or 4>5 and 5<2
print(a)
#(l)
name="Rafa"
age=0
a=name=="Rafa" or name=="Roger" and age>=2
print(a)
#(m)
name="Rafa"
age=0
a=(name=="Rafa" or name=="Roger") and age>=2
print(a)
#(n)
print(100/10*10)
#(o)
print(2**3**2)
#(p)
expression=100+200/10-3*10
print(expression)
#(q)
a=12
b=26
c=4
print(b>a>c)
#(r)
a=12
b=6
c=4
print(b<a>c)
#Q3
a=10
b=a==0 and "Hello"
print(b)
#Q4
a=10
b=a==0 or "Hello"
print(b)
#Q5
a=10
b=a==0 or 8
print(b)
#Q6
a=10
b=not(a) and a
print(b)
#Q7
a=10
b=not(a) or a
print(b)
#Q8
a=10
print(not a%5==0)
#Q9
a=10
print((not a)%5==0)
#Q10
a=1<=3<=2
print(a)
#Q11
a=1<=3!=2
print(a)
#Q12
a=1<=3!=3
print(a)
#Q13
a=2*3**2**2/10
print(a)
#Q14
a=2*3**2**2/10 or 2>3 and 2<3
print(a)
#Q15
b=2*3**2**2/10 or 2>3
a=b and 2<3
print(a)
#Q16
x1=int(input("Enter the 1st x coordinate:"))
x2=int(input("Enter the 2nd x coordinate:"))
y1=int(input("Enter the 1st y coordinate:"))
y2=int(input("Enter the 2nd y coordinate:"))
d=(((x2-x1)**2)+((y2-y1)**2))**(1/2)
print("Dist=",d)
#Q17
p=int(input("Enter the principle amt:"))
r=int(input("Enter the rate:"))
t=int(input("Enter the no of years:"))
s=(p*r*t)/100
print("SI=",s)
#Q18
c=int(input("Enter the temp in celcius:"))
f=(c*(9/5))+32
print("Temp in Farenheit=",f)
#Q19
n=int(input("Enter the no:"))
s=n%10
s=s*100
n=n//10
s+=(n%10)*10
n=n//10
s+=n
print(s)
#Q20
s=int(input("Enter the no of seconds:"))
h=s//3600
s=s%3600
m=s//60
s=s%60
print("Hours=",h,"\nMins=",m,"\nSecs=",s)

