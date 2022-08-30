from Kitchen import Kitchen
from Hall import Hall
from Bedroom import Bedroom


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


room1 = Kitchen(4, 4, 4, 3)
room1.display_info()
print("Площадь стен - ", room1.total_square(), "квадратных метров")
print("Площадь стен без двери и окна - ", room1.real_square(), "квадратных метров")
l = 'd'
w = l
h = l
s = l
while isfloat(l) == 0:
    print("Введите длину комнаты")
    l = input()
while isfloat(w) == 0:
    print("Введите ширину комнаты")
    w = input()
while isfloat(h) == 0:
    print("Введите высоту комнаты")
    h = input()
while isfloat(s) == 0:
    print("Введите количество спальных мест")
    s = input()
room2 = Bedroom(l, w, h, s)
room2.display_info()
room3 = Hall(6.2, 4.8, 3.7, 12)
room3.display_info()
