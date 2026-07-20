from .browser import Browser
from .search import DarazSearch

import logging

logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO,format="%(asctime)s | %(levelname)s | %(message)s")

def main():
    browser = BrowserManager(headless=True)

    browser.start()

    page = browser.page


    search = DarazSearch(page)

    search.navigate()

    html = page.content()

    with open(
        "data/samples/search_page.html",
        "w",
        encoding="utf-8"
    ) as file:
        file.write(html)

    logger.info("Saved HTML")
    logger.info("Length:", len(html))

    browser.close()


if __name__ == "__main__":
    main()