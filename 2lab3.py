'''функция, которая определяет, является ли год с данным номером високосным
Если год является високосным, то выведите «Год ...(год) - високосный»
иначе выведите «Это год не високосный».'''

year = int(input())
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('год', year, '- високосный')
else:
    print(year, '- это обычный год')