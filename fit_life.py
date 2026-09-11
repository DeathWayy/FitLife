# Первые две строки подсказал ии
import sys

sys.stdout.reconfigure(encoding="utf-8")
# Проект FitLife - MVP версия 1.0


print("Здравствуйте! Я бот FitLife")
print("Помогаю рассчитать ИМТ тела и норму воды в день.\n")

user_name = input("Для начала давайте знакомиться. Как вас зовут?: ")

print(f"Очень приятно {user_name}\n")

# Маленькая проверка чтоб вводили числа а не текст и сбор данных
try:
    user_age = int(input("Сколько вам лет?: "))
except ValueError:
    user_age = int(input("Укажите корректный возраст: "))

try:
    user_weight = float(input("Ваш вес?(Вес указывайте в кг. Пример: 97): "))
except ValueError:
    user_weight = float(input("Укажите корректный вес: "))

try:
    user_height = float(input("Ваш рост?(В метрах). Пример 1.78: "))
except ValueError:
    user_height = float(input("Введите корректный рост: "))


# Расчет имт(bmi) и нормы воды(water_ml) с преобразованием в литры(water_l)
WATER_PER_KG = 30
bmi = user_weight / (user_height ** 2)
water_ml = user_weight * WATER_PER_KG

bmi = round(bmi, 1)
water_l = round(water_ml / 1000, 1)
# Отчет ИМТ и нормы воды
print(f"\nОтчет для пользователя: {user_name}. Возраст: {user_age} г.")
print(f"Ваш индекс массы тела: {bmi}")
print(f"Рекомендуемая норма воды в день: {water_l} л. в день\n\n")
print("Расчет окончен! Будьте здоровы!")

# Использовал ии чтобы немного поправить грамматику
# Так же bmi забыл округлить и ии подсказал
