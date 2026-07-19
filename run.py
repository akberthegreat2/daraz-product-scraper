from daraz_scraper.collector import Collector
from daraz_scraper.exporter import JsonExporter
from daraz_scraper.browser import Browser


BASE_URL = (
    "https://www.daraz.com.bd/catalog/"
    "?q=AirPods+Pro+2nd+Gen"
)

OUTPUT_FILE = "data/output/products.json"


def main():

    browser = Browser(headless=True)

    page = browser.start()

    try:

        collector = Collector(
            page,
            BASE_URL,
            max_pages=100
        )

        products = collector.collect()

        print(
            f"Total products: {len(products)}"
        )

        exporter = JsonExporter()

        exporter.export(
            products,
            OUTPUT_FILE
        )

    finally:
        browser.close()


if __name__ == "__main__":
    main()