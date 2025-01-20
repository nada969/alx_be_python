
def safe_divide(numerator:float, denominator:float):
    try:   # first excute this
        result = numerator / denominator
   
    except ValueError :
        return f'Error: Please enter numeric values only.'
    
    except ZeroDivisionError :
        return f'Error: Cannot divide by zero.'
    
    else:   # excute this after try(if there is no excetion)
        return f'The result of the division is {result}'

# first =float(input('enter f='))
# sec= float(input('enter s='))
# print(safe_divide(first,sec))