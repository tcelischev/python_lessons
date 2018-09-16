# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

print('# Задание-1: Fibonachi')
def fibonacci(n, m):
    fib = [1, 1, ]
    i = 2
    for i in range(2, m):
        a = fib[i-2] + fib[i-1]
        fib.append(a)
    return fib[n-1:m]

print(fibonacci(1,18))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()
print('\n# Задача-2: bubleSort')

def sort_to_max(origin_list):
        sl = origin_list
        n = 1
        while n < len(sl):
            for i in range(len(sl) - n):
                if sl[i] > sl[i + 1]: sl[i], sl[i + 1] = sl[i + 1], sl[i]
            n += 1
        print(sl)

bb = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
print(bb)
sort_to_max(bb)


# Задача 2 (альтернативная):
# Напишите пожалуйста программу, которая открыват файл на запись, записывает туда N случайных чисел от -100 до 100
# после этого, закрывает файл.
# открывает файл снова для чтения, читает оттуда числа, и все числа, которые больше 0 записывает в новый файл.

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
#==== сделаю позже +++++++.

i = ['1' , '2' , '3' , '4']

def my_filter(what, where):
    new = [string for string in where if what(where)]
    return new

def superfunc(*args):
    return args % 2 == 0

print(my_filter(superfunc,i))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
# ===========================
# Задача-4: Alt
# Напишите функцию, которая считает сумму квадратов от своих аргументов.
# Кол-во аргументов функции может быть любым.
# =================

print('\n# Задача-4: / /')

dots = [[0, 0], [10, 20], [40, 0], [56, 26]]
print(dots)
dotsx = []
dotsy = []

for i in range(len(dots)):
    dotsx.append(dots[i][0])
    dotsy.append(dots[i][1])

print(dotsx)
print(dotsy)

cntx = 1
n=2  #количество сравнений отрезков между собой
while cntx in range(n):
    for i in range(n):
        if abs(dotsx[cntx] - dotsx[cntx+1]) == abs(dotsx[i+1] - dotsx[i+2]):
            cntx +=1
            if cntx == 2:  #должно быть 2 равных отрезка для условия параллелограмма
                break
    n -= 1

cnty = 1

while cnty in range(n):
    for i in range(n):
        if abs(dotsy[cnty] - dotsy[cnty+1]) == abs(dotsy[i+1] - dotsy[i+2]):
            cnty +=1
            if cnty == 2: break
    n -=1

if cntx == 2 and cnty == 2:
    print('Это параллелограмм')
else: print('Не могу распознать фигуру')




