from datetime import datetime , timedelta
def display_current_datetime():
    current_date = datetime.datetime.now()
    print('Current date and time:',current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date

def calculate_future_date():
    future_date=int(input('Enter the number of days to add to the current date: '))
    future_date = datetime.now() + timedelta(future_date)
    
    # print(f'Future date: {display_current_datetime().year}-{display_current_datetime().month}-{future_date}')
    print(future_date.strftime("%Y-%m-%d"))

# display_current_datetime()
calculate_future_date()
