a=input()
a=a.split(' ')
for x in a:
    if len(x.split('@'))==2:
        print(x)
