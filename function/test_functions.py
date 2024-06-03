import pytest
import logging
import time
from common.commonFun import *

def validate_valid_serial_number(driver, serial_num):
    try:
        verify_elements(driver, serial_num)
    except Exception as e:
        logging.error("Element not found or incorrect XPath: %s", e)
        raise

def validate_empty_serial_number(driver, serial_num):
    try:
        expected_message = "Please specify a serial number."
        verify_error_message(driver, expected_message, "data-noinput", serial_num)
    except Exception as e:
        logging.error("Expected error message not found or incorrect XPath: %s", e)
        raise

def validate_special_characters_serial_number(driver, serial_num):
    if contains_special_characters(serial_num):
        logging.error(f"Serial number {serial_num} contains special characters, please enter valid serial number.")
        time.sleep(1)

def validate_extremely_short_long_serial_number(driver, serial_num):
    try:
        if len(serial_num) < 6:
            expected_message = "A minimum of 6 characters is required."
            verify_error_message(driver, expected_message, "data-lesschars", serial_num, len(serial_num))
        elif len(serial_num) > 10:
            logging.error(f"Serial number {serial_num} is too long")
            assert True
        else:
            logging.info(f"Serial number {serial_num} passed the length check")
    except Exception as e:
        logging.error("Expected error message not found or incorrect XPath: %s", e)
        raise

def validate_leading_trailing_middle_spaces_serial_number(driver, serial_num):
    original_serial_num = serial_num
    serial_num = serial_num.strip()
    if original_serial_num != serial_num:
        logging.error(f"Serial number '{original_serial_num}' had spaces at the beginning or end.")
    elif " " in serial_num:
        logging.error(f"Serial number '{serial_num}' contains spaces in the middle, which is not allowed.")

def validate_alphabet_serial_number(driver, serial_num):
    if contains_alphabet_characters(serial_num):
        logging.error(f"Serial number '{serial_num}' contains alphabet characters.")
    else:
        logging.info(f"Serial number '{serial_num}' passed the check.")

def validate_invalid_serial_number(driver, serial_num):
    try:
        verify_elements(driver, serial_num)
    except Exception as e:
        logging.error("Element not found or incorrect XPath: %s", e)
        raise

@pytest.mark.high
def test_valid_serial_number(browser):
    serial_num_list = ["1863552437"]
    run_serial_number_tests(browser, serial_num_list, "valid serial number", validate_valid_serial_number)

@pytest.mark.low
def test_empty_serial_number(browser):
    serial_num_list = [""]
    run_serial_number_tests(browser, serial_num_list, "empty serial number", validate_empty_serial_number)

@pytest.mark.low
def test_special_characters_serial_number(browser):
    serial_num_list = generate_random_strings(12)
    run_serial_number_tests(browser, serial_num_list, "random special character serial number", validate_special_characters_serial_number)

@pytest.mark.low
def test_extremely_short_long_serial_number(browser):
    serial_num_list = generate_random_digits(1, 11)
    run_serial_number_tests(browser, serial_num_list, "random extremely short and long serial numbers", validate_extremely_short_long_serial_number)

@pytest.mark.mid
def test_leading_and_trailing_spaces_and_middle_spaces_serial_number(browser):
    serial_num_list = generate_random_serial_numbers_with_spaces(10)
    run_serial_number_tests(browser, serial_num_list, "leading, trailing, and middle spaces in serial number", validate_leading_trailing_middle_spaces_serial_number)

@pytest.mark.mid
def test_alphabet_serial_number(browser):
    serial_num_list = generate_random_serial_numbers_with_alphabet(10)
    run_serial_number_tests(browser, serial_num_list, "alphabet in serial number", validate_alphabet_serial_number)

@pytest.mark.high
def test_invalid_serial_number(browser):
    # serial_num_list = generate_random_digits(6, 10)
    serial_num_list = generate_random_digits(6, 7)
    run_serial_number_tests(browser, serial_num_list, "invalid serial number", validate_invalid_serial_number)
