# investingcom.py - Get article links from investing.com.

import requests
from bs4 import BeautifulSoup, Tag
import pprint
import time

import httpx
from httpx import Client

BASE_URL: str = "https://www.investing.com"
STOCK_MARKET_NEWS_URL: str = "https://www.investing.com/news/stock-market-news/"

def getArticleLinks(link: str) -> list[str] | None:
    # Make request to the news page
    response = requests.get(link)

    # If not a valid response, then print a message and return None to indicate something has gone wrong
    if response.status_code != 200:
        print(f"Invalid response for link: {link}")
        return None
    
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Get main section for articles (element with an id of "leftColumn")
    main_element: Tag = soup.select_one("#leftColumn")

    # Get all the <a> tags with a class of "title"
    a_elements: list[Tag] = list(main_element.select("a.title"))

    # Create a list of the href values from all the <a> tags
    # Preprend BASE_URL because the href tags only start from "/news/.../...""
    links: list[str] = [BASE_URL + a["href"] for a in a_elements]

    # There's random links that might be ads or something that do not have the word "news" in them, so filter those out
    links = [link for link in links if "news" in link]

    return links

def getInfoFromArticle(client: Client, url:str) -> dict[str, str | list[str] | None]:
    r = client.get(url)
    
    # Parse the HTML content
    soup = BeautifulSoup(r.text, 'html.parser')

    # Get main section for articles (element with an id of "leftColumn")
    main_element: Tag = soup.select_one("#leftColumn")

    # Get the article title
    title_element: Tag = main_element.select_one("h1.articleHeader")
    title: str = title_element.text

    # Get all the <a> tags with a class of "title"
    img_element: Tag | None = soup.select_one("#carouselImage")

    image_url: str | None = None
    try:
        image_url = img_element["src"]
    except:
        image_url = None

    # Get the article main content
    main_content_element: Tag = soup.select_one("div.WYSIWYG.articlePage")

    # Get all the <p> tags
    p_elements: list[Tag] = list(main_content_element.select("p"))

    # Join all the <p> tags into one string
    text_content: str = "\n".join([p.getText() for p in p_elements])

    unwanted_text = "Position added successfully to:"
    text_content = text_content.replace(unwanted_text, "")

    return {
        "title": title,
        "article_url": url,
        "image_url": image_url,
        "tags": [],     # Empty tags for now
        "article_content": text_content,
    }


def main() -> None:
    all_links: list[str] = []
    for i in range(1, 6):
        # Create the current link by appending the current index number to the end of the URL
        currentLink: str = STOCK_MARKET_NEWS_URL + str(i)

        # Get all the article links for the current news page
        links = getArticleLinks(currentLink)
        
        if links is not None:
            all_links += links

    article_infos: list[dict] = []

    # Get the info from each link (Client utilizes the underlying TCP connection for faster requests)
    with httpx.Client(timeout=10) as client:
        for i, link in enumerate(all_links):
            info = getInfoFromArticle(client, link)
            article_infos.append(info)

    pprint.pprint(article_infos)
    print(len(article_infos))


if __name__ == "__main__":
    main()
