a, K, N = [int(i) for i in input().split()]
ok = False
for b in range(K-int(a%K), N-a+1, K):
    if((a+b)%K == 0):
        print(b, end=' ')
        ok = True
if(ok == False):
    print(-1)