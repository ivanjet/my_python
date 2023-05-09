a = int(input("Введите число "))
b = int(input("Введите число "))


def sum(a, b):
    if a == 0:
        return b
    else:
        return sum(a - 1, b + 1)


print(sum(a, b))