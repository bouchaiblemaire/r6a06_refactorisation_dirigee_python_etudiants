class Movie:
    CHILDRENS = 2
    REGULAR = 0
    NEW_RELEASE = 1

    def __init__(self, title: str, price_code: int):
        self._title = title
        self._price_code = price_code

    @property
    def title(self):
        return self._title
    
    @property
    def price_code(self):
        return self._price_code

    @title.setter
    def title(self, title: str):
        self._title = title

    @price_code.setter
    def price_code(self, price_code: int):
        self._price_code = price_code
