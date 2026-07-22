"""
Browser management for the Daraz scraper.

This module provides a thin wrapper around Playwright that is responsible
for launching and shutting down the browser.
"""

from playwright.sync_api import Page, Playwright, Browser as PlaywrightBrowser, sync_playwright

from daraz_scraper.exceptions import BrowserError

class BrowserManager:
    """Launch and manage a Playwright Chromium browser."""

    def __init__(
        self,
        headless: bool = True,
        args: list[str] | None = None,
    ) -> None:
        self.headless = headless
        self.args = args or ["--no-sandbox"]

        self.playwright: Playwright | None = None
        self.browser: PlaywrightBrowser | None = None
        self.page: Page | None = None

    def start(self) -> Page:
        """Launch Chromium and return a new page."""

        try:
            self.playwright = sync_playwright().start()

            self.browser = self.playwright.chromium.launch(
                headless=self.headless,
                args=self.args,
            )

            self.page = self.browser.new_page()

            return self.page
        except Exception as error:
            raise BrowserError(
                "Failed to launch browser."
            ) from error

    def close(self) -> None:
        """Close the browser and stop Playwright."""

        if self.browser is not None:
            self.browser.close()

        if self.playwright is not None:
            self.playwright.stop()