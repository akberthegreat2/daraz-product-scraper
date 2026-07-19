SEARCH_TERM = "AirPods Pro 2nd Gen"


class DarazSearch:
    BASE_URL = "https://www.daraz.com.bd/catalog/"

    def __init__(self, page):
        self.page = page

    def execute(self):
        url = (
            f"{self.BASE_URL}?q="
            f"{SEARCH_TERM.replace(' ', '+')}"
        )

        self.page.goto(url,wait_until="domcontentloaded",timeout=60000)

        return self.page