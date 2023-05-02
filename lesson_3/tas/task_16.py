n=int(input('Введите размер элементов списка '))
list_n = input('Введите элементы списка через пробел: ')
arr = list(map(int,list_n))
while len(arr) != n:
    list_n = input('Введите элементы списка через пробел: ')
    arr = list(map(int,list_n))
else:
    x = int(input('Введите число: '))
    count = 0
    for i in range(n):
        if arr[i]==x:
            count+=1
print(f'Число, которое вы ввели встречается в массиве {count} раз')

