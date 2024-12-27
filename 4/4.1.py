import datetime

def display_current_datetime():
    current_datetime = datetime.datetime.now()
    print(f"Текущая дата и время: {current_datetime.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_date_difference(date1: datetime.datetime, date2: datetime.datetime):
    difference = date2 - date1
    print(f"Разница между датами: {difference.days} дней, {difference.seconds // 3600} часов")

def convert_string_to_datetime(date_string: str, format_string: str) -> datetime.datetime:
    try:
        date_object = datetime.datetime.strptime(date_string, format_string)
        print(f"Преобразованная дата и время: {date_object}")
        return date_object
    except ValueError:
        print("Ошибка: строка не соответствует формату.")
        return None
    
print(display_current_datetime())

date1 = datetime.datetime(2024, 12, 1)
date2 = datetime.datetime(2024, 12, 31)
print(calculate_date_difference(date1, date2))

date_string = "2024-12-31 23:00:00"
format_string = "%Y-%m-%d %H:%M:%S"
print(convert_string_to_datetime(date_string, format_string))