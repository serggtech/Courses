import csv

fileInput = "filterpress1.cfg"
file = open(fileInput, "r", encoding="utf-8-sig", errors="ignore")
string_search = "RACK"
list_find = []
list_find_list = []

for row in file:
    try:
        if string_search in row:
            row_new = row.rstrip("\n").replace('"', "")
            list_find.append(row_new)
            # print(row)
            # print(row_new)

    except UnicodeDecodeError:
        file.close()
        print("err")

file.close()

for x in list_find:
    # print(x)
    list_find_list.append([x])
    # print(list_find_list[x])


print(list_find_list)
# print(len(list_find[0].split(',')))
# print(len(list_find[1].split(',')))
# print(len(list_find))

# print("err11111")

with open("output.csv", "w", newline="\n") as file:
    # Создание объекта записи CSV
    writer = csv.writer(file)

    # Запись данных в CSV-файл
    for row in list_find_list:
        writer.writerow(row)
