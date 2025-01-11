FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    TEMP = (fahrenheit-32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return TEMP

def convert_to_fahrenheit(celsius):
    temp = celsius*CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return temp




temp = float(input('Enter the temperature to convert: '))
type_temp =str(input('Is this temperature in Celsius or Fahrenheit? (C/F): '))

# if temp is float:
if type_temp in ['C','c']:
    c_temp = temp
    f_temp = convert_to_fahrenheit(c_temp)
    print(f'{c_temp}°C is {f_temp}°F')

elif type_temp in ['F','f']:
    f_temp = temp
    c_temp = convert_to_celsius(f_temp)
    print(f'{f_temp}°F is {c_temp}°C')
else:
    print("Invalid Temperature unit. please enter (C or F).")
# else:
#     print("Invalid temperature. Please enter a numeric value.")

