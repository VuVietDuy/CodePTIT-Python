t = int(input())
while (t != 0):
    t-=1
    n = input()
    a = list(int(i) for i in n)
    if(len(a) == 1):
        print(n)
    else:
        for i in range(len(a)-2, -1, -1):
            if(a[i+1] >= 5):
               a[i]+=1
            a[i+1] = 0
        for i in a:
            print(i,end='')
        print('')