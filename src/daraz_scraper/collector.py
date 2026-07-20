"""
Product collection pipeline.
"""

from playwright.sync_api import Page

from .pagination import Pagination
from .parser import ProductParser
from .models import Product


class ProductCollector:
    """Collect products from multiple Daraz search result pages."""

    def __init__(
        self,
        page: Page,
        base_url: str,
        max_pages: int = 100,
    ) -> None:
        self.page = page
        self.pagination = Pagination(base_url)
        self.parser = ProductParser()
        self.max_pages = max_pages

    def collect(self) -> list[Product]:
        """Collect products across all configured pages."""

        products: list[Product] = []

        for page_number in range(1, self.max_pages + 1):
            page_products = self._collect_page(page_number)
            products.extend(page_products)

        return products

    def _collect_page(
        self,
        page_number: int,
    ) -> list[Product]:
        """Collect products from a single page."""

        url = self.pagination.page_url(page_number)

        print(f"Scraping page {page_number}")

        self.page.goto(
            url,
            wait_until="domcontentloaded",
            timeout=60_000,
        )

        html = self.page.content()

        products = self.parser.parse(html)

        print(f"Found {len(products)} products")

        return products