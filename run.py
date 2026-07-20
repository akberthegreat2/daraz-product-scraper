from daraz_scraper import ProductCollector
from daraz_scraper import JsonExporter
from daraz_scraper import Browser


BASE_URL = (
    "https://www.daraz.com.bd/catalog/"
    "?q=AirPods+Pro+2nd+Gen"
)

OUTPUT_FILE = "data/output/products.json"


def main():

    browser = Browser(headless=True)

    browser.start()

    page = browser.page

    try:

        collector = ProductCollector(
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