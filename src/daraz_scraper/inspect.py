from .browser import Browser
from .search import DarazSearch


def main():
    browser = BrowserManager(headless=True)

    browser.start()

    page = browser.page


    search = DarazSearch(page)

    search.execute()

    html = page.content()

    with open(
        "data/samples/search_page.html",
        "w",
        encoding="utf-8"
    ) as file:
        file.write(html)

    print("Saved HTML")
    print("Length:", len(html))

    browser.close()


if __name__ == "__main__":
    main()