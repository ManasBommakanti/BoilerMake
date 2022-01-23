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

        self.left = Frame(master, height=525, width=500, bg="#FFD28E")
        self.left.place(x=0, y=0)

        self.right = Frame(master, height=525, width=500, bg="#FFD28E")
        self.right.place(x=500, y=0)

        self.combobox1 = ttk.Combobox(self.left, textvariable="Algorithm",
                                      values=("United States", "India", "Russia", "China", "United Kingdom"),
                                      state='readonly', width=20)
        self.combobox1.current(0)
        self.combobox1.place(x=180, y=80)

        self.combobox2 = ttk.Combobox(self.left, textvariable="Algorithm1",
                                      values=("1950", "1960", "1970", "1980", "1990", "2010", "2020"),
                                      state='readonly', width=20)
        self.combobox2.current(0)
        self.combobox2.place(x=180, y=140)

        self.button1 = ttk.Button(self.left, text="Show Data", width=15, command=self.submit)
        self.button1.place(x=200, y=200)

        # self.text1 = ttk.Label(self.left, text="United States Stage: 1")

    def submit(self):
        country = self.combobox1.get()
        year = self.combobox2.get()

        # self.text1.place(x=200, y=250)

        stage = f(country, year)
        # print(stage)
        return


def main():
    root = tk.ThemedTk()
    root.get_themes()
    root.set_theme("arc")
    root.title("POPULATION PYRAMID VISUALIZER")
    root.geometry("500x300+50+200")
    app = Application(root)
    root.resizable(False, False)
    root.mainloop()


if __name__ == "__main__":
    main()
