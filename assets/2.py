def sort(x):
    return x[2]
a=[]
ch='y'
while ch=='y':
    a.append(input().split(' '))
    ch=input("do u want to add more?(y/n)")
print(a)
a.sort(reverse=True,key=sort)
print(a)
