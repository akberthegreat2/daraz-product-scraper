"""
Custom exceptions used throughout the Daraz scraper.
"""


class DarazScraperError(Exception):
    """Base exception for the Daraz scraper."""


class BrowserError(DarazScraperError):
    """Raised when browser operations fail."""


class RequestError(DarazScraperError):
    """Raised when a request to Daraz fails."""


class ParsingError(DarazScraperError):
    """Raised when product data cannot be parsed."""


class ExportError(DarazScraperError):
    """Raised when exporting scraped data fails."""