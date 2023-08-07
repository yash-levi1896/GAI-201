def safe_divide(dividend, divisor):
    try:
        result = dividend / divisor
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero."
    
print(safe_divide(5,10))
print(safe_divide(5,0))