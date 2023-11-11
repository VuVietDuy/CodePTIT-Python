a = input()
c = 0
for i in a:
    if(i.islower()): c+=1
if(c*2 >= len(a)):
    print(a.lower())
else:
    print(a.upper())