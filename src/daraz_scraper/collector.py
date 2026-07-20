from .pagination import Pagination
from .parser import ProductParser


class ProductCollector:

    def __init__(self, page, base_url, max_pages=100):
        self.page = page
        self.pagination = Pagination(base_url)
        self.parser = ProductParser()
        self.max_pages = max_pages

    def collect(self):

        products = []

        for page_number in range(1, self.max_pages + 1):

            url = self.pagination.page_url(page_number)

            print(f"Scraping page {page_number}")

            self.page.goto(
                url,
                wait_until="domcontentloaded",
                timeout=60000
            )

            html = self.page.content()

            page_products = self.parser.parse(html)

            print(
                f"Found {len(page_products)} products"
            )

            products.extend(page_products)

        return products