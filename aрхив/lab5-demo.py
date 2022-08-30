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
mas = []
try:
    with open(FILENAME, "rb") as file:  # сначала читаем из файла что там есть
        room = pickle.load(file)
        for ob in room:
            str1 = ob.split(" ")
            if str1[0] == "kitchen":
                mas.append(Kitchen(str1[1], str1[2], str1[3], str1[4]))
            elif str1[0] == "bedroom":
                mas.append(Bedroom(str1[1], str1[2], str1[3], str1[4]))
            elif str1[0] == "hall":
                mas.append(Hall(str1[1], str1[2], str1[3], str1[4]))

    for k in mas:
        k.display_info()  # и выводим это на экран
    flag = input("Хотите себе комнату?(введите 1 если да и что-нибудь другое если нет): ")
    while flag == "1":
        room = input("Добавить кухню - k\nДобавить спальню - b\nДобавить гостиную - h\n")
        ob = len_wid_hei()
        t = -2
        if room == "k":
            t = float(input("Количество техники:"))
            if 0 < ob.floor() / t < 1:
                raise SanPinError("Слишком большое количество техники на кв. метр! Это кухня а не склад!")
            mas.append(Kitchen(ob.length, ob.width, ob.height, t))
        elif room == "b":
            t = float(input("Количество людей:"))
            if 0 < ob.floor() / t < 2:
                raise SanPinError("Недопустимые нормы проживания! Это спальня а не барак!")
            mas.append(Bedroom(ob.length, ob.width, ob.height, t))
        elif room == "h":
            t = float(input("Количество мест для сидения:"))
            if 0 < ob.floor() / t < 1.5:
                raise SanPinError("Нарушение норм СанПин! Это гостиная аристократов а не ночной клуб!")
            mas.append(Hall(ob.length, ob.width, ob.height, t))
        if __debug__ == 1:
            if t < 0:
                raise AssertionError("\nIncorrect amount!!!\n")
        for k in mas:
            k.display_info()
        flag = input("Хотите добавить еще комнату?(введите 1 если да и что-нибудь другое если нет): ")
    write_or_not = input("Записать данные в файл?(введите 1 если да и что-нибудь другое если нет): ")
    if write_or_not == "1":
        with open(FILENAME, "wb+") as file:
            rooms = []
            for a in mas:
                rooms.append(a.str_to_file())
            pickle.dump(rooms, file)
except EOFError:

    print("файл был пустой, а так не пойдет, я дописала в него дефолтное значение, попробуй запустить снова")
    with open(FILENAME, "wb") as file:
        pickle.dump(Kitchen().str_to_file(), file)
    mas.append(Kitchen())
except IndexError as e:
    print("Сведения об исключении: ", e)
    print("А если по-русски, то где-то индекс поплыл, надо искать")
except ValueError:
    print("скорее всего программа не прошла тест на дуракоустойчивость...")
except FileNotFoundError:
    print("Файл не найден. Либо ошибка в имени, либо его не существует, либо его отсюда не видно")
except IOError:
    print("критический сбой базовой файловой системы или доступ к "
          "некоторому ресурсу, который связывает Python с файловой системой")
except SanPinError as e:
    print(e)
except AssertionError as e:
    print(e)
except Exception as e:
    print("Что-то пошло не так...", e)
finally:
    print("Блок try завершил выполнение")
