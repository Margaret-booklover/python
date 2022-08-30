import random

n = random.randint(2, 5)  # маленькая длина исключительно для простоты проверки
a = []  # исходный массив
b = []  # массив который по длине равен а и заполнен единицами - таким должен стать а
for i in range(0, n):
    a.append(random.randrange(1, 5))  # маленькие значения исключительно для простоты проверки
    b.append(1)
print(a)
k = 0
while a != b:
    maxx = a[0]
    minn = maxx
    max_i = 0
    min_i = 0
    for i in range(0, len(a)):
        if a[i] > maxx:  # поиск максимума
            maxx = a[i]
            max_i = i
        if a[i] < minn:  # поиск минимума
            minn = a[i]
            min_i = i
    if minn == maxx:
        k = 0
        break
    a[max_i] = a[max_i] - a[min_i]  # уменьшение максимального элемента на минимальный
    k = k + 1
print(k)
