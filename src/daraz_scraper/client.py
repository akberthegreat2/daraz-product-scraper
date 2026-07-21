import json
import math

from playwright.sync_api import Page


class DarazClient:
    """Fetch structured product data from Daraz."""

    def __init__(self, page: Page):
        self.page = page

    def get_search_results(self, url: str) -> dict:
        response = self.page.goto(
            url,
            wait_until="networkidle",
            timeout=60000,
        )

        if response is None:
            raise RuntimeError("No response received from Daraz.")

        if not response.ok:
            raise RuntimeError(
                f"HTTP {response.status}: {response.url}"
            )

        return json.loads(response.text())

    def total_pages(self, payload: dict) -> int:
        """Return the total number of available pages."""

        main_info = payload["mainInfo"]

        total_results = int(main_info["totalResults"])
        page_size = int(main_info["pageSize"])

        if page_size <= 0:
            raise ValueError("Invalid page size returned by Daraz.")

        return math.ceil(total_results / page_size)