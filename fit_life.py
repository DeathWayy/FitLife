# Первые две строки подсказал ии
import sys

sys.stdout.reconfigure(encoding="utf-8")
# Проект FitLife - MVP версия 2.0


print("Здравствуйте! Я бот FitLife")
print("Помогаю рассчитать ИМТ тела и норму воды в день.\n")

# Проверка имени на пустую строку
user_name = input("Для начала давайте знакомиться. Как вас зовут?: ")
while not user_name.strip().lower():
    user_name = input("Не оставляйте строку пустой! Введите имя: ")

print(f"Очень приятно {user_name}\n")

# Проверка чтоб вводили числа а не текст и сбор данных
while True:
    try:
        user_age = int(input("Сколько вам лет?: "))
        break
    except ValueError:
        print("Введите возраст еще раз")

while True:
    try:
        user_weight = float(input("Ваш вес?(Указывайте в кг. Пример: 97): "))
        break
    except ValueError:
        print("Введите вес еще раз")

while True:
    try:
        user_height = float(input("Ваш рост?(В метрах). Пример 1.78: "))
        break
    except ValueError:
        print("Введите возраст еще раз")

# Проверка на год, года и лет
age_suffix = ""

if 11 <= user_age % 100 <= 14:
    age_suffix = "лет"
elif user_age % 10 == 1:
    age_suffix = "год"
elif user_age % 10 in (2, 3, 4):
    age_suffix = "года"
else:
    age_suffix = "лет"

# Расчет имт(bmi) и нормы воды(water_l)
WATER_PER_KG = 30
bmi = round(user_weight / (user_height ** 2), 1)
water_l = round(user_weight * WATER_PER_KG / 1000, 1)

bmi = round(bmi, 1)

bmi_suffix = ""

# Проверка индекса массы тела(ИМТ)
if bmi < 16:
    bmi_suffix = "у вас выраженный дефицит массы тела."
elif bmi >= 16 and bmi <= 18.5:
    bmi_suffix = "у вас недостаточная масса тела."
elif bmi > 18.5 and bmi <= 25:
    bmi_suffix = "у вас нормальная масса тела."
elif bmi > 25 and bmi <= 30:
    bmi_suffix = "у вас избыточная масса тела(Предожирение)"
elif bmi > 30 and bmi <= 35:
    bmi_suffix = "у вас ожирение 1 степени"
elif bmi > 35 and bmi <= 40:
    bmi_suffix = "у вас ожирение 2 степени"
else:
    bmi_suffix = "у вас ожирение 3 степени"

# Отчет ИМТ и нормы воды
print(f"\nОтчет для пользователя: {user_name}.", end=" ")
print(f"Возраст: {user_age} {age_suffix}")
print(f"Ваш индекс массы тела: {bmi}, {bmi_suffix}")
print(f"Рекомендуемая норма воды в день: {water_l} л. в день\n\n")
print("Расчет окончен! Будьте здоровы!")

# Во второй версии использовал ии для
# проверка возраста, помощи и роста
# проверка год, года и лет
# старался чтоб ии давал подсказку
# а я дописывал
