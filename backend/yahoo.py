import requests
from bs4 import BeautifulSoup, Tag
import pprint

from classes.SeleniumScraper import SeleniumScraper

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

BASE_URL: str = "https://finance.yahoo.com"
MAIN_URL: str = "https://finance.yahoo.com/news/"

def main():
    # r = requests.get(MAIN_URL)
    # soup = BeautifulSoup(r.text, "html.parser")

    # Create the scraper instance and navigate to URL
    scraper: SeleniumScraper = SeleniumScraper(MAIN_URL, True)

    # Scroll to the bottom of the page 5 times
    for i in range(5):
        scraper.scrollToBottomAndWait()
    
    # Get the soup from the page
    soup: BeautifulSoup = scraper.createSoup()

    # Get <div> article card elements from the main <div>
    main_div = soup.select_one("#Main")
    article_card_div_elements: list[Tag] = list(main_div.select("li div.Cf"))
    
    links: list[str] = []

    for article_card in article_card_div_elements:
        # Get the divs in each card elements from each card
        card_divs = [child for child in article_card.children if isinstance(child, Tag) and child.name == 'div']

        # Find the href link from one of the divs in the card
        for div in card_divs:
            link_a_element = div.find("a")
            if link_a_element:
                links.append(BASE_URL + link_a_element["href"])
                break

    pprint.pprint(links)

if __name__ == "__main__":
    main()