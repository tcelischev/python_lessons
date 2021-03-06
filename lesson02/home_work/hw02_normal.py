from random import randint
import datetime

__author__ = 'Целищев Александр Сергеевич'
print('\nAuthor: ',__author__ )
print("\n==========")
print(" Задача-1:")
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]
# ====================================
print('Задача №1. sqrt')

num = int(randint(10, 30))
a = [25]
for i in range(num):
    a.append(randint(-100, 100))

print('List a = ', end=' ')
for i in range(num):
    print('{0:3d}|'.format(a[i]), end='')

b = []
for i in range(num):
    if a[i]>= 0 and (a[i]**0.5) % 1 == 0:
        b.append(a[i])

print('')
print('List a (sqrt) = ', end=' ')
for i in range(len(b)):
    print('{0:3d}|'.format(b[i]), end='')

input("\nPress [enter] for next task")

print("\n==========")
print(" Задача-2: date in text")
# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)
# ===================================
currentdate = str(datetime.date.today())
print('Current date = ' + currentdate)
#now = currentdate.strftime("%d %B %Y")
date_separated = list(currentdate.split('-'))
print(date_separated)

dayz = ['первое', 'второе', 'третье', 'четвёртое',
        'пятое', 'шестое', 'седьмое', 'восьмое',
        'девятое', 'десятое', 'одиннадцатое', 'двенадцатое',
        'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое',
        'семнадцатое', 'восемнадцатое', 'девятнадцатое', 'двадцатое',
        'двадцать первое', 'двадцать второе', 'двадцать третье',
        'двадацать четвёртое', 'двадцать пятое', 'двадцать шестое',
        'двадцать седьмое', 'двадцать восьмое', 'двадцать девятое',
        'тридцатое', 'тридцать первое']

monz = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']

print(dayz[int(date_separated[2])-1] + ' ' + monz[int(date_separated[1])-1] + ' ' + date_separated[0] + ' года')


input("Press [enter] for next task")
print("\n==========")
print('Задача-3: Randomizer (-100:100)')
# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
try:
    num = int(input("Write quantity of random element:"))
except:
    print("Input correct integer number.")

a = []
for i in range(num):
    a.append(randint(-100, 100))
    print(a[i], end='|')

print('\n')
input("Press [enter] for next task")

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]
# ======================================
print('Задача №4')

num = int(randint(10, 30))
a = []
for i in range(num):
    a.append(randint(1, 12))

print('List a = ', end=' ')
for i in range(num):
    print('{0:3d}|'.format(a[i]), end='')

u = []
notu = []
for i in range(num):
    if a.count(a[i]) == 1:
        u.append(a[i])
    else:
        notu.append(a[i])

print('')
print('unique in a = ', end=' ')
for index, value in enumerate(u):
    print('{0:3d}|'.format(value), end='')

print('\nNot unique in a = ', end=' ')
for index, value in enumerate(notu):
    print('{0:3d}|'.format(value), end='')

input("\nPress [enter] for next end")