import requests
from bs4 import BeautifulSoup

for i in range(1, 11):

    url = f"https://www.cnbc.com/financial-advisors/?page={i}"

    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    results = soup.find_all(
        "div", class_="Card-standardBreakerCard Card-rectangleToLeftSquareMediaUltraDense Card-rectangleToLeftSquareMedia Card-card")

    for result in results:

        title_element = result.find("a", class_="Card-title")
        image_element = result.find("img", class_="Card-mediaContainerInner")

        title = title_element.text
        article_url = title_element["href"]
        image_url = image_element["src"]

        print("Title:", title)
        print("Article URL:", article_url)
        print("Image URL:", image_url)
        print("tags: []")
        print()
