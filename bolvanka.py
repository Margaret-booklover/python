import time
from random import randint


def shaker_sorting(mas):
    n = len(mas)
    flag = True
    begin = 0
    end = n - 1
    while flag:
        flag = False  # на каждой итерации полагаем сначала, что не было перестановок
        for i in range(begin, end):  # идем в одну сторону (к концу)
            if mas[i] > mas[i + 1]:  # если текущий элемент больше следующего,
                mas[i], mas[i + 1] = mas[i + 1], mas[i]  # меняем их местами
                flag = True  # совершена хотя бы одна перестановка
        if not flag:  # если не было перестановок цикл заканчивается
            break
        for i in range(end - 2, begin - 1, -1):  # идем в другую сторону (к началу)
            if mas[i] > mas[i + 1]:
                mas[i], mas[i + 1] = mas[i + 1], mas[i]  # обмен элементов
        end = end - 1
        begin = begin + 1


repeat = int(input("Введите число экспериментов: "))
for k in range(repeat):
    temp = []
    length = int(input("Длина массива вводится вручную: "))
    for i in range(0, length):
        temp.append(randint(1, 10))  # заполнение случайными числами
    # print(temp)  # есть возможность проверить работу сортировки на маленьких массивах
    start_time = time.time()
    shaker_sorting(temp)
    print(time.time() - start_time)
    # print(temp)
