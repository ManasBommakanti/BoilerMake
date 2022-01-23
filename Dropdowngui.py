import string
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import themed_tk as tk
import tkinter.scrolledtext
from mathplot import *

class Application(object):

    def __init__(self, master):
        self.master = master

        self.left = Frame(master, height=525, width=500, bg="#DFDEDE")
        self.left.place(x=0, y=0)

        self.right = Frame(master, height=525, width=500, bg="#E9E8E8")
        self.right.place(x=500, y=0)

        self.combobox1 = ttk.Combobox(self.left, textvariable="Algorithm", values=("United States", "India", "Russia", "China", "United Kingdom"),
                                      state='readonly', width=20)
        self.combobox1.place(x=190, y=80)


        self.combobox2 = ttk.Combobox(self.left, textvariable="Algorithm1", values=("1950", "1960", "1970", "1980", "1990", "2010", "2020"),
                                      state='readonly', width=20)
        self.combobox2.place(x=190, y=140)

        self.button1 = ttk.Button(self.left, text="Show Data", width=20, command=self.submit)
        self.button1.place(x=200, y=200)



    def submit(self):

        country = self.combobox1.get()
        year = self.combobox2.get()

        f(country, year)
        return

def main():

    root = tk.ThemedTk()
    root.get_themes()
    root.set_theme("elegance")
    root.title("CRYPTOGRAPHY")
    root.geometry("500x300+500+200")
    app = Application(root)
    root.resizable(False, False)
    root.mainloop()

if __name__ == "__main__":
    main()