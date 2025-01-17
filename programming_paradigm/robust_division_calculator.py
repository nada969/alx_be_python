def safe_divide(numerator, denominator):
    try:
        result = float(numerator) / float(denominator)
        print(result)

    except ValueError as e:
        print(f' there is an error: {e}')
    
    except ZeroDivisionError as e:
        print(f' there is an error: {e}')
    
safe_divide("l",4)
