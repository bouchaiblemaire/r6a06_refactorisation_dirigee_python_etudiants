from __future__ import annotations

from .movie import Movie
from .rental import Rental


class Customer:
    def __init__(self, name: str):
        self._name = name
        self._rentals: list[Rental] = []


    @property
    def name(self) -> str:
        return self._name

    @property
    def rentals(self) -> list[Rental]:
        return self._rentals

    @name.setter
    def name(self, name: str):
        self._name = name

    @rentals.setter
    def rentals(self, rentals: list[Rental]):
        self._rentals = rentals


    def add_rental(self, arg: Rental):
        self._rentals.append(arg)

    def statement(self) -> str:
        total_amount = 0.0
        frequent_renter_points = 0

        rentals = iter(self._rentals)

        result = "Record for " + self._name + "\n"
        while True:
            try:
                this_amount = 0.0
                each = next(rentals)
            except StopIteration:
                break
            #determine amounts for each line
            if each.movie.price_code == Movie.REGULAR:
                this_amount += 2
                if each.days_rented > 2:

                    this_amount += (each.days_rented - 2) * 1.5
                
            elif each.movie.price_code == Movie.NEW_RELEASE:
                this_amount += each.days_rented * 3
            elif each.movie.price_code == Movie.CHILDRENS:
                this_amount += 1.5
                if each.days_rented > 3:
                    this_amount += (each.days_rented - 3) * 1.5
            # add frequent renter points
            frequent_renter_points += 1
            # add bonus for a two day new release rental
            if (each.movie.price_code == Movie.NEW_RELEASE) and \
                    each.days_rented > 1:
                frequent_renter_points += 1
            #show figures for this rental
            result += "\t" + each.movie.title + "\t" + str(this_amount) + "\n"
            total_amount += this_amount

        #add footer lines
        result += "Amount owed is " + str(total_amount) + "\n"
        result += "You earned " + str(frequent_renter_points) + \
                " frequent renter points"
        return result
