from daraz_scraper.parser import ProductParser


def test_product_parser():

    with open(
        "data/samples/search_page.html",
        encoding="utf-8"
    ) as file:
        html = file.read()

    parser = ProductParser()

    products = parser.parse(html)

    assert len(products) > 0

    product = products[0]

    assert product.name
    assert product.price
    assert product.link