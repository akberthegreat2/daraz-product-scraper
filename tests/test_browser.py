from daraz_scraper import BrowserManager


def test_browser_opens_daraz():
    browser = BrowserManager(headless=True)

    browser.start()

    page = browser.page


    page.goto("https://www.daraz.com.bd",wait_until="domcontentloaded")

    assert "Daraz" in page.title()

    browser.close()