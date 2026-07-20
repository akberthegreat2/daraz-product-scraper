"""
JSON export utilities.
"""

import json
from dataclasses import asdict
from pathlib import Path

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