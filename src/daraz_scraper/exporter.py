import json

from dataclasses import asdict

from daraz_scraper.models import Product


class JsonExporter:

    REQUIRED_FIELDS = [
        "name",
        "price",
        "sold",
        "rating",
        "link",
    ]

    def export(self, products, filename):

        output = []

        for product in products:
            data = asdict(product)

            clean_data = {
                field: data.get(field, "")
                for field in self.REQUIRED_FIELDS
            }

            output.append(clean_data)

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                output,
                file,
                ensure_ascii=False,
                indent=2
            )