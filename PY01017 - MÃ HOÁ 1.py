t = int(input())
while(t != 0):
    t-=1
    n = input()
    temp = n[0]
    c = 0
    for i in n:
        if (i == temp):
            c+=1
        else:
            print(str(c)+temp, end='')
            c=1
            temp = i
    print(str(c)+temp, end='')
    temp = i
    print('')