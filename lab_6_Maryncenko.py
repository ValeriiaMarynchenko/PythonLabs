day: int = (int(input("Enter a Day: ")))
month = (int(input("Enter a Month: ")))
year = (int(input("Enter a Year: ")))
month30: tuple[int, int, int, int] = (4, 6, 9, 11)
month31: tuple[int, int, int, int, int, int, int] = (1, 3, 5, 7, 8, 10, 12)

def day_of_year(year, month, day):
    if 1 <= day <= 31:
        if days_in_month(day, month) != True:
            pass
        else:
            return day_of_year(year, month, day)
    else:
        return None


# noinspection PyUnreachableCode
def days_in_month(day, month):
    if month in month30:
        if day <= 30:
            return day
        else:
            return
    else:
        return
    if month in month31:
        if day <= 31:
            return day
        else:
            return
    else:
        return
    if month == 2:
        if day <= 29:
            if is_year_leap(year) == True:
                day <= 29
                return day
            else:
                day <= 28
                return day
        else:
            return
def is_year_leap(year):
    year1 = year % 4
    year2 = year % 100
    year3 = year % 400

    if year1 == 0:
        if year2 == 0 & year3 != 0:
            return False
        else:
            return True
    else:
        return False



print(day_of_year(2000, 12, 31))
