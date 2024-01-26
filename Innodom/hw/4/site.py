# Задача 1
## Врач рекомендовал пациенту не принимать пищу в период с 18.00 до 9.00.
## Напишите калькулятор, который считает, через сколько часов пациенту можно есть. Если есть можно, выведите сообщение - можно есть, если есть нельзя, то напишите, через сколько можно.
## Пример:
##
## 16.00
## Можно есть
## 20.00
## Можно есть через 13 часов.

time_dont_eat_hour = [18, 9]
time_now_eat = input("Введите время в формате '00.00' : ")
time_now_eat = str(time_now_eat).split(".")
time_now_eat_hour = int(time_now_eat[0])


if time_dont_eat_hour[0] > time_now_eat_hour > time_dont_eat_hour[1]:
    print(f"Можно есть через {abs(int(time_now_eat[0])-time_dont_eat_hour[0])} часов")
else:
    print("Можно есть")

# Задача 2
## Напишите программу, которая выводит, какой сейчас месяц по числовой дате.
## Например:
##
## 11.11.2000 -> Ноябрь

time_now_data = input("месяц по числовой дате в формате '11.11.2000': ")
time_now_data_str = str(time_now_data).split(".")
time_now_data_int = int(time_now_data_str[0])

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
12313131231312
