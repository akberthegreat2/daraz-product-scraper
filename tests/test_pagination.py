from daraz_scraper.pagination import Pagination


def test_page_url():

    paginator = Pagination(
        "https://www.daraz.com.bd/catalog/?q=test"
    )

    url = paginator.page_url(2)

    assert "page=2" in url
    assert "q=test" in url