import math
n = input('Введите размер массива: ')
list_n = input('Введите элементы массива ')
arr = list(map(int,list_n))
while len(arr) != n or n ==0:
    n = input('Введите размер массива: ')
    list_n = input('Введите элементы массива ')
    arr = list(map(int,list_n))
else:
    x = int(input('Введите число: '))
    close = 0
    min = abs(x-arr[0])
    for i in range(n):
        dif = abs(x-arr[i])
        if dif < min:
            min = dif
            close = arr[i]
print(f'Ближайшее число к введенному является {close}')