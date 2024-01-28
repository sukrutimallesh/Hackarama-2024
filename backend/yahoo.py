# yahoo.py - Scroll the Yahoo Finance "News" page several times and get info from 100 news links.

# Native imports
import pprint
import time

# Third Party imports
import httpx
from httpx import Client
from bs4 import BeautifulSoup, Tag

# User imports
from classes.SeleniumScraper import SeleniumScraper


# Constants
BASE_URL: str = "https://finance.yahoo.com"
MAIN_URL: str = "https://finance.yahoo.com/news/"


def getLinksFromNewsPage() -> list[str]:
    # Create the scraper instance and navigate to URL
    scraper: SeleniumScraper = SeleniumScraper(MAIN_URL, True)

    # Scroll to the bottom of the page several times
    for i in range(10):
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


def getInfoFromArticle(client: Client, url: str) -> dict[str, str | list[str] | None]:
    r = client.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    # Find the title element and get its text
    title_element: Tag = soup.select_one("#caas-lead-header-undefined")
    title: str = title_element.text

    # Find the image element (it's always part of a figure)
    img_element: Tag | None = soup.select_one(".caas-figure img.caas-img")
    
    # Some articles do not have an image or it is bugged, just discard the image in both cases
    image_url: str | None = None
    try:
        image_url = img_element["src"]
    except:
        image_url = None

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


def main() -> None:
    # Get the links, only keep 100 of them if > 100 options
    links: list[str] = getLinksFromNewsPage()
    links = links[:100] if len(links) > 100 else links

    article_infos: list[dict] = []

    # Get the info from each link (Client utilizes the underlying TCP connection for faster requests)
    with httpx.Client(timeout=10) as client:
        for i, link in enumerate(links):
            info = getInfoFromArticle(client, link)
            article_infos.append(info)

            # TODO: Delete once you want all 100 articles
            if i == 9:
                break
    
    pprint.pprint(article_infos)
    print(len(article_infos))

if __name__ == "__main__":
    main()