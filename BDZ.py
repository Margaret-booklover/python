import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

pd.set_option('display.max_columns', None)  # чтобы отображались все столбцы
pd.set_option('display.max_rows', 50)  # чтобы отображались все строки

data = pd.read_csv('train.csv')

# 1. С помощью модуля pandas выведите статистику погибших/выживших отдельно
# для мужчин и женщин в каждом классе (Pclass)
for i in range(1, 4):
    Class = i
    mas = [0, 0, 0, 0]  # временный массив, где будет собираться информация
    for string in data.iterrows():
        string = string[1]  # получаем строку данных, нулевой индекс - это индекс ряда, он нам не нужен
        if string.Pclass == Class:  # собираем статистику по конкретному классу
            if string.Sex == 'female':  # собираем статистику по женщинам
                if string.Survived == 1:
                    mas[0] = mas[0] + 1  # выжившие
                else:
                    mas[1] = mas[1] + 1  # погибшие
            else:  # собираем статистику по мужчинам
                if string.Survived == 1:
                    mas[2] = mas[2] + 1  # выжившие
                else:
                    mas[3] = mas[3] + 1  # погибшие
    print("      Статистика для пассажиров класса ", i)
    print("  Женщины:\nВыжило - ", mas[0])
    print("Погибло - ", mas[1])
    print("  Мужчины:\nВыжило - ", mas[2])
    print("Погибло - ", mas[3])

# 2. С помощью модуля pandas выведите статистику по всем числовым полям, отдельно для мужчин и женщин
print("\n\t\tЖенщины, статистика по всем числовым полям\n", data[data.Sex == 'female'].describe())
print("\n\t\tМужчины, статистика по всем числовым полям\n", data[data.Sex == 'male'].describe())

# 3. Влияет ли порт посадки на выживаемость?
c = [0, 0]  # создаем по массиву на каждый порт
q = [0, 0]
s = [0, 0]
for string in data.iterrows():
    string = string[1]
    if string.Embarked == 'C':  # статистика для порта С
        if string.Survived == 0:  # погибшие
            c[0] = c[0] + 1
        else:
            c[1] = c[1] + 1  # и выжившие
    elif string.Embarked == 'Q':  # остальные два порта аналогично
        if string.Survived == 0:
            q[0] = q[0] + 1
        else:
            q[1] = q[1] + 1
    elif string.Embarked == 'S':
        if string.Survived == 0:
            s[0] = s[0] + 1
        else:
            s[1] = s[1] + 1
print("\nИсследование влияния порта посадки на выживаемость")
print("Порт\t\tВыжило\tПогибло\tВо сколько раз выживших больше чем погибших")
print("Cherbourg    {}\t\t{}\t\t{}".format(c[1], c[0], c[1] / c[0]))
print("Queenstown   {}\t\t{}\t\t{}".format(q[1], q[0], q[1] / q[0]))
print("Southampton  {}\t{}\t\t{}".format(s[1], s[0], s[1] / s[0]))
# Из результатов анализа видно, что процент выживших больше для порта Cherbourg, то есть из
# полученной статистики можно предположить, что порт скорее всего влияет на выживаемость

# 4. Выведите топ 10 популярных имён
mas = data.Name.apply(lambda name: name.split(',')[0])  # нам нужны только имена, они на первом месте поля
print("\n\tтоп 10 популярных имён")
print(mas.value_counts().head(10))

# 5. Заполните все отсутствующие в train.csv значения медианой (по столбцу)
print("Проверка столбцов на наличие пустых значений\n", data.isnull().any())
# В файле три столбца с пустыми ячейками: Age, Cabin, Embarked
# так как последния два поля не числовые, нам остается работать только с полем "Возраст"
data.Age = data.Age.fillna(data.Age.median())
print("Проверка что больше поля возраста не пусты:\n", data.isnull().any())
# Значение поля "Возраст" должно измениться на False

# 6. На основе статистики попытайтесь предсказать выживаемость для пассажиров из файла test.csv
data2 = pd.read_csv('test.csv')  # читаем данные из второго файла
survived = data['Survived']  # столбец с ответами
data.Sex = LabelEncoder().fit_transform(data.Sex)  # поле "Пол" в обеих датафреймах сменим на тип инт - 0 или 1
data2.Sex = LabelEncoder().fit_transform(data2.Sex)
# отбрасываем не влияющие на выживаемость столбцы строкового типа
data = data.drop(['Name', 'Cabin', 'Embarked', 'Ticket', 'Survived'], axis=1)
data2 = data2.drop(['Name', 'Cabin', 'Embarked', 'Ticket'], axis=1)
data2 = data2.fillna(data2.Age.median())  # заполняем пустые ячейки медианой

clf = LogisticRegression(max_iter=200)  # Логистическая регрессия
clf.fit(data, survived)  # строим лес деревьев на тренировочном наборе
prediction = clf.predict(data2)  # пытаемся предсказать выживаемость для файла "тест"
accuracy = round(clf.score(data, survived) * 100, 2)
print(str(accuracy) + ' percent')
with open('result.txt', 'w') as file:
    for temp in prediction:
        file.write(str(temp) + '\n')  # записываем результаты в файл
print("\nРезультаты задания - в файле result.txt")
