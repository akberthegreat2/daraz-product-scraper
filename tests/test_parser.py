from daraz_scraper.parser import ProductParser


def test_product_parser():
    payload = {
        "mods": {
            "listItems": [
                {
                    "name": "AirPods Pro",
                    "price": "383",
                    "itemSoldCntShow": "280 sold",
                    "ratingScore": "4.93",
                    "itemUrl": "//www.daraz.com.bd/products/airpods-pro-i123.html",
                }
            ]
        }
    }

    parser = ProductParser()

    products = parser.parse(payload)

    assert len(products) == 1

    product = products[0]

    assert product.name == "AirPods Pro"
    assert product.price == 383.0
    assert product.sold == 280
    assert product.rating == 4.93
    assert product.link.endswith("airpods-pro-i123.html")