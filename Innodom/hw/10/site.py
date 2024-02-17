# Задача 1

# Из приложенного к уроку json-файла, заберите данные и переместите их в таблицу csv, в удобном для вас виде.

import json
import csv

# /content/films.json

# Открываем JSON-файл и загружаем данные
with open("films.json") as json_file:
    data = json.load(json_file)

print(data)
for i in data:
    print(i["name"])

# # Открываем CSV-файл для записи
# with open("data.csv", "w", newline="") as csv_file:
#     # Создаем объект writer для записи в CSV
#     writer = csv.writer(csv_file)
#
#     # Записываем заголовки в CSV-файл
#     writer.writerow(data[0].keys())
#
#     # Записываем данные в CSV-файл
#     for item in data:
#         writer.writerow(item.values())
#
# print("Преобразование JSON в CSV завершено.")
