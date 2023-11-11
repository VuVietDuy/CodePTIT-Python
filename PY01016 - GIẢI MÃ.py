t = int(input())
while(t != 0):
    t-=1
    n = input()
    for i in range(0, len(n)-1, 2):
        c = int(n[i+1])
        while(c != 0):
            c-=1
            print(n[i], end='')
    print('')