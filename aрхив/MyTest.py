import unittest
from tkinter.ttk import Widget

from Kitchen import Kitchen
from Hall import Hall
from Bedroom import Bedroom
import pickle

from Room import Room
from SanPinError import SanPinError


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def len_wid_hei():
    l = w = h = "k"
    while isfloat(l) & isfloat(w) & isfloat(h) == 0:
        l = input("Длина: ")
        w = input("Ширина: ")
        h = input("Высота: ")
        print(Room(float(l), float(w), float(h)).display_info())
    return Room(float(l), float(w), float(h))


FILENAME = "lab5.dat"


class Storage:
    def __init__(self):
        self.mas = []
        self.errors = 0

    def read(self):
        try:
            with open(FILENAME, "rb") as file:  # сначала читаем из файла что там есть
                room = pickle.load(file)
                for ob in room:
                    str1 = ob.split(" ")
                    if str1[0] == "kitchen":
                        self.mas.append(Kitchen(str1[1], str1[2], str1[3], str1[4]))
                    elif str1[0] == "bedroom":
                        self.mas.append(Bedroom(str1[1], str1[2], str1[3], str1[4]))
                    elif str1[0] == "hall":
                        self.mas.append(Hall(str1[1], str1[2], str1[3], str1[4]))
            self.errors = 0
        except Exception as e:
            print(e)
            self.errors = 666
        finally:
            return self.errors

    def add(self):
        try:
            flag = input("Хотите себе комнату?(введите 1 если да и что-нибудь другое если нет): ")
            while flag == "1":
                room = input("Добавить кухню - k\nДобавить спальню - b\nДобавить гостиную - h\n")
                ob = len_wid_hei()
                t = -2
                if room == "k":
                    t = float(input("Количество техники:"))
                    if 0 < ob.floor() / t < 1:
                        raise SanPinError("Слишком большое количество техники на кв. метр! Это кухня а не склад!")
                    self.mas.append(Kitchen(ob.length, ob.width, ob.height, t))
                elif room == "b":
                    t = float(input("Количество людей:"))
                    if 0 < ob.floor() / t < 2:
                        raise SanPinError("Недопустимые нормы проживания! Это спальня а не барак!")
                    self.mas.append(Bedroom(ob.length, ob.width, ob.height, t))
                elif room == "h":
                    t = float(input("Количество мест для сидения:"))
                    if 0 < ob.floor() / t < 1.5:
                        raise SanPinError("Нарушение норм СанПин! Это гостиная аристократов а не ночной клуб!")
                    self.mas.append(Hall(ob.length, ob.width, ob.height, t))
                if __debug__ == 1:
                    if t < 0:
                        raise AssertionError("Incorrect amount!!!")
                for k in self.mas:
                    k.display_info()
                self.errors = 0
                flag = input("Хотите добавить еще комнату?(введите 1 если да и что-нибудь другое если нет): ")
        except Exception as e:
            print(e)
            self.errors = 666
        finally:
            return self.errors

    def write(self):
        try:
            write_or_not = input("Записать данные в файл?(введите 1 если да и что-нибудь другое если нет): ")
            if write_or_not == "1":
                with open(FILENAME, "wb+") as file:
                    rooms = []
                    for a in self.mas:
                        rooms.append(a.str_to_file())
                    pickle.dump(rooms, file)
            self.errors = 0
        except Exception as e:
            print(e)
            self.errors = 666
        finally:
            return self.errors


class TestRooms(unittest.TestCase):
    def setUp(self):
        self.ob = Storage()

    def test_aaread(self):
        self.assertEqual(self.ob.read(), 0)
        self.assertEqual(self.ob.add(), 0)
        self.assertEqual(self.ob.write(), 0)

    def test_add(self):
        pass
        # self.assertEqual(self.ob.add(), 0)

    def test_write(self):
        pass
        # self.assertEqual(self.ob.write(), 0)


if __name__ == "__main__":
    unittest.main()
