# investingcom.py - Get article links from investing.com.

import requests
from bs4 import BeautifulSoup, Tag
import csv
import pprint

BASE_URL: str = "https://www.investing.com"
STOCK_MARKET_NEWS_URL: str = "https://www.investing.com/news/stock-market-news/"


# def getContent(url, div_class):
#     article_response = requests.get(complete_link)
#     article_soup = BeautifulSoup(article_response.text, 'html.parser')

#     # Find specific div element that contains the article content
#     target_div = article_soup.find('div', class_=div_class)

#     if target_div:
#         # Extract all <p> tags from the div element
#         paragraphs = target_div.find_all('p')
#         # Concatenate all <p> tags into one string
#         concatenated_text = ' '.join([p.get_text() for p in paragraphs])
            
#         return concatenated_text
#     # If the div element is not found, return None
#     else:
#         print(f"Could not find a <div> with class '{div_class}' on {url}.")
#         return None



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


def main() -> None:
    for i in range(1, 2):
        # Create the current link by appending the current index number to the end of the URL
        currentLink: str = STOCK_MARKET_NEWS_URL + str(i)

        # Get all the article links for the current news page
        links = getArticleLinks(currentLink)
        pprint.pprint(links)
        print(len(links))


    #     # Write the extracted article's title, link, and summary to a CSV file
    #     with open('investingArticles.csv', 'a', newline='', encoding='utf-8') as csv_file:
    #         csv_writer = csv.writer(csv_file)
            
    #         # Write header to CSV file
    #         if csv_file.tell() == 0:
    #             csv_writer.writerow(['Title', 'Article URL', 'Image URL', 'Article Content', 'Tags'])

    #         for article in article_titles: 
    #             # Write article titles to CSV file
    #             title_elem = article.find('a', class_='title') 
    #             title = title_elem.text.strip()
    #             print(title)

    #             # Write article links to CSV file
    #             link = title_elem['href']
    #             complete_link = 'https://www.investing.com'+ link
    #             print(complete_link)

    #             # Write img links to CSV file
    #             image_elem = article.find('img', class_=' ls-is-cached lazyloaded')
    #             image_link = image_elem['data-src']
    #             print(image_link)

    #             article_content = getContent(complete_link, "WYSIWYG articlePage")

    #             csv_writer.writerow([title, complete_link, image_link, article_content])

    # print("Article information has been successfully written to investingArticles.csv.")


if __name__ == "__main__":
    main()