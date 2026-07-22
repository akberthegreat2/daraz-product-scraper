# Daraz Product Scraper

![CI](https://github.com/akberthegreat2/daraz-product-scraper/actions/workflows/ci.yml/badge.svg)

A modern, modular **Daraz product scraper** built with **Python** and **Playwright**.

Instead of scraping fragile HTML, this project captures Daraz's own AJAX search responses and extracts structured product data directly from the returned JSON. This approach is significantly more reliable against front-end layout changes while keeping the codebase clean, testable, and easy to extend.

Unlike many scraping projects that place everything inside a single script, this project separates browser management, networking, pagination, parsing, exporting, and data models into dedicated modules following clean software engineering practices.

> **Project Status:** v0.1.0

---

# Features

* Modern browser automation using Playwright
* Intercepts Daraz AJAX search responses
* Parses structured JSON instead of HTML
* Typed product data model
* Automatic multi-page collection
* Automatic pagination detection
* Clean modular architecture
* JSON export
* Metadata-rich scrape archive
* Unit tests with pytest
* Easily extensible for future exporters

---

# Project Structure

```text
daraz-product-scraper/
│
├── src/
│   └── daraz_scraper/
│       ├── browser.py
│       ├── client.py
│       ├── collector.py
│       ├── exporter.py
│       ├── models.py
│       ├── pagination.py
│       ├── parser.py
│       ├── search.py
│       ├── version.py
│       └── ...
│
├── tests/
├── data/
│   ├── output/
│   └── samples/
│
├── pyproject.toml
└── README.md
```

---

# Module Overview

| Module          | Responsibility                                    |
| --------------- | ------------------------------------------------- |
| `browser.py`    | Launches and manages the Playwright browser       |
| `client.py`     | Retrieves Daraz AJAX search responses             |
| `collector.py`  | Coordinates the complete scraping workflow        |
| `pagination.py` | Generates page URLs                               |
| `parser.py`     | Converts Daraz JSON payloads into Product objects |
| `models.py`     | Defines typed product models                      |
| `exporter.py`   | Writes JSON exports                               |
| `search.py`     | Builds search URLs                                |

---

# Requirements

* Python 3.11 or newer
* Chromium browser (installed through Playwright)

---

# Installation

Clone the repository.

```bash
git clone https://github.com/akberthegreat2/daraz-product-scraper.git

cd daraz-product-scraper
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate it.

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install the project.

```bash
pip install -e .
```

Install Chromium for Playwright.

```bash
playwright install chromium
```

---

# Quick Start

Scrape products.

```bash
daraz-scraper "AirPods Pro 2nd Gen"
```

Limit the number of pages.

```bash
daraz-scraper "Mechanical Keyboard" --pages 5
```

Save to a custom output file.

```bash
daraz-scraper "RTX 5070" --output data/output/gpus.json
```

Launch a visible browser.

```bash
daraz-scraper "SSD" --headed
```

Display all options.

```bash
daraz-scraper --help
```

---

# Architecture

The scraper no longer parses product cards from HTML.

Instead, it allows Daraz's website to load normally, intercepts the browser's own AJAX search request, and parses the returned JSON payload.

```text
Browser
    │
    ▼
Load Search Page
    │
    ▼
Intercept AJAX Response
    │
    ▼
Parse JSON Payload
    │
    ▼
Create Product Objects
    │
    ▼
Export Results
```

This design offers several advantages:

* Less affected by UI redesigns
* Faster parsing
* Structured product data
* Cleaner code
* Better long-term maintainability

---

# Output

The scraper produces two JSON files.

## products.json

A lightweight export containing only parsed products.

Example:

```json
{
  "name": "Apple AirPods Pro (2nd Generation)",
  "price": 32990.0,
  "sold": 580,
  "rating": 4.9,
  "link": "https://www.daraz.com.bd/..."
}
```

## scrape.json

A metadata-rich archive containing information about the scrape, including:

* search query
* timestamp
* scraper version
* total products
* parsed products
* raw Daraz payload

This file is intended for debugging, auditing, and future development.

---

# Running Tests

Run the complete test suite.

```bash
pytest
```

---

# Development

Install development dependencies.

```bash
pip install -e ".[dev]"
```

Run tests.

```bash
pytest
```

Run Ruff.

```bash
ruff check .
```

---

# Troubleshooting

## Chromium executable not found

Install the Playwright browser.

```bash
playwright install chromium
```

---

## Virtual environment not activated

Activate your virtual environment before running the project.

---

## Updating Playwright

If Playwright is upgraded, reinstall the browser binaries.

```bash
playwright install chromium
```

---

# Roadmap

Future improvements include:

* CSV exporter
* Excel exporter
* SQLite exporter
* Retry mechanism
* Better request throttling
* Progress bar
* GitHub Actions
* Docker support
* Documentation website

---

# Why This Project?

This project was created as an exercise in building production-quality Python software rather than simply collecting product data.

The emphasis is on:

* clean architecture
* maintainable code
* modular design
* typed models
* testing
* extensibility
* reliability

One interesting engineering challenge was adapting the scraper after discovering that direct requests to Daraz's internal search endpoint were protected by Alibaba's anti-bot systems. The project was redesigned to intercept the browser's own AJAX responses instead, resulting in a more robust and maintainable solution.

---

# Contributing

Bug reports, feature requests, pull requests, and suggestions are welcome.

---

# Acknowledgements

This project was developed by **Sakib**.

Special thanks to **ChatGPT (OpenAI)** for assistance with architecture discussions, debugging, testing, documentation, code review, and design decisions throughout the development of this project.

---

# License

This project is licensed under the MIT License.

![License](https://img.shields.io/badge/license-MIT-green.svg)
