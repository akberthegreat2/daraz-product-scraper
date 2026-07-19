from dataclasses import dataclass


@dataclass
class Product:

    name: str
    price: float
    sold: int
    rating: int
    link: str