FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    TEMP = (fahrenheit-32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return TEMP

def convert_to_fahrenheit(celsius):
    temp = celsius*CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return temp


def get_temp_value():
    while True:
        try:
            return float(input('Enter the temperature to convert: '))
        except ValueError as e:
            print(f'there is an error: {e}')

def get_temp_unit():
    while True:
        try:
            unit = str(input('Is this temperature in Celsius or Fahrenheit? (C/F): ')).upper()
            if unit in ["C", "F"]:
                return unit
            print("Invalid Temperature unit. please enter (C or F).")
        except ValueError as e:
            print(f'there is an error: {e}')

def main():
    value = get_temp_value()
    unit = get_temp_unit()

    if unit == 'C':
        fahrenheit = convert_to_fahrenheit(value)
        print(f'{value:.1f}°C is {fahrenheit:.1f}°F')
    else:  # temp_unit == 'F'
        celsius = convert_to_celsius(value)
        print(f'{value:.1f}°F is {celsius:.1f}°C')


# main()
# # temp = float(input('Enter the temperature to convert: '))
# # type_temp =str(input('Is this temperature in Celsius or Fahrenheit? (C/F): '))

# # if temp is float:
# if type_temp in ['C','c']:
#     c_temp = temp
#     f_temp = convert_to_fahrenheit(c_temp)
#     print(f'{c_temp}°C is {f_temp}°F')

# elif type_temp in ['F','f']:
#     f_temp = temp
#     c_temp = convert_to_celsius(f_temp)
#     print(f'{f_temp}°F is {c_temp}°C')
# else:
#     print("Invalid Temperature unit. please enter (C or F).")
# # else:
# #     print("Invalid temperature. Please enter a numeric value.")


def super_think():
    class root:
        def a(self):
            print("there is Root")    
    class A(root):
        # def a(self):
        #     print("there is a")
        #     super().a()
        pass
    class B(A):
        def a(self):
            print("there is BB")
            super().a()

    b = B()
    b.a()

# super_think()
a = 5
class A:
      a = 7
      pass

class B(A):
      pass

class C(B):
      pass

c = C()
print(c.a)