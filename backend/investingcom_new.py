import requests
from bs4 import BeautifulSoup, Tag
import json

BASE_URL: str = f"https://www.investing.com"

def main() -> list[dict]:
    articles: list[dict] = []

    for i in range(1, 6):

        url = f"https://www.investing.com/news/stock-market-news/{i}"

        response = requests.get(url)

        soup = BeautifulSoup(response.content, "html.parser")

        # Get main section for articles (element with an id of "leftColumn")
        main_element: Tag = soup.select_one("#leftColumn")

        # Get all the <a> tags with a class of "title"
        a_elements: list[Tag] = list(main_element.select("a.title"))

        # Create a list of the href values from all the <a> tags
        # Preprend BASE_URL because the href tags only start from "/news/.../...""
        links: list[str] = [BASE_URL + a["href"] for a in a_elements]

        # There's random links that might be ads or something that do not have the word "news" in them, so filter those out
        links = [link for link in links if "news" in link]
        
        for link in links:

            # Make a request to the article URL
            article_response = requests.get(link)
            article_soup = BeautifulSoup(article_response.content, "html.parser")

            # Get main section for articles (element with an id of "leftColumn")
            main_element: Tag = article_soup.select_one("#leftColumn")

            # Get the article title
            title_element: Tag = main_element.select_one("h1.articleHeader")
            title: str = title_element.text

            # Get all the <a> tags with a class of "title"
            img_element: Tag | None = article_soup.select_one("#carouselImage")

            image_url: str | None = None
            try:
                image_url = img_element["src"]
            except:
                image_url = None

            # Get the article main content
            main_content_element: Tag = article_soup.select_one("div.WYSIWYG.articlePage")

            # Get all the <p> tags
            p_elements: list[Tag] = list(main_content_element.select("p"))

            # Join all the <p> tags into one string
            text_content: str = "\n".join([p.getText() for p in p_elements])

            unwanted_text = "Position added successfully to:"
            article_content = text_content.replace(unwanted_text, "")
            # Create Article object

            article = {
                "title": title,
                "article_url": link,
                "image_url": image_url,
                "tags": [],
                "article_content": article_content
            }

            articles.append(article)

    return articles

    # # Convert the list of Article objects to JSON format
    # articles_json = json.dumps(articles, indent=2)

    # # Print the JSON data
    # print(articles_json)


if __name__ == "__main__":
    main()