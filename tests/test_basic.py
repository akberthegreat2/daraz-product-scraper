from daraz_scraper.browser import Browser


def test_browser_opens_daraz():
    browser = Browser(headless=True)

    page = browser.start()

    page.goto("https://www.daraz.com.bd")

    assert "Daraz" in page.title()

    browser.close()