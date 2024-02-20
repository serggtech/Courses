stack = []  # Создаем пустой стек

# Ввод чисел пользователем и добавление их в стек
while True:
    try:
        num = int(input("Введите целое число (для завершения введите любую букву): "))
        stack.append(num)
    except ValueError:
        break

# Вывод содержимого стека на экран
print("Содержимое стека:")
for num in reversed(stack):
    print(num)
