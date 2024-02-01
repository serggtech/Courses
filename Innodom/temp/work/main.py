import csv

file_name = input("Введите имя файла: ")
# file_name = "x_awas_a7"
file_format = ".cfg"
file_input = file_name + file_format
file = open(file_input, "r", encoding="utf-8-sig", errors="ignore")
string_search = "RACK", "DPSUBSYSTEM", "IOSUBSYSTEM 100"
list_find = [[], [], []]
list_find_rack = []
list_find_dp_system = []
list_find_dp_iosubsystem_100 = []
q = 0
for row in file:
    try:
        if string_search[0] in row:
            row_new = row.rstrip("\n").replace('"', "")
            list_find[0].append(row_new)
            # print(row)
            # print(row_new)
        elif string_search[1] in row:
            row_new = row.rstrip("\n").replace('"', "")
            list_find[1].append(row_new)
            # print(row)
            # print(row_new)
            # q += 1
            # print(q)
        elif string_search[2] in row:
            row_new = row.rstrip("\n").replace('"', "")
            list_find[2].append(row_new)
            # print(row)
            # print(row_new)
            # q += 1
            # print(q)

    except UnicodeDecodeError:
        file.close()
        print("err")

file.close()

# print(list_find)
# print(list_find[0])
# print(list_find[1])

for x in list_find[0]:
    # print(x)
    list_find_rack.append([x])
    # print(list_find_rack[x])


for x in list_find[1]:
    # print(x)
    list_find_dp_system.append([x])
    # print(list_find_rack[x])

for x in list_find[2]:
    # print(x)
    list_find_dp_iosubsystem_100.append([x])
    # print(list_find_rack[x])


print(list_find_rack)
# print(len(list_find[0].split(',')))
# print(len(list_find[1].split(',')))
# print(len(list_find))

# print("err11111")

with open(file_name + "_output.csv", "w", newline="\n") as file:
    # Создание объекта записи CSV
    writer = csv.writer(file)

    # Запись данных в CSV-файл
    for row in list_find_rack:
        writer.writerow(row)

    for row in list_find_dp_system:
        writer.writerow(row)

    for row in list_find_dp_iosubsystem_100:
        writer.writerow(row)
