from math import*

def check(n):
    for i in range(2, int(sqrt(n)+1)):
        if(i%2 == 1):
            return False
    return bool(n>1)

t = int(input())
while(t != 0):
    t-=1
    a, b = [int(x) for x in input().split()]
    u = gcd(a,b)
    sum = 0
    while(u != 0):
        sum += u%10
        u = int(u/10)
    if(check(sum)): print("YES")
    else: print("NO")