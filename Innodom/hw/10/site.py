# Задача 1

# Из приложенного к уроку json-файла, заберите данные и переместите их в таблицу csv, в удобном для вас виде.

import json
import csv

# Открываем JSON-файл и загружаем данные
with open("films.json") as json_file:
    data = json.load(json_file)


# print(data["films"][0]["evaluations"][0])
# print(data["films"][0]["evaluations"][1])
# print(data["films"][0]["evaluations"][2])
count = 0

field_names = [
    "count",
    "films_name",
    "release",
    "producer",
    "evaluations_name_IMDb",
    "evaluations_result_IMDb",
    "evaluations_name_metacritic",
    "evaluations_result_metacritic",
    "evaluations_name_rottentomatoes",
    "evaluations_result_rottentomatoes",
]

films_list = []
film_dict = {}

for i in data["films"]:
    count += 1
    film_dict = {
        "count": count,
        "films_name": i["name"],
        "release": i["release"],
        "producer": i["producer"],
        "evaluations_name_IMDb": i["evaluations"][0]["name"],
        "evaluations_result_IMDb": i["evaluations"][0]["result"],
        "evaluations_name_metacritic": i["evaluations"][1]["name"],
        "evaluations_result_metacritic": i["evaluations"][1]["result"],
        "evaluations_name_rottentomatoes": i["evaluations"][2]["name"],
        "evaluations_result_rottentomatoes": i["evaluations"][2]["result"],
    }
    films_list.append(film_dict)

# print(films_list)

with open("films.csv", "w") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(films_list)


with open("films.json") as json_file:
    data = json.load(json_file)

IMDb_list = []

for i in data["films"]:
    if float(i["evaluations"][0]["result"]) < 8.5:
        print(i["evaluations"][0]["result"])
        IMDb_list.append(
            [
                i["name"],
                i["release"],
                i["producer"],
                i["evaluations"][0]["name"],
                i["evaluations"][0]["result"],
                i["evaluations"][1]["name"],
                i["evaluations"][1]["result"],
                i["evaluations"][2]["name"],
                i["evaluations"][2]["result"],
            ]
        )


print(IMDb_list)
with open("films.txt", "w") as file:
    file.writelines(str(IMDb_list))  # Запись строки в файл
