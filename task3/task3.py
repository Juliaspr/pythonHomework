num1 = float(input())
num2 = float(input())

max1 = (num1 > num2) * num1 + (num2 > num1) * num2

print('max = ', max1)
