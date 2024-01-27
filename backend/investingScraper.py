import requests
from bs4 import BeautifulSoup
import csv

class Article:
    def __init__(self, url):
        self.url = url
        
    def extract_article(self):
        """Extracts article titles, links, and summaries from the webpage and writes them to a CSV file."""
        response = requests.get(url)
        
        if response.status_code == 200:
            
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')
            # Extract all articles from the webpage
            article_titles = soup.find_all('article', class_='js-article-item articleItem')

            # Write the extracted article's title, link, and summary to a CSV file
            with open('article_info.csv', 'w', newline='', encoding='utf-8') as csv_file:
                csv_writer = csv.writer(csv_file)
        
                # Write header to CSV file
                csv_writer.writerow(['Article Title', 'Link', 'Summary'])

                for article in article_titles:    
                    # Write article titles to CSV file
                    title_elem = article.find('a', class_='title') 
                    title = title_elem.text.strip()
                    print(title)

                    # Write article links to CSV file
                    link = title_elem['href']
                    complete_link = 'https://www.investing.com'+ link
                    print(complete_link)

                    # Write article summaries to CSV file else write an empty string
                    summary_elem = article.find('p')
                    summary = summary_elem.text.strip() if summary_elem else ''
                    print(summary)

                    csv_writer.writerow([title, complete_link, summary])
        
            print("Article information has been successfully written to article_info.csv.")
    


if __name__ == '__main__':
    # URL of the webpage: 'Investing.com' to be scraped
    url = 'https://www.investing.com/news/stock-market-news'
    article_scraper = Article(url)
    article_scraper.extract_article()
    

