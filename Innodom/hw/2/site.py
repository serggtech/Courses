# Задача 1
## Вычислите, результаты выведите в консоль:
print("Вычислите, результаты выведите в консоль:")
print()
print("X + 35 = 12")
X = -35 + 12
print("X =", X)
print()

print("Y – 32 = 1")
Y = 32 + 1
print("Y =", Y)
print()

print("Z * 7 / 2 / 3 = 7")
Z = 2 * 3 * 7 / 7
print("Z =", Z)
print()

# Задача 2
## У вас есть число a = 70. Увеличьте данное число на 10, а затем уменьшите его на 2.
## Работайте только с переменной a. Промежуточные результаты выведите в консоль.
print(
    "У вас есть число a = 70. Увеличьте данное число на 10, а затем уменьшите его на 2.\n",
    "Работайте только с переменной a. Промежуточные результаты выведите в консоль.",
    sep="",
)
print()
a = 70
print("a =", a)
a += 10
print("a =", a)
a -= 2
print("a =", a)
print()

# Задача 3
## Пользователь вводит два числа.
## Примените все операции, изученные на занятии, к данным числам. Результаты выведите в консоль.

print(
    "Пользователь вводит два числа.\n",
    "Примените все операции, изученные на занятии, к данным числам. Результаты выведите в консоль.",
    sep="",
)
print()

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
print()
# Сложение
print("Сложение:", "a + b =", a + b)
print()
# Вычитание
print("Вычитание:", "a - b =", a - b)
print()
# Умножение
print("Умножение:", "a * b =", a * b)
print()
# Деление
print("Деление:", "a / b =", a / b)
print()
# Целочисленное деление
print("Целочисленное деление:", "a // b =", a // b)
print()
# Остаток от деления
print("Остаток от деления:", "a % b =", a % b)
print()
# Возведение в степень
print("Возведение в степень:", "a ** b =", a ** b)
print()
