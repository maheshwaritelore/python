import calendar

def print_year_calendar(year):
    """Prints the calendar of a specific year."""
    try:
        print(calendar.TextCalendar().formatyear(year, 2, 1, 1, 3))
    except ValueError:
        print("Invalid year. Please enter a positive year value.")
