# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
"""
num = int(input('Введите число: '))

i = 1
total = 1
while i <= num:
    total *= i
    i += 1

print(total)
"""

#Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
"""
num = int(input('Введите число: '))

num_one = 0
num_two = 1
num_three = num_one + num_two
count = 3
while num_three < num:
    num_one = num_two
    num_two = num_three
    num_three = num_one + num_two
    count += 1
if num_three == num:
    print(count)
else:
    print(-1)
"""
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел. Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50


"""
num_day = int(input('Введите колличество дней: '))

max_count = 0
old_temperature = 0
temp_count = 0

for _ in range(num_day):
    temperature = int(input('Введите температуру: '))
    if temperature >= 0:
        temp_count += 1
    else:
        if temp_count > max_count:
            max_count = temp_count
        temp_count = 0
    if temp_count > max_count:
        max_count = temp_count
print(max_count)
"""
"""
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза

watermelons = int(input('Введите кол-во арбузов: '))

max_kg = int(input('Введите массу арбуза: '))
min_kg = max_kg
for _ in range(watermelons - 1):
    weight = int(input('Введите массу арбуза: '))
    if weight > max_kg:
        max_kg = weight
    else:
        if weight < min_kg:
            min_kg = weight
print(f'Для себя любимого - {max_kg}, для любимой тещи - {min_kg}')
"""