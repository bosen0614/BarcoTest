# Barco Test Plan and Test Cases

* [About this document](#about_this_document)
* [Test Environment](#test_environment)
* [Test Plan](#test_plan)
* [Test Cases](#test_cases)
  * [Verify Warranty Check with Valid Serial Number](#verify_warranty_check_with_valid_serial_number)
  * [Verify Warranty Check with Empty Serial Number Field](#verify_warranty_check_with_empty_serial_number_field)
  * [Verify Warranty Check with Special Characters in Serial Number](#verify_warranty_check_with_special_characters_in_serial_number)
  * [Verify Warranty Check with Extremely Long Serial Number](#verify_warranty_check_with_extremely_long_serial_number)
  * [Verify Warranty Check with Extremely Short Serial Number](#verify_warranty_check_with_extremely_short_serial_number)
  * [Verify Warranty Check with Leading and Trailing Spaces in Serial Number](#verify_warranty_check_with_leading_and_trailing_spaces_in_serial_number)
  * [Verify Warranty Check Page Elements are Loaded Properly](#verify_warranty_check_page_elements_are_loaded_properly)
  * [Verify Warranty Check with Invalid Serial Number](#verify_warranty_check_with_invalid_serial_number)
* [Generate HTML Test Report](#generate_html_test_report)
* [To do](#to_do)


<a name="about_this_document"></a><font color="blue">About this document</font>
---------------------

This document serves as a comprehensive guide for testing the ClickShare Extended Warranty feature provided by Barco.

### Key Sections:
1. **About this document:** Provides an overview of the document's purpose, which is to serve as a comprehensive guide for testing the ClickShare Extended Warranty feature provided by Barco.
2. **Test Environment:** Details the setup instructions for the testing environment, including the installation of various web browsers.
3. **Test Plan:** Outlines the testing strategy, environment, and scope of testing for the ClickShare Extended Warranty feature.
4. **Test Cases:** Lists detailed test cases that will be executed to verify the functionality of the warranty check feature, covering various scenarios such as valid and invalid serial numbers.
5. **Generate HTML Test Report:** Describes the process of generating HTML reports for test results using the `pytest-html` plugin.
6. **To be discussed:** Placeholder section for any topics that need further discussion.

[Back to Top](#barco-test-plan-and-test-cases)

<a name="test_environment"></a><font color="blue">Test Environment</font>
---------------------
### Browser:

1. **Google Chrome:**
    - **Install Chrome:**
        1. Visit the [Chrome Download](https://www.google.com/chrome/) page.
        2. Click on the "Download Chrome" button.
        3. Follow the installation instructions provided.

2. **Microsoft Edge:**
    - **Install Edge:**
        1. Visit the [Edge Download](https://www.microsoft.com/zh-tw/edge/download?form=MA13FJ) page.
        2. Click on the "Download Edge" button.
        3. Follow the installation instructions provided.

3. **Mozilla Firefox:**
    - **Install Firefox:**
        1. Visit the [Firefox Download](https://www.mozilla.org/en-US/firefox/new/) page.
        2. Click on the "Download Firefox" button.
        3. Follow the installation instructions provided.

4. **Safari:**
    - **Install Safari:**
        1. Visit the [Safari Download](https://safari.en.uptodown.com/windows/download) page.
        2. Click on the "Download" button.
        3. Follow the installation instructions provided.

Follow these steps to download and install each browser to ensure that your development and testing environment is properly set up.

### Set Up Project Requirements
To ensure your development environment has all the necessary libraries, you need to install the dependencies listed in the `requirements.txt` file. Follow these steps:

1. **Open your terminal or command prompt.**

2. **Navigate to the project directory:**

  ```sh
  cd BarcoTest
  ```
3. **Install the dependencies using pip:**
  ```sh
  pip install -r requirements.txt
  ```

[Back to Top](#barco-test-plan-and-test-cases)

<a name="test_plan"></a><font color="blue">Test Plan</font>
---------------------

### Test Plan for ClickShare Extended Warranty Page:

- **Test Scope:** Verify the functionality of the warranty check feature on the ClickShare Extended Warranty page.

#### Test Strategy:

- **Objective:** Ensure the warranty check feature works as expected.
- **Approach:** Perform automated testing.
- **Tools:** Selenium for UI automation, PyTest for test framework.
- **Environment:** Testing will be performed on Windows 10 using Google Chrome, Microsoft Edge, Safari and Firefox.
- **Risks:** Potential UI changes may affect the automation scripts.

[Back to Top](#barco-test-plan-and-test-cases)

<a name="test_cases"></a><font color="blue">Test Cases</font>
---------------------
### Run Tests
To run your tests, you can choose the browser you want to test with. If you do not specify the `--browser` option, tests will run on all supported browsers by default.
- **Example for running tests on Chrome:**

  ```sh
  cd BarcoTest
  python -m pytest --browser=chrome function/test_functions.py
  ```
After verification, an html report will be generated. If not, you can manually add the following parameters `--html`
- **Example for running tests on Chrome:** 
  ```sh
  python -m pytest --browser=chrome function/test_functions.py --html=report.html
  ```
If you would likt just test high level function, please use the `high` option. There are three levels in total, including high, middle and low.
- **Example for running high level tests on Chrome:** 
  ```sh
  python -m pytest -m high --browser=chrome function/test_functions.py
  ```
### Test Case 1:
<a name="verify_warranty_check_with_valid_serial_number"></a><font color="blue">Verify Warranty Check with Valid Serial Number</font>
- **Preconditions:** Navigate to the ClickShare Extended Warranty page.
- **Steps:**
  1. Enter valid serial number `1863552437` into the input field.
  2. Click the "Get info" button.
- **Expected Result:** The system should display the warranty status for the entered serial number.
- **Run command:** : `python -m pytest --browser=chrome function/test_functions.py::test_valid_serial_number`

### Test Case 2:
<a name="verify_warranty_check_with_empty_serial_number_field"></a><font color="blue">Verify Warranty Check with Empty Serial Number Field</font>
- **Preconditions:** Navigate to the ClickShare Extended Warranty page.
- **Steps:**
  1. Leave the serial number input field empty.
  2. Click the "Get info" button.
- **Expected Result:** The system should prompt the user to enter a serial number.
- **Run command:** : `python -m pytest --browser=chrome function/test_functions.py::test_empty_serial_number`

### Test Case 3:
<a name="verify_warranty_check_with_special_characters_in_serial_number"></a><font color="blue">Verify Warranty Check with Special Characters in Serial Number</font>
- **Preconditions:** Navigate to the ClickShare Extended Warranty page.
- **Steps:**
  1. Enter a serial number with special characters (e.g., `!@#$%^&*()`) into the input field.
  2. Click the "Get info" button.
- **Expected Result:** The system should display an error message indicating the serial number is invalid.
- **Run command:** : `python -m pytest --browser=chrome function/test_functions.py::test_special_characters_serial_number`

### Test Case 4:
<a name="verify_warranty_check_with_extremely_long_serial_number"></a><font color="blue">Verify Warranty Check with Extremely Long Serial Number</font>
- **Preconditions:** Navigate to the ClickShare Extended Warranty page.
- **Steps:**
  1. Enter an extremely long serial number which is more than 10 number(e.g., `12345678901234567890`) into the input field.
  2. Click the "Get info" button.
- **Expected Result:** The system should display an error message indicating the serial number is invalid.
- **Run command:** : `python -m pytest --browser=chrome function/test_functions.py::test_extremely_short_long_serial_number`

### Test Case 5:
<a name="verify_warranty_check_with_extremely_short_serial_number"></a><font color="blue">Verify Warranty Check with Extremely Short Serial Number</font>
- **Preconditions:** Navigate to the ClickShare Extended Warranty page.
- **Steps:**
  1. Enter an extremely short serial number which is less than 6 numbers (e.g., `12345`) into the input field.
  2. Click the "Get info" button.
- **Expected Result:** The system should display an error message indicating the serial number is invalid.
- **Run command:** : `python -m pytest --browser=chrome function/test_functions.py::test_extremely_short_long_serial_number`

### Test Case 6:
<a name="verify_warranty_check_with_leading_and_trailing_spaces_and_middle_spaces_in_serial_number"></a><font color="blue">Verify Warranty Check with Leading , Trailing or Middle Spaces in Serial Number</font>
- **Preconditions:** Navigate to the ClickShare Extended Warranty page.
- **Steps:**
  1. Enter a serial number with leading, trailing or middle spaces (e.g., `  18635 52437  `) into the input field.
  2. Click the "Get info" button.
- **Expected Result:** The system should display an error message indicating the serial number is invalid.
- **Run command:** : `python -m pytest --browser=chrome function/test_functions.py::test_leading_and_trailing_spaces_and_middle_spaces_serial_number`

### Test Case 7:
<a name="verify_warranty_check_serial_numbers_with_alphabet"></a><font color="blue">Verify Warranty Check Serial numbers with alphabet</font>
- **Preconditions:** Navigate to the ClickShare Extended Warranty page.
- **Steps:**
  1. Enter a serial number with alphabet(e.g., `18635asd5d`) into the input field.
  2. Click the "Get info" button.
- **Expected Result:** The system should display an error message indicating the serial number is invalid.
- **Run command:** : `python -m pytest --browser=chrome function/test_functions.py::test_alphabet_serial_number`

### Test Case 8:
<a name="verify_warranty_check_with_invalid_serial_number"></a><font color="blue">Verify Warranty Check with Invalid Serial Number</font>
- **Preconditions:** Navigate to the ClickShare Extended Warranty page.
- **Steps:**
  1. Enter valid serial number `12345678` into the input field.
  2. Click the "Get info" button.
- **Expected Result:** The system should display the warranty status for the entered serial number.
- **Run command:** : `python -m pytest --browser=chrome function/test_functions.py::test_invalid_serial_number`

[Back to Top](#barco-test-plan-and-test-cases)

<a name="generate_html_test_report"></a><font color="blue">Generate HTML Test Report</font>
---------------------
To generate HTML reports for your test results using the `pytest-html` plugin, follow these steps:
python -m pytest --browser=chrome function/test_functions.py --html=report.html

1. **Install pytest-html**:

    Ensure you have the `pytest-html` plugin installed. You can ignore this step if you have already installed the dependencies from `requirements.txt`.

    If not, you can install it using `pip`:

    ```sh
    pip install pytest-html
    ```
2. **Run Tests with HTML Report**:
  - **Run tests on all browsers (default) and generate a HTML report:** 
    ```sh
    python -m pytest function/test_functions.py --html=report.html
    ```

3. **Viewing the HTML Report**:    
    After running the tests with the --html option, an HTML report will be generated in the specified file (e.g., report.html). Follow these steps to view the report:

  - **Locate the HTML report file**:  
    The report file will be generated in the directory where you ran the pytest command. For example, if you ran the command from the project root, the report.html file will be in the project root directory.

  - **Open the HTML report**:    
    - **Using a File Explorer**:  
      1. Navigate to the directory containing report.html.
      2. Double-click on report.html to open it in your default web browser.
    - **Using a Web Browser**:    
      1. Open your preferred web browser.
      2. Drag and drop the report.html file into the browser window.
      3. Alternatively, use the browser's "Open File" option (usually accessible via Ctrl+O or Cmd+O) and select the report.html file.

You can view the example full HTML report [here](C:/Users/User/Desktop/Posen/BarcoTest/report.html?sort=result).

[Back to Top](#barco-test-plan-and-test-cases)

<a name="to_do"></a><font color="blue">To do</font>
---------------------
1. Mobile phone (IOS/Android)
2. MacOS windows
3. fuzzy search (ex: \*186355\* )
   
[Back to Top](#barco-test-plan-and-test-cases)
