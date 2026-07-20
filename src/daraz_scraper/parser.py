"""
Product HTML parser.
"""

from bs4 import BeautifulSoup
from bs4.element import Tag

from .models import Product


class ProductParser:
    """Convert Daraz product cards into Product objects."""

    def parse(self, html: str) -> list[Product]:
        """Parse all products from a search results page."""

        soup = BeautifulSoup(html, "html.parser")

        cards = soup.find_all(
            "div",
            attrs={"data-qa-locator": "product-item"},
        )

        return [self._parse_card(card) for card in cards]

    def _parse_card(self, card: Tag) -> Product:
        """Parse a single product card."""

        return Product(
            name=self._get_name(card),
            price=self._get_price(card),
            sold=self._get_sold(card),
            rating=self._get_rating(card),
            link=self._get_link(card),
        )

    def _get_name(self, card: Tag) -> str:
        """Extract the product name."""

        product = card.find("a", title=True)

        if product is None:
            return ""

        return product["title"].strip()

    def _get_price(self, card: Tag) -> float:
        """Extract the product price."""

        price = card.select_one(".ooOxS")

        if price is None:
            return 0.0

        value = (
            price.get_text(strip=True)
            .replace("৳", "")
            .replace(",", "")
        )

        try:
            return float(value)
        except ValueError:
            return 0.0

    def _get_sold(self, card: Tag) -> int:
        """Extract the sold count."""

        text = card.get_text(" ", strip=True)

        if "sold" not in text:
            return 0

        try:
            sold_text = (
                text.split("sold")[0]
                .strip()
                .split()[-1]
            )

            if sold_text.endswith("K"):
                return int(float(sold_text[:-1]) * 1000)

            return int(float(sold_text))

        except (ValueError, IndexError):
            return 0

    def _get_rating(self, card: Tag) -> int:
        """Extract the rating count."""

        rating = card.select_one(".qzqFw")

        if rating is None:
            return 0

        value = (
            rating.get_text(strip=True)
            .replace("(", "")
            .replace(")", "")
        )

        try:
            return int(value)
        except ValueError:
            return 0

    def _get_link(self, card: Tag) -> str:
        """Extract the product URL."""

        link = card.find("a", href=True)

        if link is None:
            return ""

        href = link["href"]

        if href.startswith("//"):
            return f"https:{href}"

        return href