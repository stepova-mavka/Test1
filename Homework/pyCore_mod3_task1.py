from datetime import datetime
import re

def get_days_from_today_date(date):
    try:
        date = re.sub(r"(\d{4}).(\d{2}).(\d{2})", r"\1-\2-\3", date) # validate function input
        selected_date = datetime.strptime(date, "%Y-%m-%d").date() # convert to string to date
        today_date = datetime.today().date() 
        delta = selected_date - today_date #det difference
    except ValueError:
        return "invalid date!"
    else:
        return delta.days

print(get_days_from_today_date("2026.02.008"))
