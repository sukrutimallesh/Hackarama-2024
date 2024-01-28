import requests
from bs4 import BeautifulSoup
import json


def main():
    articles = []

    for i in range(1, 11):

        url = f"https://www.cnbc.com/financial-advisors/?page={i}"

        response = requests.get(url)

        soup = BeautifulSoup(response.content, "html.parser")

        results = soup.find_all(
            "div", class_="Card-standardBreakerCard Card-rectangleToLeftSquareMediaUltraDense Card-rectangleToLeftSquareMedia Card-card")

        for result in results:

            title_element = result.find("a", class_="Card-title")
            image_element = result.find(
                "img", class_="Card-mediaContainerInner")

            title = title_element.text
            article_url = title_element["href"]
            image_url = image_element["src"] if image_element else None

            # Make a request to the article URL
            article_response = requests.get(article_url)
            article_soup = BeautifulSoup(
                article_response.content, "html.parser")

            # Extract article content
            article_content_element = article_soup.find(
                "div", class_="ArticleBody-articleBody")
            article_content = article_content_element.text.strip(
            ) if article_content_element else ""

            # Create Article object
            article = {
                "title": title,
                "article_url": article_url,
                "image_url": image_url,
                "tags": [],
                "article_content": article_content
            }

            articles.append(article)

    # Convert the list of Article objects to JSON format
    articles_json = json.dumps(articles, indent=2)

    # Print the JSON data
    print(articles_json)


if __name__ == "__main__":
    main()
