import unittest
import datetime

def validate_input():
    
    input_data = input("Enter the input to validate: ")

 # Validate symbol (capitalized, 1-7 characters)
    if input_data.isalpha() and input_data.isupper() and 1 <= len(input_data) <= 7:
        return True
    
    # Validate chart type (1 or 2)
    if input_data.isdigit() and input_data in {'1', '2'}:
        return True
    
    # Validate time series (1 - 4)
    if input_data.isdigit() and input_data in {'1', '2', '3', '4'}:
        return True
    
    # Validate start date (date type YYYY-MM-DD)
    try:
        datetime.datetime.strptime(input_data, '%Y-%m-%d')
        return True
    except ValueError:
        pass
    
    # Validate end date (date type YYYY-MM-DD)
    try:
        datetime.datetime.strptime(input_data, '%Y-%m-%d')
        return True
    except ValueError:
        pass
    
    # If none of the above conditions are met, return False
    return False

if __name__ == '__main__':
    print(validate_input())