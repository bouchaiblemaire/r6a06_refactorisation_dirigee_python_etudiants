from __future__ import annotations

from app.domain.movie import Movie


class Rental:
    def __init__(self, movie: Movie, days_rented: int):
        self._movie = movie
        self._days_rented = days_rented

    @property
    def days_rented(self):
        return self._days_rented

    @property
    def movie(self):
        return self._movie

    @movie.setter
    def movie(self, movie: Movie):
        self._movie = movie

    @days_rented.setter
    def days_rented(self, value):
        self._days_rented = value
