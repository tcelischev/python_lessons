from random import randint
import copy

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

input("Press [enter] for next task")
print("\n==========")
print("Задача-2: List 1 deletion from 2")
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
#============================================

num = int(randint(10, 30))
print('Lengh of lits: ' + str(num))
a = [1, 2] #чтобы гарантировано было 2 элемента для удаления
b = [1, 2]
for i in range(num):
    a.append(randint(1, 12))
    b.append(randint(1, 12))

print('List a = ', end=' ')
for i in range(num):
    print('{0:3d}|'.format(a[i]), end='')

print('\nList b = ', end=' ')
for i in range(num):
    print('{0:3d}|'.format(b[i]), end='')

print('\nList a (unique elements) = ', end=' ')
bset = set(b)
c = [item for item in a if item not in bset]
print(c)

# не смог понять почему иногда количество элементов в с() размножается -> [3, 3, 3] хотя в a() цифра 3 была одна.

input("Press [enter] for next task")

print("\n==========")
print("Задача-3: /4, *2")
# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
# =====================================
num = int(randint(1, 50))
print('Lengh of lits: ' + str(num))
a = [4] #для гарантии, что будет хоть один четный элемент
for i in range(num):
    a.append(randint(1, 12))

#b = a.copy()
print('List a (old) = ', end=' ')
for i in range(num):
    print('{0:>3}|'.format(a[i]), end='')

print('\nList a (new) = ', end=' ')
for i in range(num):
    if a[i] % 2 == 0:
        a[i] /= 4
    else:
        a[i] *= 2
    print('{0:>3}|'.format(a[i]), end='')
