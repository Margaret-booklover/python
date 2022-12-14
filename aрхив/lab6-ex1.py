from queue import Queue
from threading import Thread


def example(temp, n):
    ob = temp.get()
    print("Номер потока, значение: ", n, ob)


q = Queue(10)  # У меня 20 номер по списку, это 5 вариант, работа с очередью:
for i in range(10):
    q.put(i)
for i in range(10):
    t1 = Thread(target=example, args=(q, i))
    t1.start()
    t1.join()

# Синхронизация семафором: Счетчик уменьшается, когда к семафору получают доступ, и увеличивается,
# когда доступ к нему теряют. Если счетчик доходит до нуля, когда к семафору получен доступ,
# то поток блокируется

# Синхронизация условием: поток может дожидаться заданных условий, или сигнал
# о том, что условие было задано

# Синхронизация событием: Объект класса Event управляет внутренним флагом, который сбрасывается
# с помощью метода clear() и устанавливается методом set(). Потоки, которые используют объект Event
# для синхронизации блокируются при вызове метода wait(), если флаг сброшен

# Синхронизация барьером: необходимо дождаться завершения работы группы потоков, прежде
# чем продолжить выполнение задачи
