"""
Command-line interface for the Daraz Product Scraper.
"""

import argparse

from daraz_scraper import BrowserManager
from daraz_scraper import JsonExporter
from daraz_scraper import ProductCollector

import logging

logger = logging.getLogger(__name__)

DEFAULT_QUERY = "AirPods Pro 2nd Gen"
DEFAULT_OUTPUT = "data/output/products.json"


def build_url(query: str) -> str:
    """Build a Daraz search URL."""

    return (
        "https://www.daraz.com.bd/catalog/"
        f"?q={query.replace(' ', '+')}"
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
        help="Run browser with GUI",
    )

    return parser.parse_args()

def main() -> None:
    """Run the scraper."""

    args = parse_args()

    browser = BrowserManager(
        headless=not args.headed,
    )

    browser.start()

    try:
        collector = ProductCollector(
            page=browser.page,
            base_url=build_url(args.query),
            max_pages=args.pages,
        )

        products = collector.collect()

        logger.info(f"Collected {len(products)} products.")

        JsonExporter().export(
            products,
            args.output,
        )

        logger.info(f"Saved results to '{args.output}'.")

    except KeyboardInterrupt:
        logger.info("\nScraping cancelled by user.")

    except Exception as error:
        logger.info(f"\nError: {error}")
        raise

    finally:
        browser.close()

if __name__ == "__main__":
    main()