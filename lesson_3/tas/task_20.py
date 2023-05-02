n = input('Введите слово: ').upper()
arr = list(n)
list_1 = ('A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R','А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т')
list_2 = ( 'D', 'G','Д', 'К', 'Л', 'М', 'П', 'У')
list_3 = ( 'B', 'C', 'M', 'P','Б', 'Г', 'Ё', 'Ь', 'Я')
list_4 = ('F', 'H', 'V', 'W', 'Y', 'Й', 'Ы')
list_5 = ('K','Ж', 'З', 'Х', 'Ц', 'Ч')
list_8 = ('J', 'X', 'Ш', 'Э', 'Ю')
list_10 = ('Q', 'Z', 'Ф', 'Щ', 'Ъ')
count = 0
for i in range(len(n)):
    if arr[i] in list_1:
        count = count + 1
    elif arr[i] in list_2:
        count = count + 2
    elif arr[i] in list_3:
        count = count + 3
    elif arr[i] in list_4:
        count = count + 4
    elif arr[i] in list_5:
        count = count + 5
    elif arr[i] in list_8:
        count = count + 8
    else:
        count = count + 10
print(f'Кол-во очков: {count}')
