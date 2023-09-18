n = int(input("Введите кол-во монет: "))
zero_count = 0
one_count = 0
for i in range(n):
    temp = int(input("Введите 0 или 1: "))
    if temp > 0:
        one_count += 1
    else:
        zero_count += 1
if zero_count > one_count:
    print(one_count)
else:
    print(zero_count)
