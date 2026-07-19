import json

from daraz_scraper.exporter import JsonExporter
from daraz_scraper.models import Product


def test_json_schema():

    products = [
        Product(
            name="AirPods Pro 2nd Gen",
            price="৳384",
            sold="482 sold",
            rating="78",
            link="https://example.com"
        )
    ]

    output = "data/output/test.json"

    exporter = JsonExporter()

    exporter.export(
        products,
        output
    )

    with open(
        output,
        encoding="utf-8"
    ) as file:

        data = json.load(file)

    assert len(data) == 1

    assert list(data[0].keys()) == [
        "name",
        "price",
        "sold",
        "rating",
        "link",
    ]