import calendar

def print_month_calendar(year, month):
    """Prints the calendar of a specific month."""
    try:
        print(calendar.month(year, month))
    except calendar.IllegalMonthError:
        print("Invalid month. Please enter a value between 1 and 12.")
    except ValueError:
        print("Invalid year. Please enter a positive year value.")
