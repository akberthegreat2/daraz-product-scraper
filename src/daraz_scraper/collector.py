"""
Collect products from Daraz search results.
"""

from playwright.sync_api import Page

from .client import DarazClient
from .pagination import Pagination
from .parser import ProductParser
from .models import Product


class ProductCollector:
    """Collect products across multiple Daraz search result pages."""

    def __init__(
        self,
        page: Page,
        base_url: str,
        max_pages: int = 100,
    ) -> None:
        """
        Initialize the product collector.

        Args:
            page: Active Playwright page.
            base_url: Daraz search URL.
            max_pages: Maximum number of pages to scrape.
        """
        self.client = DarazClient(page)
        self.pagination = Pagination(base_url)
        self.parser = ProductParser()
        self.max_pages = max_pages

    def collect(self) -> list[Product]:
        """
        Collect products from all requested pages.

        Returns:
            A list of Product objects.
        """
        products: list[Product] = []

        for page_number in range(1, self.max_pages + 1):
            url = self.pagination.page_url(page_number)

            payload = self.client.get_search_results(url)

            page_products = self.parser.parse(payload)

            if not page_products:
                break

            products.extend(page_products)

        return products