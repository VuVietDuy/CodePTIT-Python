t = int(input())

def check(n):
    for i in n:
        if(i != '4' and i != '7'):
            return False
    return True

while(t != 0):
    t-=1
    n = input()
    if(check(n)):
        print("YES")
    else:
        print("NO")