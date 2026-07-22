"""
Logging configuration for Daraz Product Scraper.
"""

from __future__ import annotations

import logging
from datetime import datetime
from pathlib import Path


LOG_DIRECTORY = Path("logs")
LOG_DIRECTORY.mkdir(
    parents=True,
    exist_ok=True,
)

LOG_FILE = (
    LOG_DIRECTORY
    / f"scraper_{datetime.now():%Y%m%d_%H%M%S}.log"
)


def configure_logging() -> None:
    """
    Configure console and file logging.
    """

    logging.basicConfig(
        level=logging.INFO,
        format=(
            "%(asctime)s | "
            "%(levelname)-8s | "
            "%(name)s | "
            "%(message)s"
        ),
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(
                LOG_FILE,
                encoding="utf-8",
            ),
        ],
    )