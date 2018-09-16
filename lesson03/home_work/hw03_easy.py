
# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.
# =====================================
print('\n Задача №1')

def my_round(number, ndigits):
    strnum = str(number)
    leftpart, _, rightpart = strnum.partition(".")
    if (rightpart[ndigits] >= '5'):
        num = (int(strnum(:int(ndigits)+2)) * 10**ndigits + 1)/10**ndigits
     #  rightpart_new = int(rightpart[0:ndigits-1]) + 1
    elif (rightpart[ndigits] >= '0'):
        rightpart_new = int(rightpart[0:ndigits-1])
        num = leftpart + '.' + str(rightpart_new)
    else:
        pass
    return
    num


print(my_round(2.1234517, 5))
print(my_round(2.1999957, 5))
print(my_round(2.9999957, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить
# =====================================
print('\n Задача №2')

def lucky_ticket(ticket_number):
    b = list(map(int, str(ticket_number)))
    if (len(b) == 6 and (sum(b[:3]) == sum(b[-3:]))):
        d = str(ticket_number) + ':  Щастье есть'
    else:
        d = str(ticket_number) + ':  Счастье близко'
    return d


print(lucky_ticket(123006))
print(lucky_ticket(123000))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
