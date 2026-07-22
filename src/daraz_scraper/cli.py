"""
Command-line interface for the Daraz Product Scraper.
"""

import argparse
import logging

from urllib.parse import urlencode

from daraz_scraper import (
    __version__,
    BrowserManager,
    JsonExporter,
    ProductCollector,
)

from daraz_scraper.logging_config import configure_logging
from daraz_scraper.exceptions import DarazScraperError

DEFAULT_QUERY = "AirPods Pro 2nd Gen"
DEFAULT_OUTPUT = "data/output/products.json"


def build_url(query: str) -> str:
    """Build a Daraz search URL."""

    return (
        "https://www.daraz.com.bd/catalog/?"
        + urlencode({"q": query})
    )

def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(
        description="Scrape products from Daraz."
    )

    parser.add_argument(
        "query",
        nargs="?",
        default=DEFAULT_QUERY,
        help="Search query",
    )

    parser.add_argument(
        "-p",
        "--pages",
        type=int,
        default=100,
        help="Maximum pages to scrape",
    )

    parser.add_argument(
        "-o",
        "--output",
        default=DEFAULT_OUTPUT,
        help="Output JSON file",
    )

    parser.add_argument(
        "--headed",
        action="store_true",
        help="Run browser with a visible browser window.",
    )

    return parser.parse_args()


def main() -> int:
    """Run the scraper."""

    configure_logging()

    logger = logging.getLogger(__name__)

    logger.info(
        "Daraz Product Scraper %s",
        __version__,
    )

    args = parse_args()

    browser = BrowserManager(
        headless=not args.headed,
    )

    products = []

    try:
        browser.start()

        collector = ProductCollector(
            page=browser.page,
            base_url=build_url(args.query),
            max_pages=args.pages,
        )

        products = collector.collect()

        logger.info(
            "Collected %d products.",
            len(products),
        )

        JsonExporter().export(
            products,
            args.output,
        )

        JsonExporter().export_scrape(
            products=products,
            output_file="data/output/scrape.json",
            query=args.query,
            pages=args.pages,
        )

        logger.info(
            "Saved %d products to %s.",
            len(products),
            args.output,
        )

        return 0

    except KeyboardInterrupt:
        logger.info("Scraping cancelled by user.")
        return 130

    except DarazScraperError:
        logger.exception(
            "Scraping failed."
        )
        return 1

    finally:
        try:
            browser.close()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    raise SystemExit(main())