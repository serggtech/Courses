# Задача 1
## Напишите программу, которая заменяет и удаляет всё лишнее из строки:
## “У в%%А№с вввв@c~ё ппп$$ПО&л%у**Ч**<>и!тс::я”
## Вывод представьте прописными буквами.
print('Напишите программу, которая заменяет и удаляет всё лишнее из строки: “У в%%А№с вввв@c~ё ппп$$ПО&л%у**Ч**<>и!тс::я”')
print()
string_not_format = 'У в%%А№с вввв@c~ё ппп$$ПО&л%у**Ч**<>и!тс::я'
print(string_not_format)
print()
string_new_format = (string_not_format.replace('%', '')
                     .replace('№', '').replace('ввв', '')
                     .replace('@', '').replace('~', '')
                     .replace('ппп$$', '').replace('&', '')
                     .replace('*', '').replace('<>', '')
                     .replace('!', '').replace(':', ''))

print(string_new_format)
print()

print(string_new_format.upper())


# Задача 2
## Переведите сообщение пользователя на числа. Каждое сообщение состоит из 6 букв, вам нужно с помощью функции ord() перевести сообщения и сформировать строку из чисел.
## Например: привет -> “1087 1088 1080 1074 1077 1090”
print()
print("Переведите сообщение пользователя на числа.")
print()
user_msg = input("Введите сообщение пользователя из 6 букв: ")
print(f"Вы ввели: {user_msg} ->"
      f" {ord(user_msg[0])} {ord(user_msg[1])} {ord(user_msg[2])}"
      f" {ord(user_msg[3])} {ord(user_msg[4])} {ord(user_msg[5])}")


# Задача 3
## Пользователь вводит строку. Напишите программу, которая заменяет все прописные буквы заглавными, а заглавные - прописными.
## Например: “Съешь ещё этих мягких французских булок, да выпей же чаю” -> “ сЪЕШЬ ЕЩЁ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК, ДА ВЫПЕЙ ЖЕ ЧАЮ ”
print()
print("Пользователь вводит строку. Напишите программу, которая заменяет все прописные буквы заглавными, а заглавные - прописными.")
print()
user_msg = input("Введите сообщение: ")
print(f"Заменяем все прописные буквы заглавными, а заглавные - прописными: {user_msg.swapcase()}")
