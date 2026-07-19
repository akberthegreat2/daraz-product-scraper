from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: str
    sold: str
    rating: str
    link: str