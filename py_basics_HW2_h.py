# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y

pos_y = equation.find('y')
pos_x = equation.find('x')
pos_eq = equation.find('=')
pos_add = equation.find('+')
print(pos_y, pos_x, pos_eq, pos_add)

k = float(equation[pos_eq+1:pos_x]) # определяем k, срезом от х и до знака равенства, преобразуем во float
b = float(equation[pos_add+1:]) # определяем b, срезом от знака "+" до конца строки, преобразуем во float
y = k * x + b
print(y)
print('\n')



# # Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# # Проверить, корректно ли введена дата.
# # Условия корректности:
# # 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
# #  (в зависимости от месяца, февраль не учитываем)
# # 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# # 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# # 4. Длина исходной строки для частей должна быть в соответствии с форматом
# #  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)
#
# # Пример корректной даты
# date = '01.11.1985'
#
# # Примеры некорректных дат
# date = '01.22.1001'
# date = '1.12.1001'
# date = '-2.10.3001'
#
# я сделал все это в normal
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
    
print('\n')


# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3


import math
piramid_top = []

flat_num = int(input('введите номер квартиры:\n'))
i = 0
block = 1
flats_ = 0
prev_f = 0

while flats_ < flat_num:

    flats_ = block ** 2 + flats_
    l = [z for z in range(prev_f+1, flats_ +1)]
    i += 1
    prev_f = flats_
    block = i + 1
    piramid_top = l[:]
# room position in top row
flat_idx = piramid_top.index(flat_num) +1

k = int(math.sqrt(len(piramid_top)))
n = len(piramid_top)
# room position on the floor
room_position = k if flat_idx % k == 0 else flat_idx % k

fl = 0
for iz in range(0, k):
    fl = fl + iz
# room's floor
floor = fl + k - (n - flat_idx) // k

print('этаж ', floor,'-ый')
print('комната', room_position,'-ая слева')

# коряво конечно, но считает правильно))
