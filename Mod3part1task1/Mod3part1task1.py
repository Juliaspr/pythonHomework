x = float(input())
p = int(input())
y = float(input())
i=0

while x <= y:
    x = x + (x*p/100)
    x = x//1

    i+=1
print(i)
