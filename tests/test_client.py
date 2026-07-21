from unittest.mock import Mock

import pytest

from daraz_scraper.client import DarazClient


def test_get_search_results_returns_json():
    response = Mock()
    response.ok = True
    response.status = 200
    response.url = "https://example.com"
    response.text.return_value = '{"mods":{"listItems":[]}}'

    page = Mock()
    page.goto.return_value = response

    client = DarazClient(page)

    data = client.get_search_results("https://example.com")

    assert data["mods"]["listItems"] == []


def test_get_search_results_raises_when_request_fails():
    response = Mock()
    response.ok = False
    response.status = 500
    response.url = "https://example.com"

    page = Mock()
    page.goto.return_value = response

    client = DarazClient(page)

    with pytest.raises(RuntimeError):
        client.get_search_results("https://example.com")


def test_get_search_results_raises_when_no_response():
    page = Mock()
    page.goto.return_value = None

    client = DarazClient(page)

    with pytest.raises(RuntimeError):
        client.get_search_results("https://example.com")