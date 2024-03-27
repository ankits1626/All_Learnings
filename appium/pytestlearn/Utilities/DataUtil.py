import locale
import logging
import re

from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


def get_number_by_comma(number):
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')  # Set locale to ensure correct formatting
    formatted_number = locale.format_string("%d", number, grouping=True)
    return formatted_number


def get_formatted_number(is_decimal_support_in_transaction_enabled, number):
    log.logger.info(
        f'get formatted number is_decimal_support_in_transaction_enabled = {is_decimal_support_in_transaction_enabled} number = {number}')
    if is_decimal_support_in_transaction_enabled:
        return "%.2f" % number
    else:
        return get_number_by_comma(number)


def extract_number_from_string(string):
    # Use regular expression to extract only digits from the string
    digits_only = re.sub(r'\D', '', string)
    # Convert the resulting string of digits into an integer
    number = int(digits_only)
    return number
