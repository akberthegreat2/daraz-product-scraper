"""
Project-wide constants.
"""

from importlib.metadata import version

from pathlib import Path

PROJECT_NAME = "daraz-product-scraper"

AUTHOR = "Sakib"

TRANSPORT = "Playwright response interception"

SOURCE = "Daraz JSON"

VERSION = version("daraz-product-scraper")

OUTPUT_DIR = Path("data/output")

PRODUCTS_FILE = OUTPUT_DIR / "products.json"

SCRAPE_FILE = OUTPUT_DIR / "scrape.json"

METADATA_FILE = OUTPUT_DIR / "scrape_metadata.json"