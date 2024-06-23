import tkinter as tk

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book_id, title, author):
        if book_id not in self.books:
            self.books[book_id] = {"title": title, "author": author, "status": "available"}
            return f"Book '{title}' by {author} added successfully."
        else:
            return "Book with this ID already exists."

    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            return "Book removed successfully."
        else:
            return "Book not found."

    def borrow_book(self, book_id, member_id):
        if book_id in self.books:
            if self.books[book_id]["status"] == "available":
                if member_id in self.members:
                    self.books[book_id]["status"] = "borrowed"
                    self.books[book_id]["borrower"] = member_id
                    return f"Book '{self.books[book_id]['title']}' borrowed by Member {member_id}."
                else:
                    return "Member not found."
            else:
                return "Book is already borrowed."
        else:
            return "Book not found."

    def return_book(self, book_id):
        if book_id in self.books:
            if self.books[book_id]["status"] == "borrowed":
                member_id = self.books[book_id]["borrower"]
                self.books[book_id]["status"] = "available"
                del self.books[book_id]["borrower"]
                return f"Book '{self.books[book_id]['title']}' returned by Member {member_id}."
            else:
                return "This book is not borrowed."
        else:
            return "Book not found."

    def list_books(self):
        if self.books:
            output = "Available Books:\n"
            for book_id, book_info in self.books.items():
                if book_info["status"] == "available":
                    output += f"ID: {book_id}, Title: {book_info['title']}, Author: {book_info['author']}\n"
            return output
        else:
            return "No books available."

    def add_member(self, member_id, name):
        if member_id not in self.members:
            self.members[member_id] = {"name": name}
            return f"Member {name} added successfully."
        else:
            return "Member with this ID already exists."

    def remove_member(self, member_id):
        if member_id in self.members:
            del self.members[member_id]
            return "Member removed successfully."
        else:
            return "Member not found."

    def list_members(self):
        if self.members:
            output = "Library Members:\n"
            for member_id, member_info in self.members.items():
                output += f"ID: {member_id}, Name: {member_info['name']}\n"
            return output
        else:
            return "No members available."


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.library = Library()

    def create_widgets(self):
        self.book_id_label = tk.Label(self, text="Book ID:")
        self.book_id_label.pack(side="top")

        self.book_id_entry = tk.Entry(self)
        self.book_id_entry.pack(side="top")

        self.title_label = tk.Label(self, text="Title:")
        self.title_label.pack(side="top")

        self.title_entry = tk.Entry(self)
        self.title_entry.pack(side="top")

        self.author_label = tk.Label(self, text="Author:")
        self.author_label.pack(side="top")

        self.author_entry = tk.Entry(self)
        self.author_entry.pack(side="top")

        self.member_id_label = tk.Label(self, text="Member ID:")
        self.member_id_label.pack(side="top")

        self.member_id_entry = tk.Entry(self)
        self.member_id_entry.pack(side="top")

        self.name_label = tk.Label(self, text="Name:")
        self.name_label.pack(side="top")

        self.name_entry = tk.Entry(self)
        self.name_entry.pack(side="top")

        self.add_book_button = tk.Button(self)
        self.add_book_button["text"] = "Add Book"
        self.add_book_button["command"] = self.add_book
        self.add_book_button.pack(side="top")

        self.remove_book_button = tk.Button(self)
        self.remove_book_button["text"] = "Remove Book"
        self.remove_book_button["command"] = self.remove_book
        self.remove_book_button.pack(side="top")

        self.borrow_book_button = tk.Button(self)
        self.borrow_book_button["text"] = "Borrow Book"
        self.borrow_book_button["command"] = self.borrow_book
        self.borrow_book_button.pack(side="top")

        self.return_book_button = tk.Button(self)
        self.return_book_button["text"] = "Return Book"
        self.return_book_button["command"] = self.return_book
        self.return_book_button.pack(side="top")

        self.list_books_button = tk.Button(self)
        self.list_books_button["text"] = "List Books"
        self.list_books_button["command"] = self.list_books
        self.list_books_button.pack(side="top")

        self.add_member_button = tk.Button(self)
        self.add_member_button["text"] = "Add Member"
        self.add_member_button["command"] = self.add_member
        self.add_member_button.pack(side="top")

        self.remove_member_button = tk.Button(self)
        self.remove_member_button["text"] = "Remove Member"
        self.remove_member_button["command"] = self.remove_member
        self.remove_member_button.pack(side="top")

        self.list_members_button = tk.Button(self)
        self.list_members_button["text"] = "List Members"
        self.list_members_button["command"] = self.list_members
        self.list_members_button.pack(side="top")

        self.output_text = tk.Text(self)
        self.output_text.pack(side="bottom")

    def add_book(self):
        book_id = self.book_id_entry.get()
        title = self.title_entry.get()
        author = self.author_entry.get()
        output = self.library.add_book(book_id, title, author)
        self.output_text.insert("end", output + "\n")

    def remove_book(self):
        book_id = self.book_id_entry.get()
        output = self.library.remove_book(book_id)
        self.output_text.insert("end", output + "\n")

    def borrow_book(self):
        book_id = self.book_id_entry.get()
        member_id = self.member_id_entry.get()
        output = self.library.borrow_book(book_id, member_id)
        self.output_text.insert("end", output + "\n")

    def return_book(self):
        book_id = self.book_id_entry.get()
        output = self.library.return_book(book_id)
        self.output_text.insert("end", output + "\n")

    def list_books(self):
        output = self.library.list_books()
        self.output_text.insert("end", output + "\n")

    def add_member(self):
        member_id = self.member_id_entry.get()
        name = self.name_entry.get()
        output = self.library.add_member(member_id, name)
        self.output_text.insert("end", output + "\n")

    def remove_member(self):
        member_id = self.member_id_entry.get()
        output = self.library.remove_member(member_id)
        self.output_text.insert("end", output + "\n")

    def list_members(self):
        output = self.library.list_members()
        self.output_text.insert("end", output + "\n")


root = tk.Tk()
app = Application(master=root)
app.mainloop()
