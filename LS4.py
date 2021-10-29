#Q1
x=int(input("Enter a number"))
if(x%2==0):
    print("Even")
else:
    print("Odd")
#Q2
x=int(input("Enter a 3 digit number"))
if(x%2==0):
    s=x%10
    x=x//10
    s+=x%10
    x=x//10
    s+=x
    print("Sum=",s)
else:
    p=x%10
    x=x//10
    p=p*(x%10)
    x=x//10
    p=x*p
    print("Product=",p)
#Q3
x=int(input("Enter 1st number:"))
y=int(input("Enter 2nd number:"))
z=x
x=y
y=z
print("Swapped nos are:",x,"and",y)
#Q4
x=int(input("Enter 1st number:"))
y=int(input("Enter 2nd number:"))
print("1.Sum")
print("2.Difference")
print("3.Product")
print("4.Quotient")
print("5.Larger of the 2 nos")
a=int(input("Enter the no corresponding to your option:"))
r=0
if a==1:
      r=x+y
      print("Sum=",r)
elif a==2:
      if x>y:
          r=x-y
          print("Difference=",r)
      else:
          r=y-x
          print("Difference=",r)
elif a==3:
    r=x*y
    print("Product=",r)
elif a==4:
    r=x/y
    print("Quotient=",r)
elif a==5:
    if x>y:
         print("Larger number=",x)
    else:
       print("Larger number=",y)
else:
    print("Error in entry")
#Q5
x=input("Enter A,B or C:")
if(x=='A'):
    print("Apple")
elif(x=='B'):
    print("Banana")
elif(x=='C'):
    print("Coconut")
else:
    print("Error in entry")
#Q6
x=int(input("Enter College Credits:"))
if(x>90):
    print("Senior Status")
elif(x<=90)&(x>60):
    print("Junior Status")
elif(x<=60)&(x>30):
    print("Sophomore Status")
elif(x<=30)&(x>0):
    print("Freshman Status")
else:
    print("Error in entry")
#Q7
import random
x=(random.randint(1,50))
print(x)
if(x>10):
    print("Generated no is greater than 10")
else:
    print("Generated no is not greater than 10")
#Q8
x=input("Enter an alphabet:")
if(x=='A')|(x=='a')|(x=='E')|(x=='e')|(x=='I')|(x=='i')|(x=='O')|(x=='o')|(x=='U')|(x=='u'):
    print("Vowel")
else:
    print("Consonant")
#Q9
#(a)
a=int(input("Enter a number:"))
print(a<2)
b=a<2
if (a<2):
    print("Hello")
else:
    print("Bye")
#(b)
a=int(input("Enter a number:"))
print(a<2)
b=a<2
if (b):
    print("Hello")
else:
    print("Bye")
#(c)
a=int(input("Enter a number:"))
print(a<2)
b=a<2
if (True):
    print("Hello")
else:
    print("Bye")
#(d)
a=int(input("Enter a number:"))
print(a<2)
b=a<2
if (False):
    print("Hello")
else:
    print("Bye")
#Q10
a=int(input("Enter the weight of the 1st person:"))
b=int(input("Enter the weight of the 2nd person:"))
c=int(input("Enter the weight of the 3rd person:"))
d=int(input("Enter the weight of the 4th person:"))
w,x,y,z=0,0,0,0
if(a!=b)|(a!=d)|(a!=c):
    if(a==b):
        print("Car available for 1st and 2nd person")
        w=1
        x=1
    elif(a==c):
        print("Car available for 1st and 3rd person")
        w=1
        y=1
    elif(a==d):
        print("Car available for 1st and 4th person")
        w=1
        z=1
    if(w==0):
        print("No cars available for 1st person")
    if(b!=c)|(b!=d):
        if(b==c):
            print("Car available for 3rd and 2nd person")
            x=1
            y=1
        elif(b==d):
            x=1
            z=1
            print("Car available for 4th and 2nd person")
        if(x==0):
            print("No cars available for 2nd person")
    
    if(c==d):
        print("Car available for 3rd and 4th person")
        y=1
        z=1
    if(y==0):
        print("No cars available for 3rd person")
    if(z==0):
        print("No cars available for 4th person")
else:
    print("Error in values inputed")
#Q11
x=int(input("Enter 1st number(right):"))
y=int(input("Enter 2nd number(left):"))
k=int(input("Enter number of jumps:"))
a=(k/2)*(x-y)
b=(k/2)*(x-y)+x
if(k%2==0):
    print("Final position:",a,"to the right") 
else:
    print("Final position:",b,"to the left")
#Q12
w = int(input("Enter the weight of the watermelon:"))
if (w%2==0)and(w!=2):
              print("Yes")
else:
    print("No")
#Q13
n=int(input("Enter number of sticks drawn:"))
k=int(input("Enter number of sticks to be crossed out:"))
if(n==k):
    print("Yes")
elif((n%k)==0)and((n/k)%2!=0):
    print("Yes")
else:
    print("No")
