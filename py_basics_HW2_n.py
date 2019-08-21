import random
import math

# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

a = [(random.randint(-1000, 1000)) for i in range(0, 20)]
# a = [2, -5, 8, 9, -25, 25, 4] #
b = []
print(a)

for i in a:
    if i >= 0 and (math.sqrt(i) - int(math.sqrt(i)) == 0):
        b.append(int(math.sqrt(i)))

print(b)
print('\n')
#


# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

days = {1: 'первое', 2: 'второе', 3: 'третье', 4:'четвертое', 5: 'пятое',
        6: 'шестое', 7: 'седьмое', 8:'восьмое', 9: 'девятое', 10: 'десятое',
        11: 'одинадцатое', 12: 'двенадцатое', 13: 'тринадцатое', 14: 'четырнвдцатое',
        15: 'пятнадцатое', 16: 'шеснадцатое', 17: 'семнадцатое', 18: 'восемнадцатое',
        19: 'дквятнадцатое', 20: 'двадцатое', 30: 'тридцатое', 21: 'двадцать', 31: 'тридцать первое' }
months = {1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля', 5: 'мая',
         6:'июня', 7:'июля', 8: 'августа', 9: 'сентября', 10: 'октября',
         11: 'ноября', 12: 'декабря'}

years = 'года'

date = input('введите дату в формате dd.mm.yyyy:\n')
sep = '.'

if date[2] != sep or date[5] != sep:
    print('введите корректную дату!\nвведите корректный разделитель!\nиспользуйте точку!')
else:
    day, month, year = int(date[:2]), int(date[3:5]), int(date[6:])
    #print(day, month, year)

    # для дней с 31-им днем
    if month in (1, 3, 5, 7, 8, 10, 12):
        month1 = months[month]
        if day in range(1, 21) or day == 30 or day == 31:
            day1 = days[day]
        elif day in range (21, 30):
            day1 = days[21] + ' ' + days[(int(day) - 20)]
        else:
            print('введите корректную дату!')
    # для дней с 30-ю днями
    elif month in (4, 6, 9, 11):
        month1 = months[month]
        if day in range(1, 21) or day == 30:
            day1 = days[day]
        elif day in range (21, 30):
            day1 = days[21] + ' ' + days[(int(day) - 20)]
        else:
            print('введите корректную дату!')

    # февраль, просто февраль
    elif month == 2: # високосный год
        month1 = months[month]
        if year % 4 == 0:
            if day in range(1, 21):
                day1 = days[day]
            elif day in range(21, 30):
                day1 = days[21] + ' ' + days[(int(day) - 20)]
        elif year:
            if day in range(1, 21):
                day1 = days[day]
            elif day in range(21, 29):
                day1 = days[21] + ' ' + days[(int(day) - 20)]
        else:
            print('введите корректную дату!')


    if month not in range (1, 13):
        print('введите корректную дату!')

    if year in range(0, 10000):
        year1 = year
    elif year < 0:
        year1 = str(abs(year))+' '+'A.D.' # до нашей эры))
    else:
        print('введите корректную дату!')

    print(day1, month1, year1, years)





# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
# желательно вводить число в диапазоне 15..40, т.к. список используется в задании ниже
num = int(input('введите целое число n:\n'))
a = [(random.randint(-100, 100)) for i in range(0, num)]
print(f'list "a":\n{a}')
#print('\n')


# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]


# возьмем готовый список "a" из задачи №3, выше, чтобы не выдумывать новый

lst2 = list(set(a)) # значения

print(f'values in list "a"":\n{lst2}')
for i in lst2:
    counter = a.count(i)
    if counter != 1:
        lst2.remove(i)

print(f'unique values in list "a":\n{lst2}') # не повторяющиеся значения





