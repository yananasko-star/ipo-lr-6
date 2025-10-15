import random
from itertools import combinations

# Создаём случайный список из 20 значений
numbers = [random.randint(-10, 10) for _ in range(20)]

# Находим все уникальные комбинации из 4 чисел
unique_combinations = set()
for comb in combinations(numbers, 4):
    unique_combinations.add(tuple(sorted(comb)))

# Пользователь вводит число
n = int(input("Введите целое число: "))

# Считаем пары с суммой меньше n
count = 0
for comb in unique_combinations:
    if sum(comb) < n:
        count += 1

# Выводим результаты
print("Список чисел:", numbers)
print("Уникальные комбинации:")
for comb in unique_combinations:
    print(comb)
print(f"Количество пар с суммой меньше {n}: {count}")