import os

with open("stars.txt", "rb") as file:
    data = file.read()
    print(data)


with open("stars.bin", "wb") as bin_file:
    bin_file.write(data)

os.remove("stars.txt")

with open("stars.bin", "r", encoding="utf-8") as bin_file:
    din_data = bin_file.read()

print()
print(din_data)
