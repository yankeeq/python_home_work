# Строки
some_str = 'hello world'
print(len(some_str))
print(some_str[-1])
print(some_str[::-1])
print(some_str)

for letter in some_str:
    print(letter)

for ind in range(0, len(some_str)):
    print(ind)

print(some_str.index('h'))

some_str[1] = 'l'
print(some_str)


some_list = [1, 'g', True, 1213.2121, [1, 2, 3], True]
print(some_list[0:])
some_list[0] = 2
print(some_list)
some_list.append(10)
print(some_list)
some_list.insert(2, False)
print(some_list)
some_list.pop(-1)
print(some_list)
# some_list.remove(True)
# print(some_list)
for element in some_list:
    if element == True:
        some_list.remove(True)
print(some_list)

n = int(input('Введите кол-во элементов: '))
some_list = []
for _ in range(n):
    some_list.append(int(input()))
print(some_list)

some_list = [1, 2, 3, 4, 5, 6]

for element in some_list:
    print(element)

count = 0
for ind in range(1, len(some_list)):
    if some_list[ind] > some_list[ind - 1]:
        count += 1
print(count)

# Задача 1. Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

n = int(input('Введите кол-во элементов: '))
list_1 = []
for _ in range(n):
    list_1.append(int(input('Введите значения: ')))
print(list_1)

list_2 = []

for elem in list_1:
    if elem not in list_2:
        list_2.append(elem)

print(len(list_2))



# Задача 2. Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

n = int(input('Введите кол-во элементов: '))
list_1 = []
for _ in range(n):
    list_1.append(int(input('Введите значения: ')))
print(list_1)

k = int(input('Введите число K: '))

for i in range(k-1):
    list_1.insert(0,list_1[-1])
    list_1.pop(-1)
print(list_1)

# другой вариант
n = int(input('Введите кол-во элементов: '))
k = int(input('Число '))
s = []
for iu in range(n):
    s.append(int(input()))
print(s)
x = s[:k]
y = s[k:]
z = y + x
print(z) 

# Задача 3. Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3, 8, 4]
# Output: 2 (-1 < 5, 2 < 3)

n = int(input('Введите кол-во элементов: '))
list_1 = []
for _ in range(n):
    list_1.append(int(input('Введите значения: ')))
print(list_1)

count = 0
for i in range(1, len(list_1)):
    if list_1[i] > list_1[i - 1]:
        count += 1
print(count)


# Задача 4. Создайте список из случайных чисел. Найдите номер его последнего локального максимума
# (локальный максимум — это элемент, который больше любого из своих соседей).
# [0, -1, 5, 2, 3, (8), 4]

n = int(input('Введите кол-во элементов: '))
list_1 = []
for _ in range(n):
    list_1.append(int(input('Введите значения: ')))
print(list_1)

indexMax = 0
for i in range(1, len(list_1)):
    if list_1[i  - 1]< list_1[i] > list_1[i + 1]:
        indexMax = i + 1
print(indexMax)