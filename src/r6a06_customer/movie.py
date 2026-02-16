class Movie:
    CHILDRENS = 2
    REGULAR = 0
    NEW_RELEASE = 1

    def __init__(self, title: str, price_code: int):
        self.title = title
        self.price_code = price_code
