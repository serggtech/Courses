# Задача 1
# Каждый 16 день от начала года Маша заказывает суши.
# Помогите посчитать, сколько дней в году Маша заказывает суши. Учтите, что в году не всегда 365 дней.
days_count = input("Введите количество дней в году: ")
days_period_sushi = 16
result = int(days_count) / days_period_sushi
print(f"сколько дней в году Маша заказывает суши {result}")


# Задача 2
# Есть список [98,67,92,112,68,39,98, 91,74,34,88].
# Найдите среднее арифметическое этих значений.
user_list = [98, 67, 92, 112, 68, 39, 98, 91, 74, 34, 88]
user_list_len = len(user_list)
user_list_sum = sum(user_list)
user_list_average = user_list_sum / user_list_len
print(user_list_average)
