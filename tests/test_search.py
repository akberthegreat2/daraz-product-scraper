from daraz_scraper import BrowserManager
from daraz_scraper import DarazSearch


def test_daraz_search():
    browser = BrowserManager(headless=True)

    browser.start()

    page = browser.page


    search = DarazSearch(page)
    search.execute()

    assert "catalog" in page.url

    browser.close()