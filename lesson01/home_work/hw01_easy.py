__author__ = 'Целищев Александр Сергеевич'
print('\nAuthor: ',__author__ )
print("\n==========")
print("Задача-1: \nДано произвольное целое число (число заранее неизвестно).")
print("Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).")
print("Подсказки:")
print("* постарайтесь решить задачу с применением арифметики и цикла while;")
print("* при желании решите задачу с применением цикла for.")
print("==========\n")

#1st
try:
    num = int(input("Write your random integer number:"))
except:
    print("Вы ввели не число.")

a = str(num)
z = len(a)
x = 0
while x < z:
    print(a[x], end='')
    x += 1
    if x % 3 == 0 and x != z:
        print('.', end='')
    
# без "end=''" получится некрасивый, но правильный ответ на задачу.
print("\n\n")
input("Press [enter] for next task")

print("\n==========")
print("Задача-2: \nИсходные значения двух переменных запросить у пользователя.")
print("Поменять значения переменных местами. Вывести новые значения на экран.")
print("Подсказка:")
print(" * постарайтесь сделать решение через дополнительную переменную") 
print("  или через арифметические действия")
print(" Не нужно решать задачу так:")
print(" print(\"a = \", b, \"b = \", a) - это неправильное решение!")
print("==========\n")

print("Hi, user!")
#чтобы поменять 122 и Вася преобразую явно к строке
a = str(input("Write your 1st thought:"))
b = str(input("Write your 2st thought:"))
c = a
a = b
b = c
print("Теперь всё наоборот:", a + ' ' + b)
print("\n\n")
input("Press [enter] for next task")


print("\n==========")
print("Задача-3: \nЗапросите у пользователя его возраст.")
print("Если ему есть 18 лет, выведите: \"Доступ разрешен\",")
print("иначе \"Извините, пользование данным ресурсом только с 18 лет\"")
print("==========")

print("Hi, User!")
i=0
while i != 1:
    age = int(input("Write your age: "))
    if 18 <= age <= 100:
        print("Access granted.")
        i=1
    elif 0 < age < 18:
        print("Access deny, 18+ only.")
        i=1
    else:
        print("Please, input correct age.")

#ломается если ввести не число. пока не знаю как обработать  :)
