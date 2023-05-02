n = int(input('Введите размер первого набора: '))
n_set = set()
for i in range(n):
    n_set.add(input(f'Введите {i+1} число: '))
m = int(input('Введите размер второго набора: '))
m_set = set()
for i in range(m):
    m_set.add(input(f'Введите {i+1} число: '))
if n > m:
    n = n_set.intersection(m_set)
    a = list(n)
    a.sort()
    print(a)
else:
    m = m_set.intersection(n_set)
    b = list(m)
    b.sort()
    print(b)