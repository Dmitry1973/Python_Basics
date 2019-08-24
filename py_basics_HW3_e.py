# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    num = (int(number * 10 ** ndigits)) * 10
    r = int(number * 10 ** ndigits)
    r1 = int(number * (10 ** (ndigits + 1)))
    if r1 - num >= 5:
        rounded = (r + 1)/ 10 ** (ndigits)
    else:
        rounded = r / 10 ** (ndigits)

    return rounded

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 1))
print(my_round(2.12254467, 6))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    word  = str(ticket_number)
    lst = []
    for i in word:
        lst.append(int(i))
    if len(lst) % 2 != 0:
        return 'Try next'
    else:
        half = int(len(lst) / 2)
        h1 = lst[: half]
        h2 = lst[half:]
        if sum(h1) == sum(h2):
            return 'Lucky'
        else:
            return None


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(4365445751))
