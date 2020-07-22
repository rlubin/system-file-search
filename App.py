from pathlib import Path
from tkinter import *
import re
import os
import subprocess
import time

class App():
    def __init__(self):
        """window setup"""
        self.root = Tk()
        self.root.title('System File Search')
        self.root.geometry('500x500')
        self.root.minsize(300, 225)
        self.root.bind('<Return>', self.enter_hit)

        self.search_frame = Frame(self.root, height=7)
        self.label = Label(self.search_frame, text='Filename')
        self.entry = Entry(self.search_frame)
        self.button = Button(self.search_frame, text='Search', command=self.search_button)
        self.label.pack(side=LEFT)
        self.entry.pack(side=LEFT, expand=True, fill=X)
        self.button.pack(side=LEFT)
        self.search_frame.pack(fill=X)

        self.result_frame = Frame(self.root)
        self.listbox = Listbox(self.result_frame, selectmode=EXTENDED)
        self.listbox.bind('<Double-Button-1>', self.double_click)
        self.count_frame = Frame(self.result_frame, height=7)
        self.counter = IntVar()
        self.counter.set(0)
        self.status = StringVar()
        self.matches_label = Label(self.count_frame, text='Matches: ')
        self.count_label = Label(self.count_frame, textvariable=self.counter)
        self.search_status = Label(self.count_frame, textvariable=self.status)
        self.matches_label.pack(side=LEFT)
        self.count_label.pack(side=LEFT)
        self.search_status.pack(side=RIGHT)
        self.count_frame.pack(fill=X)
        self.y_scrollbar = Scrollbar(self.result_frame)
        self.y_scrollbar.pack(side=RIGHT, fill=Y)
        self.listbox.config(yscrollcommand=self.y_scrollbar.set)
        self.y_scrollbar.config(command=self.listbox.yview)
        self.x_scrollbar = Scrollbar(self.result_frame, orient=HORIZONTAL)
        self.x_scrollbar.pack(side=BOTTOM, fill=X)
        self.listbox.config(xscrollcommand=self.x_scrollbar.set)
        self.x_scrollbar.config(command=self.listbox.xview)
        self.listbox.pack(side=LEFT, expand=True, fill=BOTH)
        self.result_frame.pack(expand=True, fill=BOTH)

        self.root.mainloop()

    def find_matches(self, path, regex):
        """recursive function that crawls through directories and updates filenames to listbox that match the regular expression"""
        for x in os.listdir(path):
            p = os.path.join(path, x)
            if os.path.isdir(p):
                try:
                    a = self.find_matches(p, regex)
                    paths.extend(a)
                except:
                    pass
            if os.path.isfile(p):
                if re.search(regex, x):
                    self.listbox.insert(END, path + '\\' + x)
                    update_counter = self.counter.get() + 1
                    self.counter.set(update_counter)
                    self.listbox.update()
                    self.counter.update()

    def search_button(self):
        """handle search button click"""
        regex = self.entry.get()
        root_dir = Path.home().parts[0]
        self.status.set('Search in progress...')
        self.find_matches(root_dir, regex)
        self.status.set('Search complete')

    def enter_hit(self, event):
        """allow the search button to be activated with enter key"""
        self.search_button()

    def double_click(self, event):
        """opens file explorer to current single selection"""
        filepath = self.listbox.get(self.listbox.curselection())
        loc = Path(filepath)
        folder = os.path.dirname(loc)
        subprocess.Popen(f'explorer /select, "{loc}"')

app = App()