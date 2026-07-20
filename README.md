# Daraz Product Scraper

A modern, modular web scraper for **Daraz** built with **Playwright** and **BeautifulSoup**.

Production-oriented Python scraper for collecting Daraz search results for "AirPods Pro 2nd Gen" with fixed JSON schema export.

Unlike many scraping projects that place all logic inside a single script, this project is designed with maintainability in mind. Navigation, pagination, parsing, exporting, and browser management are separated into dedicated modules, making the code easier to understand, extend, and test.

> **Project Status:** Early Development (v0.1.0)

---

## Features

- Modern browser automation using Playwright
- HTML parsing with BeautifulSoup
- Typed product data model
- Multi-page product collection
- Clean modular architecture
- JSON export
- Unit tests
- Easy to extend for additional exporters or scraping features

---

## Project Structure

```
daraz-product-scraper/
│
├── src/
│   └── daraz_scraper/
│       ├── browser.py
│       ├── collector.py
│       ├── exporter.py
│       ├── models.py
│       ├── pagination.py
│       ├── parser.py
│       ├── search.py
│       └── ...
│
├── tests/
│
├── run.py
├── pyproject.toml
└── README.md
```

### Module Overview

| Module | Responsibility |
|---------|----------------|
| `browser.py` | Launches and manages the Playwright browser |
| `search.py` | Performs product searches on Daraz |
| `pagination.py` | Handles navigation across multiple result pages |
| `collector.py` | Coordinates scraping and product collection |
| `parser.py` | Extracts structured product data from HTML |
| `models.py` | Defines typed product models |
| `exporter.py` | Exports collected products |

---

# Requirements

- Python 3.11 or newer
- Chromium browser (installed through Playwright)

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

Activate the environment.

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install the package.

```bash
pip install -e .
```

Install the Playwright browser.

```bash
playwright install chromium
```

---

# Quick Start

Run the project using

```bash
python run.py
```

Adjust the search term or configuration inside `run.py` as needed.

---

# How It Works

The scraper follows a simple pipeline.

```
Browser
    │
    ▼
Search Products
    │
    ▼
Navigate Pages
    │
    ▼
Collect HTML
    │
    ▼
Parse Product Data
    │
    ▼
Typed Product Objects
    │
    ▼
Export Results
```

Keeping each step independent makes the project easier to maintain and extend.

---

# Output

The scraper currently exports product information as JSON.

Example output:

```json
{
  "name": "Apple AirPods Pro (2nd Generation)",
  "price": "32990",
  "rating": 4.9,
  "sold": "500+",
  "link": "https://..."
}
```

---

# Running Tests

Execute the test suite with

```bash
pytest
```

---

# Troubleshooting

## Chromium executable not found

If you see an error similar to

```
Executable doesn't exist...
```

Playwright's browser binaries have not been installed.

Run

```bash
playwright install chromium
```

and try again.

---

## Virtual environment not activated

If Python cannot locate dependencies, make sure your virtual environment is activated before running the project.

---

## Updating Playwright

If Playwright is updated, reinstall the browser binaries.

```bash
playwright install chromium
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

Lint the project.

```bash
ruff check .
```

---

# Roadmap

Planned improvements include

- CSV export
- Excel export
- SQLite export
- Retry mechanism
- Better exception handling
- CLI interface
- Logging improvements
- GitHub Actions
- Documentation website

---

# Contributing

Contributions, bug reports, feature requests, and suggestions are welcome.

If you discover a bug or have an idea for improvement, feel free to open an issue or submit a pull request.

---

# License

This project is licensed under the MIT License.

---

# Why This Project?

This project was built as an exercise in writing **clean, maintainable Python**, not simply scraping data.

The focus is on:

- modular architecture
- readable code
- typed data models
- separation of concerns
- maintainability over shortcuts

The goal is to provide a solid foundation that can grow into a production-quality scraping library.