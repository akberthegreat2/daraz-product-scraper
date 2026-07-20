from playwright.sync_api import sync_playwright


class Browser:
    def __init__(self, headless=True, args=None):
        self.headless = headless
        self.playwright = None
        self.browser = None
        self.page = None
        self.args = args or ["--no-sandbox"]

    def start(self):
        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            headless=self.headless
        )

        self.page = self.browser.new_page()

        return self.page

    def close(self):
        if self.browser:
            self.browser.close()

        if self.playwright:
            self.playwright.stop()