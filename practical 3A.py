#creating a class book.
class Book:

    
    def accept_details(self):
        #creating a function for accepting details of a book.
        
        self.book_name = input("Enter name of the book:")
        self.book_author = input("Enter the author of the book:")
        self.book_price = int(input("Enter the price of the book:"))
        self.no_of_copies = int(input("Enter number of copies:"))
        
    def total_price(self):
        #calculating total price.
        
        print(f"The total price is :{self.b_price * self.no_of_copies}")
    def details(self):
        #displaying details.
        
        print(f"The name of the book is :{self.book_name}")
        print(f"The author of the book is :{self.book_author}")
        print(f"The price of the book is :{self.book_price}")


book_object = Book()        #creating an object for book.
book_object.accept_details()#calling the method for accepting details.

while True:
    
    print("1.Total price")
    print("2.Display details")
    print("3.quit")
    #creating option system to call methods.
    
    option = int(input("Enter option:"))    #user can enter options to navigate throught the functions.
    if option == 1:
        book_object.total_price()
    elif option ==2:
        book_object.details()
    elif option == 3:
        break
