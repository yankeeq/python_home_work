arr = []
n = int(input("Введите количество элементов: "))
for i in range(0, n):
    ele = int(input())
    if ele % 2 == 0 and ele % 3 == 0:
        arr.append(ele)
a = sum(arr) / n
print(a)