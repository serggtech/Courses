# Задача 1
# Напишите программу, которая создаёт единичную матрицу с длиной 10.
# Вычислите sin всех элементов матрицы. Умножьте её на 10 и посчитайте сумму.
# Все действия необходимо выполнить в 1 строку.

import numpy as np

print(np.sum(10 * np.sin(np.eye(10))))


# Задача 2
# Массив состоит из 10 строк различной длины.
# Посчитайте количество символов, содержащихся в каждом элементе массива.
# Для поиска функции воспользуйтесь документацией.
print()
my_array = [
    "Hello",
    "Python",
    "World",
    "String",
    "List",
    "Hakaton",
    "NumPy",
    "Array",
    "Length",
    "InnoDom",
]


lengths = list(map(len, my_array))
print(lengths)
