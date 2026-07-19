from daraz_scraper.browser import Browser
from daraz_scraper.search import DarazSearch


def main():
    browser = Browser(headless=True)

    page = browser.start()

    search = DarazSearch(page)

    search.search()

    print("TITLE:", page.title())
    print("URL:", page.url)

    page.screenshot(path="search_result.png")

    browser.close()


if __name__ == "__main__":
    main()
