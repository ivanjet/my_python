#task 2
a = int(input('Введите число: '))
sum = 0
while a >= 1:
    x = a % 10
    sum = sum + x
    a = a // 10
print(sum) 
#task 4
b = int(input('Введите итоговое количество сделанных игрушек: '))
if (b % 2 == 0 and b != 2):
    PS = b // 6
    K = PS * 4
    print('Дети сделали', int(b), 'игрушек', 'из них Катя сделала',int(K),',а Петя с Сережей по',int(PS),'игрушек' )
else :
    print("Решение невозможно")
#task 6
x = int(input('Введите шестизначный номер билета: '))
sum1 = 0
sum2 = 0
if (x/1000 > 100 and x/1000 < 1000) :
    while x > 1000:
       y1 = x % 10
       sum1  = sum1 +y1
       x = x//10
    while x >=1:
        y2 = x %10
        sum2 = sum2 + y2
        x= x//10         
else :
    print('Решение невозможно, так как в билете не шестизначный')
if ( sum1 == sum2):
    print('Ура, вы счастливчик!')
else:
    print('Увы, но ваш билет не счастливый, удачи в следующий раз')
#task 8
n = int(input())
m = int(input())
k = int(input())
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')