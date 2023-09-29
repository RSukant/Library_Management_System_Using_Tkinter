class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book_id, title, author):
        if book_id not in self.books:
            self.books[book_id] = {"title": title, "author": author, "status": "available"}
            print(f"Book '{title}' by {author} added successfully.")
        else:
            print("Book with this ID already exists.")

    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            print("Book removed successfully.")
        else:
            print("Book not found.")

    def borrow_book(self, book_id, member_id):
        if book_id in self.books:
            if self.books[book_id]["status"] == "available":
                if member_id in self.members:
                    self.books[book_id]["status"] = "borrowed"
                    self.books[book_id]["borrower"] = member_id
                    print(f"Book '{self.books[book_id]['title']}' borrowed by Member {member_id}.")
                else:
                    print("Member not found.")
            else:
                print("Book is already borrowed.")
        else:
            print("Book not found.")

    def return_book(self, book_id):
        if book_id in self.books:
            if self.books[book_id]["status"] == "borrowed":
                member_id = self.books[book_id]["borrower"]
                self.books[book_id]["status"] = "available"
                del self.books[book_id]["borrower"]
                print(f"Book '{self.books[book_id]['title']}' returned by Member {member_id}.")
            else:
                print("This book is not borrowed.")
        else:
            print("Book not found.")

    def list_books(self):
        if self.books:
            print("Available Books:")
            for book_id, book_info in self.books.items():
                if book_info["status"] == "available":
                    print(f"ID: {book_id}, Title: {book_info['title']}, Author: {book_info['author']}")
        else:
            print("No books available.")

    def add_member(self, member_id, name):
        if member_id not in self.members:
            self.members[member_id] = {"name": name}
            print(f"Member {name} added successfully.")
        else:
            print("Member with this ID already exists.")

    def remove_member(self, member_id):
        if member_id in self.members:
            del self.members[member_id]
            print("Member removed successfully.")
        else:
            print("Member not found.")

    def list_members(self):
        if self.members:
            print("Library Members:")
            for member_id, member_info in self.members.items():
                print(f"ID: {member_id}, Name: {member_info['name']}")
        else:
            print("No members available.")


def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. List Available Books")
        print("6. Add Member")
        print("7. Remove Member")
        print("8. List Members")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_id = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            library.add_book(book_id, title, author)
        elif choice == "2":
            book_id = input("Enter Book ID to remove: ")
            library.remove_book(book_id)
        elif choice == "3":
            book_id = input("Enter Book ID to borrow: ")
            member_id = input("Enter Member ID: ")
            library.borrow_book(book_id, member_id)
        elif choice == "4":
            book_id = input("Enter Book ID to return: ")
            library.return_book(book_id)
        elif choice == "5":
            library.list_books()
        elif choice == "6":
            member_id = input("Enter Member ID: ")
            name = input("Enter Member Name: ")
            library.add_member(member_id, name)
        elif choice == "7":
            member_id = input("Enter Member ID to remove: ")
            library.remove_member(member_id)
        elif choice == "8":
            library.list_members()
        elif choice == "9":
            print("Exiting Library Management System.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
