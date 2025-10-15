import random

# Создаём список из 25 случайных чисел от -50 до 50
numbers = [random.randint(-50, 50) for _ in range(25)]

# Считаем количество положительных, отрицательных и нулевых
positive = len([x for x in numbers if x > 0])
negative = len([x for x in numbers if x < 0])
zero = len([x for x in numbers if x == 0])

# Вычисляем проценты
total = len(numbers)
p_percent = (positive / total) * 100
n_percent = (negative / total) * 100
z_percent = (zero / total) * 100

# Находим мин и макс
max_val = max(numbers)
min_val = min(numbers)

# Выводим результаты
print("Список:", numbers)
print(f"Положительные: {positive} ({p_percent:.1f}%)")
print(f"Отрицательные: {negative} ({n_percent:.1f}%)")
print(f"Нулевые: {zero} ({z_percent:.1f}%)")
print(f"Максимум: {max_val}")
print(f"Минимум: {min_val}")
