# Задача 1
# Создайте переводчик, который переводит слова с русского на английский и наоборот.
# Пользователь вводит слово, нужно перевести его на другой язык.
# Если такого слова не существует в словаре, выведите на экран “нет такого слова”.

Translate_dict = {
    "people": "люди",
    "family": "семья",
    "woman": "женщина",
    "man": "мужчина",
    "girl": "девочка",
    "boy": "мальчик",
    "child": "ребёнок",
    "friend": "друг",
    "husband": "муж",
    "wife": "жена",
    "name": "имя",
    "head": "голова",
    "face": "лицо",
    "hand": "рука",
    "life": "жизнь",
    "hour": "час",
    "week": "неделя",
    "day": "день",
    "night": "ночь",
    "month": "месяц",
    "year": "год",
    "time": "время",
    "world": "мир",
    "sun": "солнце",
    "animal": "животное",
    "tree": "дерево",
    "water": "вода",
    "food": "еда",
    "fire": "огонь",
    "country": "страна",
    "city": "город",
    "street": "улица",
    "work": "работа",
    "school": "школа",
    "shop": "магазин",
    "house": "дом",
    "room": "комната",
    "car": "машина",
    "paper": "бумага",
    "pen": "ручка",
    "door": "дверь",
    "chair": "стул",
    "table": "стол",
    "money": "деньги",
    "way": "путь",
    "end": "конец",
    "price": "цена",
    "question": "вопрос",
    "answer": "ответ",
    "number": "номер.",
}

str_val = input("Введите слово: ")

# print(str_val)
flag_known_word = False
for word_eng, word_rus in Translate_dict.items():
    if str_val == word_eng:
        print(f"Русское слово: {word_rus}")
        flag_known_word = True
        break

    elif str_val == word_rus:
        print(f"Английское слово: {word_eng}")
        flag_known_word = True
        break

if not flag_known_word:
    print("нет такого слова")


# Задача 2
# 1кг творога стоит 5 руб.
# Выведите на экран таблицу стоимости творога массой 100г, 200г, 300г, 600г, 900г

price_per_kg = 5

weights = [100, 200, 300, 600, 900]

print("Масса (г)\t\tСтоимость (руб)")
for weight in weights:
    price = weight / 1000 * price_per_kg
    print(f"{weight}\t\t\t{price}")
