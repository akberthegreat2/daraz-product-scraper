from unittest.mock import MagicMock, patch

from daraz_scraper.cli import build_url, main


def test_build_url():
    assert (
        build_url("AirPods Pro 2nd Gen")
        == "https://www.daraz.com.bd/catalog/?q=AirPods+Pro+2nd+Gen"
    )


@patch("daraz_scraper.cli.JsonExporter")
@patch("daraz_scraper.cli.ProductCollector")
@patch("daraz_scraper.cli.BrowserManager")
@patch("daraz_scraper.cli.parse_args")
def test_main(
    mock_parse_args,
    mock_browser,
    mock_collector,
    mock_exporter,
):
    mock_parse_args.return_value = MagicMock(
        query="AirPods",
        pages=2,
        output="output.json",
        headed=False,
    )

    browser = mock_browser.return_value
    browser.page = MagicMock()

    collector = mock_collector.return_value
    collector.collect.return_value = []

    main()

    mock_browser.assert_called_once_with(headless=True)

    collector.collect.assert_called_once()

    mock_exporter.return_value.export.assert_called_once()