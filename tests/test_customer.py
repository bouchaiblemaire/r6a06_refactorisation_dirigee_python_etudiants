from r6a06_customer import Customer, CustomerBuilder, Movie, Rental


def test_should_create_customer_given_default_builder():
    customer = CustomerBuilder().build()
    assert customer is not None


def test_should_return_name_given_customer_with_name():
    customer = Customer("David")
    assert customer.name == "David"


def test_should_generate_statement_given_regular_movie_rental():
    movie1 = Movie("Gone with the Wind", Movie.REGULAR)
    rental1 = Rental(movie1, 3)  # 3 day rental
    customer2 = (
        CustomerBuilder()
        .with_name("Sallie")
        .with_rentals(rental1)
        .build()
    )
    expected = (
        "Record for Sallie\n"
        "\tGone with the Wind\t3.5\n"
        "Amount owed is 3.5\n"
        "You earned 1 frequent renter points"
    )
    statement = customer2.statement()
    assert statement == expected


def test_should_generate_statement_given_new_release_movie_rental():
    movie1 = Movie("Star Wars", Movie.NEW_RELEASE)
    rental1 = Rental(movie1, 3)  # 3 day rental
    customer2 = (
        CustomerBuilder()
        .with_name("Sallie")
        .with_rentals(rental1)
        .build()
    )
    expected = (
        "Record for Sallie\n"
        "\tStar Wars\t9.0\n"
        "Amount owed is 9.0\n"
        "You earned 2 frequent renter points"
    )
    statement = customer2.statement()
    assert statement == expected


def test_should_generate_statement_given_childrens_movie_rental():
    movie1 = Movie("Madagascar", Movie.CHILDRENS)
    rental1 = Rental(movie1, 3)  # 3 day rental
    customer2 = (
        CustomerBuilder()
        .with_name("Sallie")
        .with_rentals(rental1)
        .build()
    )
    expected = (
        "Record for Sallie\n"
        "\tMadagascar\t1.5\n"
        "Amount owed is 1.5\n"
        "You earned 1 frequent renter points"
    )
    statement = customer2.statement()
    assert statement == expected


def test_should_generate_statement_given_multiple_movie_rentals():
    movie1 = Movie("Madagascar", Movie.CHILDRENS)
    rental1 = Rental(movie1, 6)  # 6 day rental

    movie2 = Movie("Star Wars", Movie.NEW_RELEASE)
    rental2 = Rental(movie2, 2)  # 2 day rental

    movie3 = Movie("Gone with the Wind", Movie.REGULAR)
    rental3 = Rental(movie3, 8)  # 8 day rental

    customer1 = (
        CustomerBuilder()
        .with_name("David")
        .with_rentals(rental1, rental2, rental3)
        .build()
    )
    expected = (
        "Record for David\n"
        "\tMadagascar\t6.0\n"
        "\tStar Wars\t6.0\n"
        "\tGone with the Wind\t11.0\n"
        "Amount owed is 23.0\n"
        "You earned 4 frequent renter points"
    )
    statement = customer1.statement()
    assert statement == expected
