t = int(input())
while(t != 0):
    t-=1
    n = input()
    l = len(n)
    if(n[0:2] == n[l-2:l]):
        print("YES")
    else:
        print("NO")
