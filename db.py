import sqlite3 as sql
from sqlite3 import Error
from tkinter import messagebox


class database:

    def __init__(self, book_id):
        self.book_id = book_id
    
    def connect_to_db(self):

        try:
            self.connection = sql.connect("Library.db")
            self.cur = self.connection.cursor()
            self.cur.execute('''CREATE TABLE library (book_id INTEGER PRIMARY KEY, book_title TEXT, book_author TEXT, book_status TEXT)''')
        
        except Error:
            pass

    def add_book(self, book_title, book_author, book_status):
        try:
            self.cur.execute("INSERT INTO library VALUES (?, ?, ?, ?)", (self.book_id, book_title, book_author, book_status))

        except Error:
            messagebox.showerror("Error!", "A book with same ID have already been added.\nTry entring different ID.")

        else:
            self.connection.commit()
            self.connection.close()
            messagebox.showinfo("Success!", "Successfully added the book.")

    def entries(self):
        return list(self.cur.execute("SELECT * FROM library"))
            
    def delete_book(self):
        self.cur.execute("DELETE FROM library WHERE book_id=?", (self.book_id, ))
        self.connection.commit()
        self.connection.close()
        messagebox.showinfo("Success", "Successfully deleted the book.")

    def issue_book(self):
        self.cur.execute('''UPDATE library
                            SET book_status = ?
                            WHERE book_id = ?''', ("Issued", self.book_id))
        
        self.connection.commit()
        self.connection.close()
        messagebox.showinfo("Success", "Successfully issued the book.")

    def return_book(self):
        self.cur.execute('''UPDATE library
                            SET book_status = ?
                            WHERE book_id = ?''', ("Available", self.book_id))
        
        self.connection.commit()
        self.connection.close()
        messagebox.showinfo("Success", "Successfully returned the book.")

    def book_exists(self):
        list_of_book = list(self.cur.execute("SELECT * FROM library WHERE book_id=?", (self.book_id, )))
        if len(list_of_book) == 0: messagebox.showerror("Error!", "No book exist with that ID.")
        else: return True

    def book_available_to_issue(self):
        book = list(self.cur.execute("SELECT * FROM library WHERE book_id=?", (self.book_id, )))
        ele = [d for _, _, _, d in book]
        if ele[0] == "Available": return True
        else: messagebox.showerror("Error!", "Book already issued")

    def book_issued_to_return(self):
        book = list(self.cur.execute("SELECT * FROM library WHERE book_id=?", (self.book_id, )))
        ele = [d for _, _, _, d in book]
        if ele[0] == "Issued": return True
        else: messagebox.showerror("Error!", "That book was returned.")