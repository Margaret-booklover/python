import random

M = random.randint(2, 5)
print("M = ", M)
a = []  # исходный массив
for i in range(0, M):
    a.append(random.randrange(1, 30))
k = M

flag = True
while flag:
    b = []
    index1 = 0
    for i in range(index1 + 1, k):
        if a[i - 1] <= a[i]:
            b.append(a[i])
    if len(b) < M:
        a.append(random.randrange(1, 30))
        index1 = index1 + 1
    else:
        print("b ", b)
        flag = False
print("a ", a)

