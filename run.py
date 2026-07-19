from daraz_scraper.browser import Browser
from daraz_scraper.search import DarazSearch
from daraz_scraper.parser import ProductParser
from daraz_scraper.exporter import JsonExporter


OUTPUT_FILE = "data/output/products.json"


def main():

    browser = Browser(headless=True)

    page = browser.start()

    try:
        search = DarazSearch(page)

        search.execute()

        html = page.content()

        parser = ProductParser()

        products = parser.parse(html)

        print(
            f"Products found: {len(products)}"
        )

        exporter = JsonExporter()

        exporter.export(
            products,
            OUTPUT_FILE
        )

        print(
            f"Saved: {OUTPUT_FILE}"
        )

    finally:
        browser.close()


if __name__ == "__main__":
    main()