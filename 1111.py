from datetime import datetime, timedelta
try:
    date_order=datetime.strptime (input('введите дату (гггг-мм-дд): '), '%Y-%m-%d')
    date_b=datetime(datetime.now().year, 7, 31)
    current_date=datetime.now()
    if current_date == date_b:
        print("с днем рождени202я, Гарри! Вечеринка сегодня!")
    elif current_date > date_b:
        print("Вечеринка уже прошла. До следующего дня рождения Гарри осталось 364 дня")
    else:
         print("вечеринка еще впереди.Осталось 6 дней до дня рождения Гарри.")
except ValueError as G:
    print(G)

