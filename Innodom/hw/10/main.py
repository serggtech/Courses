import csv

count_passenger = 0

count_survived = 0
count_no_survived = 0

count_survived_male = 0
count_survived_female = 0
count_survived_child = 0

count_male_all = 0
count_male_child = 0
count_male = 0

count_female_all = 0
count_female_child = 0
count_female = 0

count_child = 0


with open("titanic.csv", "r", newline="") as csv_file:
    read_data = csv.DictReader(csv_file)
    for row in read_data:
        print(row)

        if row["Survived"] == "1":
            count_survived += 1
        else:
            count_no_survived += 1

        count_male_all
        if row["Sex"] == "male" and row["Age"] >= "15":
            count_male += 1
        if row["Sex"] == "male" and row["Age"] <= "15":
            count_male_child += 1

        if row["Sex"] == "female" and row["Age"] >= "15":
            count_female += 1
        if row["Sex"] == "female" and row["Age"] <= "15":
            count_female_child += 1
        #
        # if row["Sex"] == "female":
        #     count_female += 1
print()
print(f"count_all_survived: {count_survived}")
print()
print(
    f"count_male_all: {count_male_all}, count_male: {count_male}, count_male_child: {count_male_child}"
)
print()
print(f"count_female: {count_female}, count_female_child: {count_female_child}")
print(count_male + count_male_child + count_female + count_female_child)

print(type(read_data))
print()
print(read_data)