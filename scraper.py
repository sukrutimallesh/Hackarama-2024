from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome


class WebDriver(object):

    def __init__(self):
        self.options = Options()

        self.options.binary_location = '/opt/headless-chromium'
        self.options.add_argument('--headless')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--start-maximized')
        self.options.add_argument('--start-fullscreen')
        self.options.add_argument('--single-process')
        self.options.add_argument('--disable-dev-shm-usage')

    def get(self):
        driver = Chrome('/opt/chromedriver', options=self.options)
        return driver


def get_tickers(driver):
    """return the number of tickers available on the webpage"""
    TABLE_CLASS = "W(100%)"
    tablerows = len(driver.find_elements(
        By.XPATH, value="//table[@class= '{}']/tbody/tr".format(TABLE_CLASS)))
    return tablerows


def parse_ticker(rownum, table_driver):
    """Parsing each Ticker row by row and return the data in the form of Python dictionary"""
    Symbol = table_driver.find_element(
        By.XPATH, value="//tr[{}]/td[1]".format(rownum)).text
    Name = table_driver.find_element(
        By.XPATH, value="//tr[{}]/td[2]".format(rownum)).text
    LastPrice = table_driver.find_element(
        By.XPATH, value="//tr[{}]/td[3]".format(rownum)).text
    MarketTime = table_driver.find_element(
        By.XPATH, value="//tr[{}]/td[4]".format(rownum)).text
    Change = table_driver.find_element(
        By.XPATH, value="//tr[{}]/td[5]".format(rownum)).text
    PercentChange = table_driver.find_element(
        By.XPATH, value="//tr[{}]/td[6]".format(rownum)).text
    Volume = table_driver.find_element(
        By.XPATH, value="//tr[{}]/td[7]".format(rownum)).text
    MarketCap = table_driver.find_element(
        By.XPATH, value="//tr[{}]/td[8]".format(rownum)).text

    return {
        'Symbol': Symbol,
        'Name': Name,
        'LastPrice': LastPrice,
        'MarketTime': MarketTime,
        'Change': Change,
        'PercentChange': PercentChange,
        'Volume': Volume,
        'MarketCap': MarketCap
    }


FORBES_URL = "https://www.forbes.com/money/?sh=3f6ec8a1c19a"  # global variable

instance_ = WebDriver()
driver = instance_.get()
driver.get(FORBES_URL)
print('Fetching the page')
table_rows = get_tickers(driver)
print('Found {} Tickers'.format(table_rows))
print('Parsing Trending tickers')
table_data = [parse_ticker(i, driver) for i in range(1, table_rows + 1)]
driver.close()
driver.quit()

FINANCIAL_TIMES_URL = "https://www.ft.com/world"  # global variable

instance_ = WebDriver()
driver = instance_.get()
driver.get(FINANCIAL_TIMES_URL)
print('Fetching the page')
table_rows = get_tickers(driver)
print('Found {} Tickers'.format(table_rows))
print('Parsing Trending tickers')
table_data = [parse_ticker(i, driver) for i in range(1, table_rows + 1)]
driver.close()
driver.quit()

REUTERS_URL = "https://www.reuters.com/business/finance/"  # global variable

instance_ = WebDriver()
driver = instance_.get()
driver.get(REUTERS_URL)
print('Fetching the page')
table_rows = get_tickers(driver)
print('Found {} Tickers'.format(table_rows))
print('Parsing Trending tickers')
table_data = [parse_ticker(i, driver) for i in range(1, table_rows + 1)]
driver.close()
driver.quit()

BLOOMBERG_URL = "https://www.bloomberg.com/"  # global variable

instance_ = WebDriver()
driver = instance_.get()
driver.get(BLOOMBERG_URL)
print('Fetching the page')
table_rows = get_tickers(driver)
print('Found {} Tickers'.format(table_rows))
print('Parsing Trending tickers')
table_data = [parse_ticker(i, driver) for i in range(1, table_rows + 1)]
driver.close()
driver.quit()

# global variable
WALL_STREET_JOURNAL_URL = "https://www.wsj.com/finance?mod=nav_top_section"

instance_ = WebDriver()
driver = instance_.get()
driver.get(WALL_STREET_JOURNAL_URL)
print('Fetching the page')
table_rows = get_tickers(driver)
print('Found {} Tickers'.format(table_rows))
print('Parsing Trending tickers')
table_data = [parse_ticker(i, driver) for i in range(1, table_rows + 1)]
driver.close()
driver.quit()
