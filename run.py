from daraz_scraper.browser import Browser


def main():
    browser = Browser(headless=True, args=["--no-sandbox"])

    page = browser.start()

    page.goto("https://www.daraz.com.bd")

    print("TITLE:", page.title())

    page.screenshot(path="daraz_home.png")

    browser.close()


if __name__ == "__main__":
    main()