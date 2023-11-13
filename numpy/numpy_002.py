import numpy as np

ar = np.array([(-3,2,3), (1,9,4), (2,4,6)])
max = min = ar[0,0]
for row in ar:
    for i in row:
        if(i>max): max = i
        if(i<min): min = i
print(max, min)