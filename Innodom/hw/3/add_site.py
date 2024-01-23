# Задача
## Переведите любую картинку в ASCII Art с помощью pywhatkit

import pywhatkit

# img_in = input("Введите входное изображение: ")
# img_out = input("Введите выходное изображение: ")
print("Переведите любую картинку в ASCII Art с помощью pywhatkit")
print()
img_in = "in.jpg"
img_out = "out"

print(pywhatkit.image_to_ascii_art(img_in, img_out))
