
import datetime,  _07_bday_messages

today = datetime.date.today()

next_birthday = datetime.date(today.year, 12, 31)

days_away = (next_birthday - today).days

if today == next_birthday:
    print(_07_bday_messages.random_message)

else:
    print(f"Your birthday is in {days_away} days! 🎉")

