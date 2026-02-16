from __future__ import annotations

from app.domain.customer import Customer
from app.domain.rental import Rental


class CustomerBuilder:
    NAME = "Gregroire"

    def __init__(self):
        self.name = CustomerBuilder.NAME
        self.rentals: list[Rental] = []

    def build(self) -> Customer:
        result = Customer(self.name)
        for rental in self.rentals:
            result.add_rental(rental)
        return result

    def with_name(self, name: str) -> CustomerBuilder:
        self.name = name
        return self

    def with_rentals(self, *rentals: Rental) -> CustomerBuilder:
        self.rentals.extend(rentals)
        return self
