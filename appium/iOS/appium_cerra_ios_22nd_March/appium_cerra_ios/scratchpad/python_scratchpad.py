import re

def extract_number_from_string(string):
    # Use regular expression to extract digits and decimal point
    match = re.search(r'(\d+(\.\d{1,2})?)', string)
    if match:
        number = float(match.group(1))
        # Round the number to two decimal places
        num  =  round(number, 2)
        return f"{num:.2f}"
    return None  # Return None if no number is found

# Example usage
string_with_decimal = "You have 1970857.00 points"
string_without_decimal = "You have 1970857 points"

print(extract_number_from_string(string_with_decimal))  # Output: 1970857.0
print(extract_number_from_string(string_without_decimal))  # Output: 1970857.0
