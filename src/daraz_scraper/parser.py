"""
Parse structured Daraz API responses into Product objects.
"""

from .models import Product


class ProductParser:
    """Convert Daraz JSON search results into Product objects."""

    def parse(self, payload: dict) -> list[Product]:
        """
        Parse all products from a Daraz AJAX search response.

        Args:
            payload: JSON response returned by the Daraz search endpoint.

        Returns:
            A list of parsed Product objects.
        """

        items = payload.get("mods", {}).get("listItems", [])

        return [
            Product(
                name=item.get("name", ""),
                price=float(item.get("price", 0)),
                sold=self._parse_sold(
                    item.get("itemSoldCntShow", "")
                ),
                rating=float(item.get("ratingScore") or 0),
                link=item.get("itemUrl", ""),
            )
            for item in items
        ]

    def _parse_sold(self, text: str) -> int:
        """
        Convert Daraz sold count text into an integer.

        Examples:
            "280 sold" -> 280
            "3.0K sold" -> 3000
        """

        text = (
            text.lower()
            .replace("sold", "")
            .strip()
        )

        if not text:
            return 0

        try:
            if text.endswith("k"):
                return int(float(text[:-1]) * 1000)

            return int(float(text))

        except ValueError:
            return 0