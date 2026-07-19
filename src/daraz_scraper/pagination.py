from urllib.parse import urlencode


class Pagination:

    def __init__(self, base_url: str):
        self.base_url = base_url

    def page_url(
        self,
        page_number: int
    ) -> str:

        separator = "&" if "?" in self.base_url else "?"

        return (
            f"{self.base_url}"
            f"{separator}"
            f"page={page_number}"
        )