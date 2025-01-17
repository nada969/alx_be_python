def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
        return result

    except ValueError as e:
        return ("Error: Please enter numeric values only.")
    
    except ZeroDivisionError as e:
        return ("Error: Cannot divide by zero.")
    
