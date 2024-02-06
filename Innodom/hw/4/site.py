# Задача 1
# Врач рекомендовал пациенту не принимать пищу в период с 18.00 до 9.00. # Напишите калькулятор,
# который считает, через сколько часов пациенту можно есть. Если есть можно, выведите сообщение - можно есть,
# если есть нельзя, то напишите, через сколько можно. # Пример: # # 16.00 # Можно есть # 20.00 # Можно есть через 13
# часов.

time_dont_eat_hour_start = 9.00
time_dont_eat_hour_end = 18.00

current_time = input("Введите время в формате '00.00' : ")
current_time = float(current_time)
if time_dont_eat_hour_start <= current_time < time_dont_eat_hour_end:
    print("Можно есть")
elif current_time < time_dont_eat_hour_start:
    hours_to_eat = time_dont_eat_hour_start - current_time
    print(f"Можно есть через {hours_to_eat} часов.")
else:
    hours_to_eat = 24.00 - current_time + time_dont_eat_hour_start
    print(f"Можно есть через {hours_to_eat} часов.")


# Задача 2
# Напишите программу, которая выводит, какой сейчас месяц по числовой дате.
# Например:
# 11.11.2000 -> Ноябрь
print()

# """
# 1 — январь (первый месяц по счету январь)
# 2 — февраль (второй месяц по счету февраль)
# 3 — март (третий месяц по счету март)
# 4 — апрель (четвертый месяц по счету апрель)
# 5 — май (пятый месяц по счету май)
# 6 — июнь (шестой месяц по счету июнь)
# 7 — июль (седьмой месяц по счету июль)
# 8 — август (восьмой месяц по счету август)
# 9 — сентябрь (девятый месяц по счету сентябрь)
# 10 — октябрь (десятый месяц по счету октябрь)
# 11 — ноябрь (одиннадцатый месяц по счету ноябрь)
# 12 — декабрь (двенадцатый месяц по счету декабрь)
# """

time_now_data = input("Введите дату в формате '11.11.2000': ")
time_now_data_str = str(time_now_data).split(".")
time_now_data_int = int(time_now_data_str[1])

if time_now_data_int == 1:
    print(f"{time_now_data} -> Январь")

elif time_now_data_int == 2:
    print(f"{time_now_data} -> Февраль")

elif time_now_data_int == 3:
    print(f"{time_now_data} -> Март")

elif time_now_data_int == 4:
    print(f"{time_now_data} -> Апрель")

elif time_now_data_int == 5:
    print(f"{time_now_data} -> Май")

elif time_now_data_int == 6:
    print(f"{time_now_data} -> Июнь")

elif time_now_data_int == 7:
    print(f"{time_now_data} -> Июль")

elif time_now_data_int == 8:
    print(f"{time_now_data} -> Август")

elif time_now_data_int == 9:
    print(f"{time_now_data} -> Сентябрь")

elif time_now_data_int == 10:
    print(f"{time_now_data} -> Октябрь")

elif time_now_data_int == 11:
    print(f"{time_now_data} -> Ноябрь")

elif time_now_data_int == 12:
    print(f"{time_now_data} -> Декабрь")

# """
# match time_now_data_int:
#     case 1:
#         print(f"{time_now_data} -> Январь")
#     case 2:
#         print(f"{time_now_data} -> Февраль")
#     case 3:
#         print(f"{time_now_data} -> Март")
#     case 4:
#         print(f"{time_now_data} -> Апрель")
#     case 5:
#         print(f"{time_now_data} -> Май")
#     case 6:
#         print(f"{time_now_data} -> Июнь")
#     case 7:
#         print(f"{time_now_data} -> Июль")
#     case 8:
#         print(f"{time_now_data} -> Август")
#     case 9:
#         print(f"{time_now_data} -> Сентябрь")
#     case 10:
#         print(f"{time_now_data} -> Октябрь")
#     case 11:
#         print(f"{time_now_data} -> Ноябрь")
#     case 12:
#         print(f"{time_now_data} -> Декабрь")
# """
