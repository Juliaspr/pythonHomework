from random import randint

n = 5
m = [[randint(0,100) for i in range(n)] for j in range(n)]
print(m)
max = 0

for i in range(0,n):
    for j in range(0,n):
        if max<m[i][j]:
            max = m[i][j]
print(max)