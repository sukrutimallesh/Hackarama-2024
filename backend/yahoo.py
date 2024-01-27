import requests
from bs4 import BeautifulSoup, Tag
import pprint

BASE_URL: str = "https://finance.yahoo.com"
MAIN_URL: str = "https://finance.yahoo.com/news/"

def main():
    r = requests.get(MAIN_URL)
    soup = BeautifulSoup(r.text, "html.parser")

    # Get <div> article card elements from the main <div>
    main_div: Tag = soup.select_one("#Main")
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