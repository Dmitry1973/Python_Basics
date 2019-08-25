# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

# методом разностей фибоначей
def fibonacci(n, m):
    fibn1 = fibn2 = fibm1 = fibm2 = 1
    while n > 0:
        fibn1, fibn2 = fibn2, fibn1 + fibn2
        n -= 1
    while m > 0:
        fibm1, fibm2 = fibm2, fibm1 + fibm2
        m -= 1
        
    return print(abs(fibm2 - fibn2))

fibonacci(12, 10)

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    for i in range(len(origin_list), 0, -1):
        for j in range(1, i):
            if origin_list[j - 1] > origin_list[j]:
                origin_list[j - 1], origin_list[j] = origin_list[j], origin_list[j - 1]
    return print(origin_list)


sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
def para(x1,y1,x2,y2,x3,y3,x4,y4):
    if y1 == y4 and y2 == y3 and abs(x1 - x2) == abs(x3 - x4):
        return print('Is Parallelogramm')
    else:
        return print('Not a Perallellogramm')
