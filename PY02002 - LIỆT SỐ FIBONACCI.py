
fib = [0, 1]  

for i in range(2, 94):
    next_fib = fib[-1] + fib[-2]  
    fib.append(next_fib) 

t = int(input())
while(t != 0):
    t-=1
    a, b = [int(i) for i in input().split()]
    for i in range(a, b+1):
        print(fib[i], end=' ')
    print('')