import math
s = int(input("Введите число : S "))
p = int(input("Введите число : P "))
y = (-s + math.sqrt(s**2 - 4*p))/-2
x = s - y
print (int(x), int (y))
