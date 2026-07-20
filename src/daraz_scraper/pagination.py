"""
Pagination utilities for Daraz search results.
"""

from urllib.parse import parse_qs, urlencode, urlparse, urlunparse


class Pagination:
    """Generate paginated Daraz search URLs."""

    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def page_url(self, page_number: int) -> str:
        """
        Return the URL for the requested page number.
        """

        parsed = urlparse(self.base_url)

        query = parse_qs(parsed.query)
        query["page"] = [str(page_number)]

        return urlunparse(
            parsed._replace(query=urlencode(query, doseq=True))
        )