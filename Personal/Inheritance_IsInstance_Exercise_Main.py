from Inheritance_IsInstance_Exercise import Product, Movie, Book


def main():
    print("PRODUCT DATA")
    product1 = Product('Quartet Marker', 2.99, 20)
    book1 = Book('The Shining', 12.00, 10, 'Stephen King')
    movie1 = Movie('Venom', 12.00, 5, 2013)
    items = [product1, book1, movie1]
    for item in items:
        if isinstance(item, Product):
            print(Product.name)
            print(Product.getDiscountPrice())
        if isinstance(item, Book):
            print(Book.name)
            print(Book.getDescription())
        if isinstance(item, Movie):
            print(Movie.name)
            print(Movie.year)
            print(Movie.getDiscountprice())


if __name__ == '__main__':
    main()
