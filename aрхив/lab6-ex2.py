import random
import multiprocessing
from math import sqrt
from time import time

N = 5000  # 20 номер в списке -> формула 5 варианта с использованием многопроцессорности


# Спойлер: многопроцессорность - 13 с, один поток - 24 с


class Storage:
    def __init__(self):
        self.P = []
        self.Q = []
        self.R1 = [0] * N
        for i in range(N):
            self.P.append(random.randint(-10, 10))
            self.Q.append(random.randint(-10, 10))
            self.R1[i] = [0] * N

    def formula(self, j, i):
        n = round(sqrt(abs(self.Q[j] - self.P[i])), 2)
        return n

    def without(self):
        for i in range(N):
            for j in range(N):
                self.R1[i][j] = self.formula(j, i)

    def first_half(self, start, stop):
        mas = [0] * (N // 2)
        for i in range(N // 2):
            mas[i] = [0] * N
        for i in range(0, N // 2):
            for j in range(N):
                mas[i][j] = self.formula(j, i + start)
        return mas


if __name__ == "__main__":
    ob = Storage()
    temp = time()
    p = multiprocessing.Pool(2)
    a, b = p.starmap(ob.first_half, [(0, N // 2), (N // 2, N)])
    p.terminate()
    print("Мультипроцессинг - ", str(time() - temp))
    temp = time()
    ob.without()
    print("Выполнение в один поток - ", str(time() - temp))
    #print("В один поток     - ", ob.R1)
    #print("Мультипроцессинг - ", a + b)
