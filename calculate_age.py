from datetime import datetime
'''
Написати функцію, яка буде приймати дату народження та рахувати вік людини
'''

# calculate_persons_age("01-01-2000")
# def calculate_persons_age(birthday_date: datetime):

#"01-01-2000"
#"dd-mm-yyyy"

def calculate_persons_age(birthday_date: str) -> int:
    """ Function that calculate age of a person """
    birthday = datetime.strptime(birthday_date, "%d-%m-%Y").date()
    today = datetime.now().date()
    # print(today - birthday)

    birthday_this_year = birthday.replace(year=today.year)

    year_difference = today.year - birthday.year
    
    if (birthday_this_year > today):
        year_difference -= 1
        # year_difference = year_difference - 1
    return year_difference


print(calculate_persons_age("01-01-2000")) # 24
print(calculate_persons_age("05-10-2024")) # 0
print(calculate_persons_age("07-10-2000")) # 23
