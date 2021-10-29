a=[]
for x in range(5):
    a.append((input().split(',')))
for x in range(5):
    for y in range(len(a[x])):  
        print(a[x][y],end=' ')
    print()
