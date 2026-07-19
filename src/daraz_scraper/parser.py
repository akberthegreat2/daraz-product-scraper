from bs4 import BeautifulSoup

from daraz_scraper.models import Product


class ProductParser:

    def parse(self, html: str) -> list[Product]:
        soup = BeautifulSoup(html, "html.parser")

        products = []

        cards = soup.find_all(
            "div",
            attrs={
                "data-qa-locator": "product-item"
            }
        )

        for card in cards:
            products.append(
                Product(
                    name=self._get_name(card),
                    price=self._get_price(card),
                    sold=self._get_sold(card),
                    rating=self._get_rating(card),
                    link=self._get_link(card),
                )
            )

        return products

    def _get_name(self, card) -> str:
        product = card.find(
            "a",
            title=True
        )

        if not product:
            return ""

        return product["title"].strip()

    def _get_price(self, card) -> float:
        price = card.select_one(".ooOxS")

        if not price:
            return 0.0

        value = (
            price.get_text(strip=True)
            .replace("৳", "")
            .replace(",", "")
            .strip()
        )

        try:
            return float(value)

        except ValueError:
            return 0.0

    def _get_sold(self, card) -> int:
        text = card.get_text(
            " ",
            strip=True
        )

        if "sold" not in text:
            return 0

        try:
            sold_text = (
                text.split("sold")[0]
                .strip()
                .split()[-1]
            )

            if sold_text.endswith("K"):
                number = float(
                    sold_text.replace("K", "")
                )

                return int(number * 1000)

            return int(
                float(sold_text)
            )

        except (ValueError, IndexError):
            return 0

    def _get_rating(self, card) -> int:
        rating = card.select_one(".qzqFw")

        if not rating:
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

    def _get_link(self, card) -> str:
        link = card.find(
            "a",
            href=True
        )

        if not link:
            return ""

        href = link["href"]

        if href.startswith("//"):
            return "https:" + href

        return href