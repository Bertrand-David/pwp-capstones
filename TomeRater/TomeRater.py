class User(object):
    def __init__(self, name = str, email = str):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, new_email = str):
        self.email = new_email
        print("{name}'s email address updated.".format(name = self.name))

    def __repr__(self):
        return "User {name}, email: {email}, books read: {number}.".format(name = self.name, email = self.email, number = len(self.books))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False

    def read_book(self, book = str, rating = None):
        self.books[book] = rating

    def get_average_rating(self):
        self.total_rating = 0
        self.ratings_number = 0
        for book in self.books:
            if self.books[book] != None:
                self.total_rating += self.books[book]
                self.ratings_number += 1
            else:
                continue
        if self.ratings_number != 0:
            return self.total_rating / self.ratings_number
        else:
            return "No ratings."

class Book(object):
    def __init__(self, title = str, isbn = int):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn = int):
        self.isbn = new_isbn
        print("ISBN of {title} updated.".format(title = self.title))

    def add_rating(self, rating = int):
        if rating != None:
            if rating in range(0, 5):
                self.ratings.append(rating)
            else:
                print("Invalid Rating.")

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else:
            return False

    def get_average_rating(self):
        self.total_ratings = 0
        if len(self.ratings) != 0:
            for rating in self.ratings:
                self.total_ratings += rating
            return self.total_ratings / len(self.ratings)
        else:
            return "No ratings"

    def __hash__(self):
        return hash((self.title, self.isbn))

class Fiction(Book):
    def __init__(self, title = str, author = str, isbn = int):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}.".format(title = self.title, author = self.author)

class Non_Fiction(Book):
    def __init__(self, title = str, subject = str, level = str, isbn = int):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}.".format(title = self.title, level = self.level, subject = self.subject)

class TomeRater():
    def __init__(self):
        self.users = {}
        self.books = {}
        self.isbn_lst = []

#Additional error testing
    def create_book(self, title, isbn):
        if self.isbn_control(isbn) == True:
            return Book(title, isbn)

#Additional error testing
    def create_novel(self, title, author, isbn):
        if self.isbn_control(isbn) == True:
            return Fiction(title, author, isbn)

#Additional error testing
    def create_non_fiction(self, title, subject, level, isbn):
        if self.isbn_control(isbn) == True:
            return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating = None):
        if email not in self.users.keys():
            print("No user with email {email}!".format(email = email))
        else:
            self.users[email].read_book(book, rating)
            book.add_rating(rating)
            if book not in self.books.keys():
                self.books[book] = 1
            else:
                self.books[book] += 1

#Additional error testing
    def add_user(self, name, email, user_books = None):
        if self.email_control(email) == True:
            if email in self.users.keys():
                print("User profile using same email ({email}) already present.".format(email = email))
            else:
                self.users[email] = User(name, email)
                if user_books != None:
                    for book in user_books:
                        self.add_book_to_user(book, email)

    def print_catalog(self):
        for book in self.books.keys():
            print(book)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def get_most_read_book(self):
        top_readings = -float("inf")
        most_read_book = ""
        for book in self.books.keys():
            if self.books[book] > top_readings:
                top_readings = self.books[book]
                most_read_book = book
            else:
                continue
        return str(most_read_book) + " (" + str(top_readings) + ")"

    def highest_rated_book(self):
        top_rating = -float("inf")
        top_rated_book = ""
        for book in self.books.keys():
            book_rating = book.get_average_rating()
            if book_rating > top_rating:
                top_rating = book_rating
                top_rated_book = book
            else:
                continue
        return str(top_rated_book) + " (" + str(top_rating) + ")"

    def most_positive_user(self):
        top_ratings = -float("inf")
        top_rater = ""
        for user in self.users.values():
            user_ratings = user.get_average_rating()
            if user_ratings > top_ratings:
                top_ratings = user_ratings
                top_rater = user
            else:
                continue
        return str(top_rater)+ " (" + str(top_ratings) + ")"

# Additional error testing
    def isbn_control(self, isbn):
        if isbn not in self.isbn_lst:
            self.isbn_lst.append(isbn)
            return True
        else:
            print("Reference already declared -> ISBN: {isbn}.".format(isbn = isbn))
            return False

#Additional error testing
    def email_control(self, email):
        if "@" not in email or email[-4:] not in [".com", ".edu", ".org"]:
            print("Invalid email address.")
            return False
        else:
            return True