# Занятие 2
## Задача 1
print("Вывести тип и результат выражения 3/2.:", type(3 / 2))

## Задача 2
print("Пользователь вводит 2 числа. Нужно вывести на экран остаток от их деления.")
print()
nubmer_one = int(input("Введите число 1: "))
number_two = int(input("Введите число 2: "))
print("Остаток от их деления:", (nubmer_one % number_two))

## Задача 3
print("Пользователь вводит трёхзначное число. Нужно вывести на экран сумму его цифр.")
print()
num = int(input("Введите трёхзначное число: "))
digit_one = (num // 100)
digit_two = (num - (digit_one * 100)) // 10
digit_three = num - ((digit_two * 10) + (digit_one * 100))
print('Сумма его цифр:', (digit_one + digit_two + digit_three))

## Задача 4
print(
    "Создайте четыре переменные a, b, c, d, присвойте им разные значения. Затем поменяйте их значения местами без "
    "использования дополнительных переменной.")
print()
a, b, c, d = "a", "b", "c", "d"
print("До замены значений :", a, b, c, d)
a, b, c, d = d, c, b, a
print("После замены хначений :", a, b, c, d)

## Задача 5
print(
    'Создайте три переменные со строками. Используйте print(), чтобы вывести эти переменные на одной строке, '
    'разделяя их конструкцией " : ". Закончите вывод символом ".".')

string_a = 'string_a'
string_b = 'string_b'
string_c = 'string_b'

print()
print(string_a, string_b, string_c)
print()
print(string_a, string_b, string_c, sep=':', end='.')
print()
