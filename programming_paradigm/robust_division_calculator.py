def safe_divide(numerator, denominator):
    try:
<<<<<<< HEAD
        result = numerator / denominator
=======
        result = float(numerator)/float(denominator)
>>>>>>> 9081896e4398d900f0235364ef3a0243f6af9296
        return (f"The result of the division is {result}")

    except ValueError as e:
        return ("Error: Please enter numeric values only.")
    
    except ZeroDivisionError as e:
        return ("Error: Cannot divide by zero.")
    
print(safe_divide(1,2))