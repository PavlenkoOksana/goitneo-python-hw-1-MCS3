from collections import defaultdict
from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    birthdays_per_week = defaultdict(list)
    today = datetime.today().date()
    # str_names = ""
    
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year: datetime = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year = today.year + 1)
        # # без этого условия, если выполнять программу в понедельник, прошедшие выходные не попадают поле зрения
        # if (today.weekday() == 0 and (birthday_this_year.day-today.day) == -1) or (today.weekday() == 0 and (birthday_this_year.day-today.day) == -2):
        #     if "Monday" not in birthdays_per_week:
        #             birthdays_per_week["Monday"] = [name]         
        #     else:
        #             birthdays_per_week["Monday"].append(name)
        # if birthday_this_year < today:
        #      birthday_this_year=birthday.replace(year=today.year+1)  
        # delta_days = (birthday_this_year - today).days
        if today <= birthday_this_year <= today + timedelta(7) :
            wd = birthday_this_year.weekday()
            if wd in (5, 6):
                birthdays_per_week["Monday"].append(name)
            else:
                birthdays_per_week[birthday_this_year.strftime("%A")].append(name)
            # if birthday_this_year.weekday() == 0 or \
            # (birthday_this_year.weekday() == 5 and delta_days < 5) or \
            #     (birthday_this_year.weekday() == 6 and delta_days < 6):
            #     # не змогла перенести умови умовного оператора на нову строку, для візуального розділення та щоб було виконано рекомендаціЇ PEP 8, видає помилку
            #     if "Monday" not in birthdays_per_week:
            #         birthdays_per_week["Monday"] = [name]         
            #     else:
            #         birthdays_per_week["Monday"].append(name)
            # elif birthday_this_year.weekday() == 1:
            #     if "Tuesday" not in birthdays_per_week:
            #         birthdays_per_week["Tuesday"] = [name]
            #     else:
            #         birthdays_per_week["Tuesday"].append(name)
            # elif birthday_this_year.weekday() == 2:
            #     if "Wednesday" not in birthdays_per_week:
            #         birthdays_per_week["Wednesday"] = [name]
            #     else:
            #         birthdays_per_week["Wednesday"].append(name)
            # elif birthday_this_year.weekday() == 3:
            #     if "Thursday" not in birthdays_per_week:
            #         birthdays_per_week["Thursday"] = [name]
            #     else:
            #         birthdays_per_week["Thursday"].append(name)          
            # elif birthday_this_year.weekday() == 4:
            #     if "Friday" not in birthdays_per_week:
            #         birthdays_per_week["Friday"] = [name]
            #     else:
            #         birthdays_per_week["Friday"].append(name)   
    for weekday, user  in birthdays_per_week.items():
        # for i in range(len(birthdays_per_week[key])):
        #     str_names = str_names + birthdays_per_week[key][i] + ", "
        print("\033[36m{}".format(weekday)+"\033[30m{}".format(": " + ", ".join(user)))
        # str_names = ""     


if __name__ == "__main__":      

    get_birthdays_per_week([{"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
        {"name": "Taras Svhevchenko", "birthday": datetime(1970, 10, 9)},
        {"name": "Lesja Ukrainka", "birthday": datetime(1971, 10, 10)},
        {"name": "Ivan Gates", "birthday": datetime(1955, 10, 10)},
        {"name": "Star Pol", "birthday": datetime(1900, 10, 11)},
        {"name": "Elvis Presly", "birthday": datetime(1912, 10, 12)},
        {"name": "Ben Cambr", "birthday": datetime(1913, 10, 13)},
        {"name": "Bill Gates1", "birthday": datetime(1955, 12, 11)},
        {"name": "Bill Gates2", "birthday": datetime(1955, 3, 3)},
        {"name": "Bill Gates3", "birthday": datetime(1944, 5, 20)},
        {"name": "Volodimir Zelensky", "birthday": datetime(1979, 10, 7)},
        {"name": "Alla Mazur", "birthday": datetime(1999, 10, 8)},
        {"name": "Name 11111", "birthday": datetime(1999, 10, 14)},
        {"name": "Name 22222", "birthday": datetime(1999, 10, 15)},
        {"name": "Getman Skoropadskiy", "birthday": datetime(1999, 10, 16)},
        {"name": "Arni Schwarzneger", "birthday": datetime(1955, 10, 13)}
    ])


