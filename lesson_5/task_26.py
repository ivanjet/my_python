a = int(input('Введите число: '))
b= int(input('Введите степень: '))
a1=a
def setDegree(a,b):
    if b == 0:
        return 1

    return a * setDegree(a, b - 1)
print(setDegree(a, b))