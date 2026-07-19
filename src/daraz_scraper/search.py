SEARCH_TERM = "AirPods Pro 2nd Gen"


class DarazSearch:

    BASE_URL = "https://www.daraz.com.bd/catalog/"

    def __init__(self, page):
        self.page = page

    def build_url(self):
        return (
            f"{self.BASE_URL}"
            f"?q={SEARCH_TERM.replace(' ', '+')}"
        )

    def execute(self):

        self.page.goto(
            self.build_url(),
            wait_until="domcontentloaded",
            timeout=60000
        )

        return self.page