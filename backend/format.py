import yahoo
import investingcom_new
import cnbc_scraper
import pprint
import json


def main() -> None:
    cnbc_articles = cnbc_scraper.main()
    yahoo_articles = yahoo.main()
    investing_com_articles = investingcom_new.main()

    all_articles: list[dict] = cnbc_articles + yahoo_articles + investing_com_articles

    with open("articles.json", 'w') as json_file:
        json.dump(all_articles, json_file, indent=4)

    pprint.pprint(all_articles)
    print("Articles JSON saved.")

if __name__ == "__main__":
    main()
