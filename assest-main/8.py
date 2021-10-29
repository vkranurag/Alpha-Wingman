a=input()
a=a.split('.')
a.pop()
print(a[0],end='.')
for i in (1,len(a)-1):
    if a[i][0].islower:
        print(a[i][0].upper(),a[i][1:],sep='',end='')
    else:
        print(a[i],end='')
    print('.',end='')
