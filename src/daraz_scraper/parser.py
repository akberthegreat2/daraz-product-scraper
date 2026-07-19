from bs4 import BeautifulSoup

from daraz_scraper.models import Product


class ProductParser:

    def parse(self, html):
        soup = BeautifulSoup(html, "html.parser")

        products = []

        cards = soup.find_all(
            "div",
            attrs={
                "data-qa-locator": "product-item"
            }
        )

        for card in cards:

            name = self._get_name(card)
            price = self._get_price(card)
            sold = self._get_sold(card)
            rating = self._get_rating(card)
            link = self._get_link(card)

            products.append(
                Product(
                    name=name,
                    price=price,
                    sold=sold,
                    rating=rating,
                    link=link
                )
            )

        return products


    def _get_name(self, card):
        item = card.find(
            "a",
            title=True
        )

        return item["title"] if item else ""


    def _get_price(self, card):
        price = card.select_one(
            ".ooOxS"
        )

        return price.text.strip() if price else ""


    def _get_sold(self, card):
        text = card.get_text(" ", strip=True)

        if "sold" in text:
            parts = text.split()

            for i, word in enumerate(parts):
                if word == "sold":
                    return parts[i-1] + " sold"

        return ""


    def _get_rating(self, card):
        rating = card.select_one(
            ".qzqFw"
        )

        return rating.text.strip("()") if rating else ""


    def _get_link(self, card):
        link = card.find("a", href=True)

        if not link:
            return ""

        href = link["href"]

        if href.startswith("//"):
            return "https:" + href

        return href