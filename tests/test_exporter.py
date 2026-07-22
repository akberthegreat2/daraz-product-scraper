import json

from daraz_scraper import JsonExporter
from daraz_scraper import Product


def test_json_schema():

    products = [
        Product(
            name="AirPods Pro 2nd Gen",
            price=384.0,
            sold=482,
            rating=4.8,
            link="https://example.com",
        )
    ]

    output = "data/output/test.json"

    exporter = JsonExporter()

    exporter.export(
        products,
        output,
    )

    with open(
        output,
        encoding="utf-8",
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

    assert isinstance(data[0]["price"], float)
    assert isinstance(data[0]["sold"], int)
    assert isinstance(data[0]["rating"], float)
    assert isinstance(data[0]["link"], str)


def test_metadata_export():

    products = [
        Product(
            name="AirPods Pro 2nd Gen",
            price=384.0,
            sold=482,
            rating=4.8,
            link="https://example.com",
        )
    ]

    output = "data/output/test.json"

    exporter = JsonExporter()

    exporter.export_scrape(
        products=products,
        output_file=output,
        query="AirPods Pro",
        pages=1,
    )

    with open(
        "data/output/test_metadata.json",
        encoding="utf-8",
    ) as file:
        data = json.load(file)

    assert "metadata" in data
    assert "products" in data

    metadata = data["metadata"]

    assert metadata["project"] == "Daraz Product Scraper"
    assert metadata["query"] == "AirPods Pro"
    assert metadata["pages_requested"] == 1
    assert metadata["products_collected"] == 1

    assert len(data["products"]) == 1
    assert data["products"][0]["name"] == "AirPods Pro 2nd Gen"