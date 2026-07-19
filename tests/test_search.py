from daraz_scraper.browser import Browser
from daraz_scraper.search import DarazSearch


def test_daraz_search():
    browser = Browser(headless=True)

    page = browser.start()

    search = DarazSearch(page)
    search.execute()

    assert "catalog" in page.url

    browser.close()