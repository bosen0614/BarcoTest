import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import platform

WAIT_TIME = 20
SUPPORTED_BROWSERS = ["chrome", "firefox", "edge", "safari"]
URL = "https://www.barco.com/en/support/clickshare-extended-warranty/warranty"
MAC_OS = "Darwin"
Linux_OS = "Linux"
WINDOWS_OS = "Windows"

class BrowserFactory:
    @staticmethod
    def create_browser(browser_name):
        if browser_name == "chrome":
            options = webdriver.ChromeOptions()
            # options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            options.add_argument('--no-sandbox')
            service = ChromeService(ChromeDriverManager().install())
            return webdriver.Chrome(service=service, options=options)
        elif browser_name == "firefox":
            options = webdriver.FirefoxOptions()
            # options.add_argument('--headless')
            service = FirefoxService(GeckoDriverManager().install())
            return webdriver.Firefox(service=service, options=options)
        elif browser_name == "edge":
            options = webdriver.EdgeOptions()
            # options.add_argument('--headless')
            service = EdgeService(EdgeChromiumDriverManager().install())
            return webdriver.Edge(service=service, options=options)
        elif browser_name == "safari":
            if platform.system() != 'Darwin':
                # 'Darwin' indicates the macOS operating system.
                # Check if the current operating system is not macOS. 
                # When the condition if platform.system() != 'Darwin' is true
                # it means the current operating system is not macOS,
                # and Safari browser cannot be used.                
                logging.warning(f"Safari browser is only supported on macOS.")
                return None
            return webdriver.Safari()
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

class Browser:
    def __init__(self, browser_names):
        self.browsers = []
        for name in browser_names:
            browser = BrowserFactory.create_browser(name)
            if browser is not None:
                self.browsers.append((browser, name))

    def open_url(self, url):
        for driver, _ in self.browsers:
            driver.get(url)
            wait = WebDriverWait(driver, WAIT_TIME)
            accept_cookies_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Accept All Cookies')]"))
            )
            accept_cookies_button.click()

    def quit(self):
        for driver, _ in self.browsers:
            driver.quit()

    def get_drivers(self):
        return self.browsers

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="all", help="browser option: chrome, firefox, edge, safari, or all"
    )

@pytest.fixture(scope="session")
def browser(request):
    browser_instance = None
    try:
        browser_option = request.config.getoption("--browser")
        logging.info(f"Use {browser_option} browser")
        if browser_option == "all":
            browser_names = SUPPORTED_BROWSERS
        else:
            browser_names = [browser_option]

        browser_instance = Browser(browser_names)
        browser_instance.open_url(URL)
        # ------------------------- Testing -------------------------
        yield browser_instance.get_drivers()
        # ------------------------- Teardown -------------------------
    finally:
        if browser_instance:
            logging.info(f"Close {browser_option} browser")
            browser_instance.quit()
