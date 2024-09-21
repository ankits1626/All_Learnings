import locale
import logging
import re

from utility.logger import setup_logger

logger = setup_logger()


def get_number_by_comma(number):
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')  # Set locale to ensure correct formatting
    formatted_number = locale.format_string("%d", number, grouping=True)
    return formatted_number


def get_formatted_number(is_decimal_support_in_transaction_enabled, number):
    logger.info(
        f'get formatted number is_decimal_support_in_transaction_enabled = {is_decimal_support_in_transaction_enabled} number = {number}')
    if is_decimal_support_in_transaction_enabled:
        return "%.2f" % number
    else:
        return get_number_by_comma(number)


def extract_number_from_string(string):
    # Use regular expression to extract digits and decimal point
    match = re.search(r'(\d+(\.\d{1,2})?)', string)
    if match:
        number = float(match.group(1)) if '.' in match.group(1) else int(match.group(1))
        return number
    return None  # Return None if no number is found