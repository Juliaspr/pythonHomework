a = int(input())
b = int(input())
c = int(input())
s = float(0)

def area (a, b, c):
    s = (((a+b+c)/2)*(((a+b+c)/2)-a)*(((a+b+c)/2)-b)*(((a+b+c)/2)-c))** 0.5
    print(s)

area(a, b, c)