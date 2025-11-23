from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print("Current Date and Time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    Days_to_add = int(input("Enter number of days to add to the current date: "))
    future_date = datetime.now() + timedelta(days=Days_to_add)
    print("Future Date after adding", Days_to_add, "days:", future_date.strftime("%Y-%m-%d %H:%M:%S"))

