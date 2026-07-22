"""
JSON export utilities.
"""

import json
from dataclasses import asdict
from pathlib import Path
from datetime import datetime

from importlib.metadata import version

from .constants import AUTHOR
from .constants import PROJECT_NAME
from .constants import SOURCE
from .constants import TRANSPORT

from .models import Product


class JsonExporter:
    """Export products to a JSON file."""

    REQUIRED_FIELDS = (
        "name",
        "price",
        "sold",
        "rating",
        "link",
    )

    def export(
        self,
        products: list[Product],
        filename: str | Path,
    ) -> None:
        """Export products to a formatted JSON file."""

        output = [
            self._serialize(product)
            for product in products
        ]

        filename = Path(filename)

        filename.parent.mkdir(parents=True, exist_ok=True)

        with filename.open(
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                output,
                file,
                ensure_ascii=False,
                indent=2,
            )

    def _serialize(
        self,
        product: Product,
    ) -> dict:
        """Convert a Product into a JSON-compatible dictionary."""

        data = asdict(product)

        return {
            field: data.get(field, "")
            for field in self.REQUIRED_FIELDS
            }

    def export_scrape(
        self,
        products: list[Product],
        filename: str,
        *,
        query: str,
        pages: int,
    ) -> None:
        """
        Export products together with scrape metadata.
        """

        path = Path(filename)
        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        payload = {
            "metadata": {
                "project": "daraz-product-scraper",
                "version": version(PROJECT_NAME),
                "author": "Sakib",
                "scraped_at": (
                    datetime.now()
                    .astimezone()
                    .isoformat()
                ),
                "query": query,
                "pages": pages,
                "products": len(products),
                "transport": (
                    "Playwright response interception"
                ),
                "source": "Daraz JSON",
            },
            "products": [
                product.model_dump()
                for product in products
            ],
        }

        with path.open(
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                payload,
                file,
                ensure_ascii=False,
                indent=2,
            )