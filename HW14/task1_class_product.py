class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Book(Product):
    def __init__(self, name, price, quantity, author):
        super().__init__(name, price, quantity)
        self.author = author

    def read(self):
        print(f"Book Title: {self.name}\nAuthor: {self.author}\nPrice:\
 ${self.price}\nQuantity Available: {self.quantity}")


# Example usage:
my_book = Book('The Black Swan', 10.99, 50, 'Nassim Nicholas Taleb')
my_book.read()
