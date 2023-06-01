year = int(input('Введите год: '))
def is_year_leap(year):
    if(year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("Год високосный.")
    else:
        print("год не високосный.")
is_year_leap(year)