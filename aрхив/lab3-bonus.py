import random

n = random.randint(1, 10)
a = []
for i in range(1, n + 1):
    a.append(random.randrange(1, 10))
print(a)
x = random.randrange(1, 20)
print("x = ", x)
result = []
flag = 0
if sum(a) >= x:
    for i in a:
        if x < i:
            flag = flag + 1
        tempsum = i
        k = a.index(i)
        result = [i]
        while (tempsum < x) & (tempsum < sum(a)) & (k < n-1):
            tempsum = tempsum + a[k+1]
            result.append(a[k+1])
            k = k + 1
        if sum(result) == x:
            print(result)
            break
    if (flag == n) | (sum(result) != x):
        print("False")
else:
    print("False")
