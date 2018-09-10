from random import randint

__author__ = 'Целищев Александр Сергеевич'
print('\nAuthor: ',__author__ )
print("\n==========")
print("Задача-1: Fruits sorting and alignment")
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()
#============================================
fruits = ["яблоко", "банан", "киви", "арбуз"]
print(fruits, end='')
print(' => ')
for ind, value in enumerate(fruits):
    print('{0}. {1:>10}'.format(ind+1, value))

print("\n==========")
print("Задача-2: List 1 deletion from 2")
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
#============================================

num = randint(0, 100)
print(num)
a = []
for i in range(num):
    a.append(randint(-100, 100))

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
