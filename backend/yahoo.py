import requests
from bs4 import BeautifulSoup, Tag
import pprint
import time

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
TEST_URL: str = "https://finance.yahoo.com/news/covid-era-program-awash-fraud-141658128.html"


def getLinksFromNewsPage() -> list[str]:
    # Create the scraper instance and navigate to URL
    scraper: SeleniumScraper = SeleniumScraper(MAIN_URL, False)

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

    return links


def getInfoFromArticle(url: str) -> dict[str, str | list[str]]:
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    # Find the title element and get its text
    title_element: Tag = soup.select_one("#caas-lead-header-undefined")
    title: str = title_element.text

    # Find the image element and get its src url (it's always part of a figure)
    img_element: Tag = soup.select_one(".caas-figure img.caas-img")
    image_url: str = img_element["src"]

    # Find the element that holds the main content
    main_content_element: Tag = soup.select_one(".caas-body")

    # Get every <p> element for only text
    p_elements: list[Tag] = list(main_content_element.select("p"))

    # Join all the <p> elements' text with newlines to create the final text content
    text_content: str = "\n".join([p.getText() for p in p_elements])

    return {
        "title": title,
        "article_url": url,
        "image_url": image_url,
        "tags": [],     # Empty tags for now
        "article_content": text_content,
    }


def main():
    # links: list[str] = getLinksFromNewsPage(scraper)
    # pprint.pprint(links)

    info = getInfoFromArticle(TEST_URL)
    pprint.pprint(info)


if __name__ == "__main__":
    main()