SEARCH_TERM = "AirPods Pro 2nd Gen"


class DarazSearch:
    def __init__(self, page):
        self.page = page

    def search(self, keyword=SEARCH_TERM):
        search_url = (
            "https://www.daraz.com.bd/catalog/"
            "?q="
            + keyword.replace(" ", "+")
        )

        self.page.goto(search_url)

        self.page.wait_for_load_state("networkidle")

        return self.page