# Задача 1
## Напишите программу, которая выводит прямоугольник, по периметру состоящий из звездочек *. Высоту и ширину должен ввести пользователь с консоли. (значение минимум 4)
## Если высота = 3, а ширина равна 8, то прямоугольник выглядит так:
## ********
## *      *
## ********
## P.S.: для начала можете решить упрощенную задачу и вывести прямоугольник размером как в примере.
print()
width = int(input("a сторона ширина: "))
height = int(input("b сторона высота: "))

star = "*"
space = " "

zvezda_width = star + "" + (star * (width - 2)) + "" + star
space_height = (star + "" + (space * (width - 2)) + "" + star + "\n") * (height - 2)
print()
print(zvezda_width)
print(space_height, end="")
print(zvezda_width)

# Задача 2
## Отформатируйте текст между кавычками:
## “                                     наше Солнце и ближайшие к нему звезды являются частью обширного звездного скопления — галактики Млечный Путь. долгое время люди думали, что это и есть вся Вселенная. только в 1924 г. американский астроном Эдвин Хаббл показал, что наша Галактика — не единственная во Вселенной. На самом деле существует много других галактик, разделенных огромными участками пустого пространства. чтобы доказать это, ему потребовалось измерить расстояния до этих галактик. мы можем определить расстояния до ближайших звезд, наблюдая изменение их положений на небе по мере обращения Земли вокруг Солнца. но другие галактики находятся так далеко, что в отличие от ближайших звезд кажутся неподвижными. поэтому Хабблу пришлось использовать косвенные методы измерения расстояний.                   ”
print()

string_start = "                                     наше Солнце и ближайшие к нему звезды являются частью обширного звездного скопления — галактики Млечный Путь. долгое время люди думали, что это и есть вся Вселенная. только в 1924 г. американский астроном Эдвин Хаббл показал, что наша Галактика — не единственная во Вселенной. На самом деле существует много других галактик, разделенных огромными участками пустого пространства. чтобы доказать это, ему потребовалось измерить расстояния до этих галактик. мы можем определить расстояния до ближайших звезд, наблюдая изменение их положений на небе по мере обращения Земли вокруг Солнца. но другие галактики находятся так далеко, что в отличие от ближайших звезд кажутся неподвижными. поэтому Хабблу пришлось использовать косвенные методы измерения расстояний.                   "
print(f"Неформатированная строка: {string_start}")
string_format = string_start.lstrip().rstrip().capitalize()
print()
print(f"Форматированная строка: {string_format}")

# Задача 3
## Пользователь вводит строку и подстроку. Необходимо найти индекс первого и последнего вхождения подстроки в строку и вывести их на экран.
print()

user_string = input("Введите строку: ")
user_sub_string = input("Введите подстроку: ")
print()
print(
    f"Индекс первого вхожднения подстроки в строку: {user_string.find(user_sub_string)} \n"
    f"Индекс последнего вхождения подстроки в строку: {user_string.rfind(user_sub_string)}"
)

# Задача 4
## Напишите программу, которая выведет на экран подстроку от 7 до 15 (включительно) символа с конца и в обратном порядке.
#
## Consectetur accumsan dui in pulvinar dui ipsum sed hac imperdiet accumsan ut. Interdum malesuada dui vel arcu ultricies. Faucibus. Orci, vitae mattis libero, in sed dictumst. Urna tempus nulla luctus elit. Non eget habitasse sodales libero, tempus quam, eleifend ex. Molestie vulputate amet in malesuada leo, molestie mollis ultricies. Mollis pellentesque sed id cras consectetur integer sed vulputate nulla malesuada molestie in et mattis platea amet vel et adipiscing quis.
print()
string_str = (
    "Consectetur accumsan dui in pulvinar dui ipsum sed hac imperdiet accumsan ut. Interdum malesuada dui "
    "vel arcu ultricies. Faucibus. Orci, vitae mattis libero, in sed dictumst. Urna tempus nulla luctus "
    "elit. Non eget habitasse sodales libero, tempus quam, eleifend ex. Molestie vulputate amet in "
    "malesuada leo, molestie mollis ultricies. Mollis pellentesque sed id cras consectetur integer sed "
    "vulputate nulla malesuada molestie in et mattis platea amet vel et adipiscing quis."
)

print(string_str[-7:-15:-1])

# Задача 5
## Есть строка "<248>". Напишите программу, которая выведет на экран произведение чисел этой строки.
print(
    'Есть строка "<248>". Напишите программу, которая выведет на экран произведение чисел этой строки.'
)
print()
string_start = "<248>"
string_start_new = string_start[1:4]
print(
    f"Произведение чисел этой строки: {int(string_start_new[0]) * int(string_start_new[1]) * int(string_start_new[2])}"
)

# Задача 6
## Пользователь вводит строку. Напишите программу, которая разрежет строку пополам, переставит эти части местами и выведет результат на экран.
print(
    "Пользователь вводит строку. Напишите программу, которая разрежет строку пополам, переставит эти части местами и выведет результат на экран."
)
print()
user_string = input("Пользователь вводит строку: ")
print()
user_string_len = len(user_string)
user_string_len_half = int(user_string_len) // 2
# print(user_string_len)
# print(int(user_string_len_half))

print(
    f"{user_string[user_string_len_half:user_string_len]}{user_string[0:user_string_len_half]}"
)
print()
print("А теперь в одну строку")
print()
print(
    f"{user_string[(len(user_string) // 2):len(user_string)]}{user_string[0:(len(user_string) // 2)]}"
)

# Задача 7
## Пользователь вводит строку, где слова разделены пробелом. Напишите программу, которая выведет на экран количество слов в строке. (Не используйте то, что мы ещё не изучали)
print(
    "Пользователь вводит строку, где слова разделены пробелом. Напишите программу, которая выведет на экран количество слов в строке. (Не используйте то, что мы ещё не изучали)"
)
print()
user_string = input("Пользователь вводит строку, где слова разделены пробелом: ")
print()
print(user_string)
user_string_count_space = user_string.count(" ")
print(f"Количество пробелов в строке: {user_string_count_space}")
print(f"Количество символов в строке: {len(user_string) - user_string_count_space}")
user_string_split = user_string.split(" ")
print(f"Количество слов в строке: {len(user_string_split)}")
print()
print("А теперь в одну строку")
print()
print(f"Количество слов в строке: {len(user_string.split(' '))}")
