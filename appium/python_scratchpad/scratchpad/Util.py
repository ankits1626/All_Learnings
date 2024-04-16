from datetime import datetime


def _reformat_date(date_str):
    # List of date formats to try
    date_formats = [
        '%d %b %Y',  # e.g., 10 Nov 2021
        '%b %d, %Y',  # e.g., Nov 10, 2021
        '%Y-%m-%d',  # e.g., 2021-11-10 (ISO format)
        '%d %B %Y',  # e.g., 05 March 2024
        '%Y/%m/%d',  # e.g., 2021/11/10
        '%m/%d/%Y',  # e.g., 11/10/2021
        '%d-%m-%Y',  # e.g., 10-11-2021
        '%m-%d-%Y',  # e.g., 11-10-2021
        '%d/%m/%Y',  # e.g., 10/11/2021
        '%Y.%m.%d',  # e.g., 2021.11.10
        '%m.%d.%Y',  # e.g., 11.10.2021
        '%d.%m.%Y',  # e.g., 10.11.2021
        # Add more formats here as needed
    ]

    for fmt in date_formats:
        try:
            parsed_date = datetime.strptime(date_str, fmt)
            return parsed_date.strftime('%Y-%m-%d')
        except ValueError:
            pass

    # Return the original date string if all parsing attempts fail
    return date_str

print("Parsed date from func:", _reformat_date('05 March 2024'))
print("Parsed date from func:", _reformat_date('Nov 10, 2021'))
print("Parsed date from func:", _reformat_date('05 March 2024'))
print("Parsed date from func:", _reformat_date('2021-11-10'))
print("Parsed date from func:", _reformat_date('2021/11/10'))
print("Parsed date from func:", _reformat_date('2021-11-10'))



date_string = "05 March 2024"
parsed_date1 = datetime.strptime(date_string, "%d %B %Y")

print("Parsed date:", parsed_date1)