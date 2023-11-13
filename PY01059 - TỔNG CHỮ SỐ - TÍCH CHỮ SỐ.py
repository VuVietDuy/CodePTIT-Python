t = int(input())
while(t != 0):
    t-=1
    n = input()
    sum = 0
    tich = 1
    oke = False
    for i in range(len(n)):
        a = int(n[i])
        if(i%2 == 0):
            sum += a
        if(i%2 != 0 and a != 0):
            tich *= a
            oke = True
    if(oke == False):
        tich = 0
    print(sum, tich)

