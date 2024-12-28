from utils.month_calendar import print_month_calendar
from utils.year_calendar import print_year_calendar

def main():
    while True:
        print("\n--- Calendar Menu ---")
        print("1. Print specific month calendar")
        print("2. Print specific year calendar")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                year = int(input("Enter the year: "))
                month = int(input("Enter the month (1-12): "))
                print_month_calendar(year, month)
            elif choice == 2:
                year = int(input("Enter the year: "))
                print_year_calendar(year)
            elif choice == 3:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid menu option.")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
