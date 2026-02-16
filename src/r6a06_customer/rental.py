from __future__ import annotations

from .movie import Movie


class Rental:
    def __init__(self, movie: Movie, days_rented: int):
        self.movie = movie
        self.days_rented = days_rented
