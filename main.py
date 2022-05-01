import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from db import database
from tkinter import ttk



class Library:
    width = 0
    height = 0
    winPos = []


    def __init__(self, master):
        self.master = master

        self.bg = Image.open("images\\books.jpg")
        self.bg = ImageTk.PhotoImage(self.bg)
        self.width = self.bg.width()
        self.height = int(self.bg.height() / 1.3)

        self.cavas = tk.Canvas(self.master, width=self.width, height=self.height)
        self.cavas.pack(fill=tk.BOTH, expand=True)
        self.cavas.create_image(0, 0, image=self.bg, anchor="nw")

        self.home()
        self.center_window()


    def home(self):
        self.headingFrame = tk.Frame(self.master, bg="lightpink", bd=5)
        self.headingFrame.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
        self.headingLabel = tk.Label(self.headingFrame, text="Welcome to \n Falconic's Library", bg='black', fg='white', font=('Courier',25))
        self.headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

        self.add_book_btn = tk.Button(self.master ,text="Add Book Details", bg='lightpink', fg='black', font=('Merriweather',12), command=self.add_book)
        self.add_book_btn.place(relx=0.30 ,rely=0.3, relwidth=0.40, relheight=0.1)
            
        self.delete_book_btn = tk.Button(self.master,text="Delete Book", bg='lightpink', fg='black', font=('Merriweather',12), command=self.delete_book)
        self.delete_book_btn.place(relx=0.30,rely=0.4, relwidth=0.40, relheight=0.1)
            
        self.view_book_btn = tk.Button(self.master,text="View Book List", bg='lightpink', fg='black', font=('Merriweather',12), command=self.view_book)
        self.view_book_btn.place(relx=0.30,rely=0.5, relwidth=0.40, relheight=0.1)
            
        self.issue_book_btn = tk.Button(self.master,text="Issue Book to Student", bg='lightpink', fg='black', font=('Merriweather',12), command=self.issue_book)
        self.issue_book_btn.place(relx=0.30,rely=0.6, relwidth=0.40, relheight=0.1)
            
        self.return_book_btn = tk.Button(self.master,text="Return Book", bg='lightpink', fg='black', font=('Merriweather',12), command=self.return_book)
        self.return_book_btn.place(relx=0.30, rely=0.7, relwidth=0.40, relheight=0.1)

    def add_book(self):
        self.delete_elements()

        self.headingLabel["text"] = "Add Book"

        self.frame = tk.Frame(self.master, bg="lightpink")
        self.frame.place(relx=0.2,rely=0.4, relwidth=0.6, relheight=0.4)

        # Book Id    
        self.lbl_book_id = tk.Label(self.frame, text="Book ID", bg='lightpink', fg='black', font=('Merriweather',12))
        self.lbl_book_id.place(relx=0.05, rely=0.2, relheight=0.08)
            
        self.ent_book_id = tk.Entry(self.frame, font=('Merriweather', 11))
        self.ent_book_id.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)
            
        # Title
        self.lbl_book_title = tk.Label(self.frame, text="Title", bg='lightpink', fg='black', font=('Merriweather',12))
        self.lbl_book_title.place(relx=0.05, rely=0.35, relheight=0.08)
            
        self.ent_book_title = tk.Entry(self.frame, font=('Merriweather', 11))
        self.ent_book_title.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
            
        # Book Author
        self.lbl_book_author = tk.Label(self.frame,text="Author", bg='lightpink', fg='black', font=('Merriweather',12))
        self.lbl_book_author.place(relx=0.05, rely=0.50, relheight=0.08)
            
        self.ent_book_author = tk.Entry(self.frame, font=('Merriweather', 11))
        self.ent_book_author.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)
            
        # Book Status
        self.lbl_book_status = tk.Label(self.frame, text="Status(Available/issued)", bg='lightpink', fg='black', font=('Merriweather',12))
        self.lbl_book_status.place(relx=0.05, rely=0.65, relheight=0.08)
            
        self.ent_book_status = tk.Entry(self.frame, font=('Merriweather', 11))

        self.ent_book_status.place(relx=0.3, rely=0.65, relwidth=0.62, relheight=0.08)
        self.ent_book_status.insert(0, "Available")

        #Submit Button
        self.SubmitBtn = tk.Button(self.frame, text="SUBMIT", bg='black', fg='white', command=self.add_book_to_db)
        self.SubmitBtn.place(relx=0.30, rely=0.82, relwidth=0.16, relheight=0.1)
        
        # Quit Button
        self.quitBtn = tk.Button(self.frame, text="QUIT", bg="black", fg="white", command=self.return_home)
        self.quitBtn.place(relx=0.53, rely=0.82, relwidth=0.16, relheight=0.1)

    def add_book_to_db(self):
        book_id = self.ent_book_id.get()
        book_title = self.ent_book_title.get()
        book_author = self.ent_book_author.get()
        book_status = self.ent_book_status.get()

        if self.check_entries((book_id, book_title, book_author, book_status)) and self.check_id_field(book_id):

            db = database(book_id)
            db.connect_to_db()
            db.add_book(book_title, book_author, book_status)

            self.ent_book_id.delete(0, tk.END)
            self.ent_book_title.delete(0, tk.END)
            self.ent_book_author.delete(0, tk.END)

    def return_home(self):
        self.frame.destroy()
        self.home()

    def delete_elements(self):
        self.add_book_btn.destroy()
        self.delete_book_btn.destroy()
        self.view_book_btn.destroy()
        self.issue_book_btn.destroy()
        self.return_book_btn.destroy()

    def delete_book(self):
        self.delete_elements()
        self.headingLabel["text"] = "Delete Book"

        self.frame = tk.Frame(self.master, bg="lightpink")
        self.frame.place(relx=0.2,rely=0.4, relwidth=0.6, relheight=0.3)

        # Book Id    
        self.lbl_book_id = tk.Label(self.frame, text="Book ID", bg='lightpink', fg='black', font=('Merriweather',12))
        self.lbl_book_id.place(relx=0.05, rely=0.2, relheight=0.08)
            
        self.ent_book_id = tk.Entry(self.frame, font=('Merriweather', 11))
        self.ent_book_id.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

        # Submit Button
        self.SubmitBtn = tk.Button(self.frame, text="SUBMIT", bg='black', fg='white', command=self.delete_book_from_db)
        self.SubmitBtn.place(relx=0.30, rely=0.82, relwidth=0.16, relheight=0.1)
        
        # Quit Button
        self.quitBtn = tk.Button(self.frame, text="QUIT", bg="black", fg="white", command=self.return_home)
        self.quitBtn.place(relx=0.53, rely=0.82, relwidth=0.16, relheight=0.1)

    def delete_book_from_db(self):
        book_id = self.ent_book_id.get()

        db = database(book_id)
        db.connect_to_db()

        if self.check_entries((book_id, )) and self.check_id_field(book_id) and db.book_exists():
            db.delete_book()

    def view_book(self):
        self.delete_elements()

        self.headingLabel["text"] = "View Books"

        self.frame = tk.Frame(self.master, bg="lightpink")
        self.frame.place(relx=0.2, rely=0.3, relwidth=0.6, relheight=0.6)

        db = database(None)
        db.connect_to_db()

        tree = ttk.Treeview(self.frame, column=("c1", "c2", "c3", "c4"), show='headings')

        for row in db.entries():
            tree.insert("", tk.END, values=row)
        
        tree.column("#1", anchor=tk.NW)
        tree.heading("#1", text="BOOK ID", anchor=tk.NW)

        tree.column("#2", anchor=tk.NW)
        tree.heading("#2", text="BOOK TITLE", anchor=tk.NW)

        tree.column("#3", anchor=tk.NW)
        tree.heading("#3", text="BOOK AUTHOR", anchor=tk.NW)

        tree.column("#4", anchor=tk.NW)
        tree.heading("#4", text="BOOK STATUS", anchor=tk.NW)

        tree.place(rely=0.05, relheight=0.85)

        self.quitBtn = tk.Button(self.frame, text="BACK", bg="black", fg="white", command=self.return_home)
        self.quitBtn.place(relx=0.75, rely=0.92, relwidth=0.16, relheight=0.05)

    def issue_book(self):
        self.delete_elements()
        self.headingLabel["text"] = "Issue Book"

        self.frame = tk.Frame(self.master, bg="lightpink")
        self.frame.place(relx=0.2,rely=0.4, relwidth=0.6, relheight=0.3)

        # Book Id    
        self.lbl_book_id = tk.Label(self.frame, text="Book ID", bg='lightpink', fg='black', font=('Merriweather',12))
        self.lbl_book_id.place(relx=0.05, rely=0.2, relheight=0.08)
            
        self.ent_book_id = tk.Entry(self.frame, font=('Merriweather', 11))
        self.ent_book_id.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

        # Submit Button
        self.SubmitBtn = tk.Button(self.frame, text="SUBMIT", bg='black', fg='white', command=self.issue_book_from_db)
        self.SubmitBtn.place(relx=0.30, rely=0.82, relwidth=0.16, relheight=0.1)
        
        # Quit Button
        self.quitBtn = tk.Button(self.frame, text="QUIT", bg="black", fg="white", command=self.return_home)
        self.quitBtn.place(relx=0.53, rely=0.82, relwidth=0.16, relheight=0.1)

    def issue_book_from_db(self):
        book_id = self.ent_book_id.get()
        db = database(book_id)
        db.connect_to_db()

        if self.check_entries((book_id, )) and self.check_id_field(book_id) and db.book_exists() and db.book_available_to_issue():
            db.issue_book()

    def return_book(self):
        self.delete_elements()
        self.headingLabel["text"] = "Return Book"

        self.frame = tk.Frame(self.master, bg="lightpink")
        self.frame.place(relx=0.2,rely=0.4, relwidth=0.6, relheight=0.3)

        # Book Id    
        self.lbl_book_id = tk.Label(self.frame, text="Book ID", bg='lightpink', fg='black', font=('Merriweather',12))
        self.lbl_book_id.place(relx=0.05, rely=0.2, relheight=0.08)
            
        self.ent_book_id = tk.Entry(self.frame, font=('Merriweather', 11))
        self.ent_book_id.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

        # Submit Button
        self.SubmitBtn = tk.Button(self.frame, text="SUBMIT", bg='black', fg='white', command=self.return_book_to_db)
        self.SubmitBtn.place(relx=0.30, rely=0.82, relwidth=0.16, relheight=0.1)
        
        # Quit Button
        self.quitBtn = tk.Button(self.frame, text="QUIT", bg="black", fg="white", command=self.return_home)
        self.quitBtn.place(relx=0.53, rely=0.82, relwidth=0.16, relheight=0.1)

    def return_book_to_db(self):
        book_id = self.ent_book_id.get()
        db = database(book_id)
        db.connect_to_db()

        if self.check_entries((book_id, )) and self.check_id_field(book_id) and db.book_exists() and db.book_issued_to_return():
            db.return_book()

    def check_entries(self, entries):
        if "" in entries:
            messagebox.showerror("Error!", "Don't leave any field empty.\nPlease provide all the reqired information to procced.")

        else: return True

    def check_id_field(self, id_field):
        try:
            int(id_field)

        except ValueError:
            messagebox.showerror("Error!", "The BOOK ID must be an INTEGER.")

        else:
            return True

    def center_window(self):
        screenWidth = self.cavas.winfo_screenwidth()
        screenHeight = self.cavas.winfo_screenheight()
        posTop = int(screenHeight/2 - self.height/2)
        posLeft = int(screenWidth/2 - self.width/2)
        self.winPos.append(posTop)
        self.winPos.append(posLeft)



if __name__ == "__main__":
    win = tk.Tk()
    win.title("Library")
    lib = Library(win)
    win.geometry(f"{lib.width}x{lib.height}+{lib.winPos[0]}+{lib.winPos[1]}")
    win.resizable(width=False, height=False)
    win.mainloop()
