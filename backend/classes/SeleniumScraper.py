import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class SeleniumScraper:
    def __init__(self, url: str, isHeadless: bool = True) -> None:
        """
        Create a Selenium instance and navigate to the specified URL.

        Parameters:
        - url (str): The URL to navigate to upon instantiation.
        - isHeadless (bool, optional): Makes the instance headless with no *actual* browser screen. REQUIRED for AWS scraping in the cloud. Defaults to True.
        """

        self.isHeadless: bool = isHeadless
        self.url: str = url

        # Initialize the driver and go to the passed in URL
        self.driver: WebDriver = self.__createDriver()
        self.driver.get(self.url)


    def createSoup(self) -> BeautifulSoup:
        """Return soup that is created from the HTML currently present on the Selenium instance."""
        return BeautifulSoup(self.driver.page_source, "html.parser")


    def scrollToBottomAndWait(self, secondsToWait: int = 1) -> None:
        """
        Scroll the page to the bottom and wait a specified amount of seconds (usually recommended when working with web pages)

        Parameters:
        - secondsToWait (int, optional): Amount of seconds to wait after scrolling. Defaults to 1 second.
        """

        self.driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(secondsToWait) # Let webpage breathe, especially after scrolling


    def __createDriver(self) -> WebDriver:
        """
        Called upon instantiation of the object, actually creates the Selenium instance. Window size is set to 1920x1080.
        Headless options are created if isHeadless was True during initialization of the object.

        Returns:
        WebDriver: The created Selenium driver instance.
        """

        options = Options()
        if self.isHeadless:
            options.add_argument("--headless")
            options.add_argument('--no-sandbox')
            options.add_argument("--disable-gpu")
            options.add_argument("--single-process")
            options.add_argument("--disable-dev-shm-usage")

        # Setting window size to 1920x1080 to prevent clicking errors later because the UI might block something if not maximum size
        driver = webdriver.Chrome(options)
        driver.set_window_size(1920, 1080)

        return driver