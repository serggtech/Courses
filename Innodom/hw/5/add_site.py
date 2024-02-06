# Задача 1
# Создайте список с числами, переведите этот список в массив array и обратно в список.

from array import *

list_number = [1, 2, 3, 4, 5, 6]
print(list_number)
array_number = array("i", list_number)
print(array_number)
array_number = list(array_number)
print(array_number)
print()
array_number_1 = array("i")
array_number_1.fromlist(list_number)
print(array_number_1)
array_number_1 = list(array_number_1)
print(array_number_1)


# Задача 2
# Создайте массив array со значениями от 1 до 10000. Переведите этот массив в массив байтов.

my_array = array("i", range(1, 10001))
# print(my_array)
my_bytes_array = my_array.tobytes()
# print(my_bytes_array)


# Задача 3
# Создайте 3 массива с числами от 10 до 100 с разными типами.
# В каждом массиве выведите его тип, размер в байтах 1 элемента и информацию: ячейка памяти, длина.

array_int = array("i", range(10, 101))
array_float = array("f", [float(x) for x in range(10, 101)])
array_byte = array("b", [x for x in range(10, 101)])


print("Массив array_int:")
print("Тип элементов:", array_int.typecode)
print("Размер элемента (в байтах):", array_int.itemsize)
print("Ячейка памяти и длина массива:", array_int.buffer_info())
print()
print("Массив array_float:")
print("Тип элементов:", array_float.typecode)
print("Размер элемента (в байтах):", array_float.itemsize)
print("Ячейка памяти и длина массива:", array_float.buffer_info())
print()
print("Массив array_byte:")
print("Тип элементов:", array_byte.typecode)
print("Размер элемента (в байтах):", array_byte.itemsize)
print("Ячейка памяти и длина массива:", array_byte.buffer_info())


# Задача 4
# Пользователь вводит 2 числа — это диапазон, требуется создать список на эти числа.
# Есть массив array [1,2,3,4,5,6,7,8,9,10]. Расширьте массив значениями из сгенерированного списка.
print()
my_array = array("i", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

generated_list = list(range(start, end + 1))

my_array.extend(generated_list)

print(my_array)
