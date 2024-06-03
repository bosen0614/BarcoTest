import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string
import re

SERIAL = "serial"

def run_serial_number_tests(browser, serial_num_list, test_case_name, validate_func):
    logging.info("#" * 10 + f" Start testing {test_case_name} " + "#" * 10)
    for driver, browser_name in browser:
        logging.info("#" * 10 + f" Browser: {browser_name} " + "#" * 10)
        for serial_num in serial_num_list:
            run_test(driver, serial_num)
            validate_func(driver, serial_num)

def generate_random_serial_numbers_with_alphabet(n, length=8):
    """
    Generate random serial numbers containing both letters and digits.

    Parameters:
    n (int): The number of serial numbers to generate.
    length (int): The length of each serial number.

    Returns:
    list: A list of randomly generated serial numbers.
    """
    return [
        ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
        for _ in range(n)
    ]

def run_test(driver, serial_nums):
    """
    Run the test by entering the serial number and clicking the "Get info" button.

    Parameters:
    driver (WebDriver): Selenium WebDriver instance.
    serial_nums (str or list): Serial number or a list of serial numbers.
    """
    wait = WebDriverWait(driver, 10)
    serial_input = wait.until(EC.visibility_of_element_located((By.ID, SERIAL)))
    if isinstance(serial_nums, str):
        serial_nums = [serial_nums]
    for serial_num in serial_nums:
        serial_input.clear()
        serial_input.send_keys(serial_num)
        time.sleep(2)
        get_info_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Get info')]")))
        get_info_button.click()
        time.sleep(3)

def generate_random_serial_numbers_with_spaces(n):
    """
    Generate random serial numbers with spaces at the beginning, middle, or end.

    Parameters:
    n (int): The number of serial numbers to generate.

    Returns:
    list: A list of randomly generated serial numbers with spaces.
    """
    result = []
    for _ in range(n):
        random_digits = ''.join(random.choice(string.digits) for _ in range(8))
        position = random.choice(['leading', 'trailing', 'middle'])
        if position == 'leading':
            random_digits = " " + random_digits
        elif position == 'trailing':
            random_digits = random_digits + " "
        elif position == 'middle':
            middle_index = random.randint(1, len(random_digits) - 1)
            random_digits = random_digits[:middle_index] + " " + random_digits[middle_index:]
        result.append(random_digits)
    return result

def contains_special_characters(s):
    """
    Check if a string contains special characters.

    Parameters:
    s (str): The string to check.

    Returns:
    bool: True if the string contains special characters, False otherwise.
    """
    pattern = re.compile(r'[^a-zA-Z0-9]')
    return bool(pattern.search(s))

def contains_alphabet_characters(s):
    """
    Check if a string contains alphabet characters.

    Parameters:
    s (str): The string to check.

    Returns:
    bool: True if the string contains alphabet characters, False otherwise.
    """
    pattern = re.compile(r'[a-zA-Z]')
    return bool(pattern.search(s))

def generate_random_strings(n):
    """
    Generate random strings containing special characters.

    Parameters:
    n (int): The number of strings to generate.

    Returns:
    list: A list of randomly generated strings.
    """
    special_characters = "!@#$%^&*()-_=+[]{}|;:,.<>?/~`"
    all_characters = string.ascii_letters + string.digits + special_characters
    return [
        ''.join(random.choice(all_characters) for _ in range(i))
        for i in range(1, n + 1)
    ]

def generate_random_digits(min_length, max_length):
    """
    Generate random digit strings of varying lengths from min_length to max_length.

    Parameters:
    min_length (int): The minimum length of the digit string.
    max_length (int): The maximum length of the digit string.

    Returns:
    list: A list of randomly generated digit strings.
    """
    digits = string.digits
    return [
        ''.join(random.choice(digits) for _ in range(length))
        for length in range(min_length, max_length + 1)
    ]

def verify_elements(driver, serial_num):
    """
    Verify that elements on the page are present and not empty.

    Parameters:
    driver (WebDriver): Selenium WebDriver instance.
    serial_num (str): The serial number used for the query.
    """
    wait = WebDriverWait(driver, 5)
    try:
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.cmp-product-warranty__inner dl.cmp-product-warranty__list")))
    except Exception as e:
        error_message = f"We couldn't find a product with this serial number {serial_num}. Please double-check the serial number and try again."
        logging.error(error_message)
        return

    elements = {
        "description": "//dt[contains(text(), 'Description')]/following-sibling::dd",
        "part_number": "//dt[contains(text(), 'Part number')]/following-sibling::dd",
        "installation_date": "//dt[contains(text(), 'Installation date')]/following-sibling::dd",
        "warranty_end_date": "//dt[contains(text(), 'Warranty end date')]/following-sibling::dd"
    }
    
    missing_elements = []
    empty_elements = []

    # Verify that elements on the page are present and not empty.
    for key, xpath in elements.items():
        try:
            element = driver.find_element(By.XPATH, xpath)
            element_text = element.text
            if not element_text:
                empty_elements.append(key)
        except Exception as e:
            missing_elements.append(key)
    
    if missing_elements or empty_elements:
        # if missing_elements:
        #     error_message += f"Missing elements: {', '.join(missing_elements)}. "
        # if empty_elements:
        #     error_message += f"Empty elements: {', '.join(empty_elements)}."
        error_message = f"We couldn't find a product with this serial number {serial_num}. Please double-check the serial number and try again."
        logging.error(error_message)
    else:
        logging.info("All elements are present and contain text.")

def verify_error_message(driver, expected_message, data_attribute, serial_num, len_serial=None):
    """
    Verify that the error message is correct.

    Parameters:
    driver (WebDriver): Selenium WebDriver instance.
    expected_message (str): The expected error message.
    data_attribute (str): The HTML attribute containing the error message.
    serial_num (str): The serial number used for the query.
    len_serial (int, optional): The length of the serial number.
    """
    wait = WebDriverWait(driver, 5)
    element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.cmp-product-warranty__inner")))
    actual_message = element.get_attribute(data_attribute)
    if len_serial:
        logging.info(f"Serial number {serial_num} length is {len_serial}.")
    logging.error(f"{actual_message}")
    assert actual_message == expected_message, f"Error message does not match: {actual_message} != {expected_message}"