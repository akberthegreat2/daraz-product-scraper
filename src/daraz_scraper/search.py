"""
Daraz search navigation.
"""

from playwright.sync_api import Page

DEFAULT_SEARCH_TERM = "AirPods Pro 2nd Gen"


class DarazSearch:
    """Navigate to a Daraz search results page."""

    BASE_URL = "https://www.daraz.com.bd/catalog/"

    def __init__(
        self,
        page: Page,
        search_term: str = DEFAULT_SEARCH_TERM,
    ) -> None:
        self.page = page
        self.search_term = search_term

    def build_url(self) -> str:
        """Build the Daraz search URL."""

        query = self.search_term.replace(" ", "+")

        return f"{self.BASE_URL}?q={query}"

    def navigate(self) -> Page:
        """Open the search results page."""

        self.page.goto(
            self.build_url(),
            wait_until="domcontentloaded",
            timeout=60_000,
        )

        return self.page