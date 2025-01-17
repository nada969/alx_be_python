def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
        return result

    except ValueError as e:
        return (f' there is an error: {e}')
    
    except ZeroDivisionError as e:
        return (f' there is an error: {e}')
    
