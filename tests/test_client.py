import math

from unittest.mock import Mock

from daraz_scraper.client import DarazClient


def test_total_pages():
    client = DarazClient(Mock())

    payload = {
        "mainInfo": {
            "totalResults": "81",
            "pageSize": "40",
        }
    }

    assert client.total_pages(payload) == 3


def test_total_pages_exact_multiple():
    client = DarazClient(Mock())

    payload = {
        "mainInfo": {
            "totalResults": "80",
            "pageSize": "40",
        }
    }

    assert client.total_pages(payload) == 2


def test_total_pages_single_page():
    client = DarazClient(Mock())

    payload = {
        "mainInfo": {
            "totalResults": "9",
            "pageSize": "40",
        }
    }

    assert client.total_pages(payload) == 1