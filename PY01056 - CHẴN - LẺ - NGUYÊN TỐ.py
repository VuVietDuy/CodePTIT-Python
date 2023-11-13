import math as m

def check(n):
    sum = 0
    for i in range(len(n)):
        a = int(n[i])
        sum += a
        if(i%2 == 0 and a%2 != 0):
            return False
        if(i%2 != 0 and a%2 == 0):
            return False
    return checkSnt(sum)

def checkSnt(x):
    for i in range(2, int(m.sqrt(x))):
        if(x%i == 0):
            return False
    return True

t = int(input())
while(t != 0):
    t-=1
    n = input()
    if(check(n) == True):
        print("YES")
    else:
        print("NO")
