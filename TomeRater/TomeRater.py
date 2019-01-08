class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, new_email):
        self.email = new_email
        print("{user}'s email has been updated to {email}".format(user = self.name, email = new_email))

    def __repr__(self):
        return "User: {name}, email: {email}, books read: {books}".format(name = self.name, email = self.email, books = len(self.books))

    def __eq__(self, other):
        if self.name == other.name and self.email == other.email:
            return self == other

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        total = 0
        num_ratings = 0
        for rating in self.books.values():
            if rating != None:
                total += rating
                num_ratings += 1
        return total / num_ratings

class Book():
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []
    
    def __repr__(self):
        return self.title

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("{title}'s ISBN has been updated to {ISBN}".format(title = self.title, ISBN = self.isbn))

    def add_rating(self, rating):
        if rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def __eq__(self, other):
        if self.title == other.title and self.isbn == other.isbn:
            return self == other

    def get_average_rating(self):
        total = 0
        num_ratings = 0
        for rating in self.ratings:
            if rating != None:
                total += rating
                num_ratings += 1
        return total / num_ratings

    def	__hash__(self):		
        return hash((self.title, self.isbn))

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def __repr__(self):
        return "{title} by {author}".format(title = self.title, author = self.author)

    def get_author(self):
        return self.author

class NonFiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level
    
    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title = self.title, level = self.level, subject= self.subject)

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level


class TomeRater():
    def __init__(self):
        self.users = {}
        self.books = {}

    def __repr__(self):
        return "This TomeRater has {num_users} users and {num_books} books being rated".format(num_users = len(self.users.values()), num_books = len(self.books))

    def __eq__(self, other):
        if self.users == other.users and self.books == other.books:
            return self == other

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return NonFiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        if email in self.users:
            self.users[email].read_book(book, rating)
            if rating != None:
                book.add_rating(rating)
        else:
            print("No user with email {email}!".format(email = email))

    def add_user(self, name, email, user_books=None):
        if email in self.users and self.users[email] == name:
            print("This user already exists!")
        else:
            self.users[email] = User(name, email)
            if user_books != None:
                for book in user_books:
                    self.add_book_to_user(book, email)
                    if book in self.books:
                        self.books[book] += 1
                    else:
                        self.books[book] = 1

    def print_catalog(self):
        for book in self.books:
            print(book)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def most_read_book(self):
        most_read = []
        most_times_read = 0
        for book in self.books:
            if self.books[book] > most_times_read:
                most_times_read = self.books[book]
                most_read = [book]
            elif self.books[book] == most_times_read:
                most_read.append(book)
        return most_read

    def highest_rated_book(self):
        highest_rating = 0
        highest_rated_book = []
        for book in self.books:
            if book.get_average_rating() > highest_rating:
                highest_rating = book.get_average_rating()
                highest_rated_book = [book]
            elif book.get_average_rating() == highest_rating:
                highest_rated_book.append(book)
        return highest_rated_book

    def most_positive_user(self):
        highest_rating = 0
        most_positive_user = []
        for user in self.users.values():
            if user.get_average_rating() > highest_rating:
                highest_rating = user.get_average_rating()
                most_positive_user = [user]
            elif user.get_average_rating() == highest_rating:
                most_positive_user.append(user)
        return most_positive_user

        