degree = 0
n = int(input("Введите число : S "))
while 2**degree < n:
    print(2**degree , end =" " )
    degree +=1
