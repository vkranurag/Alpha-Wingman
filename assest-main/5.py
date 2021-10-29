a=input()
b=a.split(" ")
c=0
for x in b:
    if len(x)>c:
        c=len(x)
print(c)
