import random

# Создаем матрицу произвольного размера
rows = random.randint(4, 8)
cols = random.randint(4, 8)

values = [-3, -5, -2, -12, 0, 15, 4, 7, 2]

# Создаем матрицу с использованием list comprehension
matrix = [[values[(i * cols + j) % len(values)] for j in range(cols)] for i in range(rows)]

# Выводим матрицу
print(f"Матрица {rows}×{cols}:")
for row in matrix:
    print(' '.join(f"{num:4}" for num in row))

# Считаем сумму отрицательных элементов
negative_sum = sum(num for row in matrix for num in row if num < 0)
print(f"\nСумма отрицательных элементов: {negative_sum}")
