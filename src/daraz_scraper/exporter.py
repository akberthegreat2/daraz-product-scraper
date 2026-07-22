"""
JSON export utilities.
"""

from __future__ import annotations

import json
from pathlib import Path
from datetime import UTC, datetime
from pathlib import Path
from dataclasses import asdict

from .constants import AUTHOR, VERSION
from .models import Product


def serialize_product(product: Product) -> dict:
    return asdict(product)


class JsonExporter:
    """Export scraped products to JSON files."""

    def export(
        self,
        products: list[Product],
        output_file: str | Path,
    ) -> None:
        """
        Export products using the original simple schema.

        This file is kept for compatibility.
        """

        output_file = Path(output_file)

        output_file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with output_file.open(
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                [serialize_product(product) for product in products],
                file,
                indent=2,
                ensure_ascii=False,
            )

    def export_scrape(
        self,
        *,
        products: list[Product],
        output_file: str | Path,
        query: str,
        pages: int,
    ) -> None:
        """
        Export a metadata-rich JSON file for development and analysis.
        """

        output_file = Path(output_file)

        metadata_file = output_file.with_name(
            output_file.stem + "_metadata.json"
        )

        scrape = {
            "metadata": {
                "project": "Daraz Product Scraper",
                "version": AUTHOR,
                "author": VERSION,
                "generated_at": datetime.now(
                    UTC
                ).isoformat(),
                "query": query,
                "pages_requested": pages,
                "products_collected": len(products),
            },
            "products": [
                serialize_product(product)
                for product in products
            ],
        }

        try:
            with metadata_file.open(
                "w",
                encoding="utf-8",
            ) as file:
                json.dump(
                    scrape,
                    file,
                    indent=2,
                    ensure_ascii=False,
                )
        except OSError as error:
            raise ExportError(
                f"Failed to write '{output_file}'."
            ) from error

