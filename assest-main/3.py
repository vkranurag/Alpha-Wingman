a=input()
b=[]
for x in a:
    if x in b or x==" ":
        continue
    else:
        c=1
        for y in a:
            if x==y:
                c+=1
    b.append(x)
    print(x,"-",c-1)
