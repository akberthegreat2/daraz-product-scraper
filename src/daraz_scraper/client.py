import json
import math

from playwright.sync_api import Page


class DarazClient:
    """Fetch structured product data from Daraz."""

    def __init__(self, page: Page):
        self.page = page

    def get_search_results(self, url: str) -> dict:
        """
        Fetch the JSON search response by letting Daraz's own page
        perform the AJAX request.
        """

        normal_url = url.replace(
            "&ajax=true&isFirstRequest=true",
            "",
        )

        with self.page.expect_response(
            lambda response: (
                "ajax=true" in response.url
                and response.request.resource_type == "xhr"
            ),
            timeout=60000,
        ) as response_info:

            self.page.goto(
                normal_url,
                wait_until="networkidle",
            )

        response = response_info.value

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