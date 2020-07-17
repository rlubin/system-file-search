from pathlib import Path
from tkinter import *
import re
import os

# def find_matches(path, matches, regex):
#     """recursive function that crawls through directories and appends filenames to matches array that match the regular expression"""
#     for x in os.listdir(path):
#         p = os.path.join(path, x)
#         if os.path.isdir(p):
#             try:
#                 a = find_matches(p, matches, regex)
#                 paths.extend(a)
#             except:
#                 pass
#         if os.path.isfile(p):
#             if re.search(regex, x):
#                 matches.append(path + '\\' + x)

# def system_search(matches, regex):
#     """populate matches array with regex filename matches"""
#     root_dir = Path.home().parts[0]
#     p = Path('.')
#     p = p.resolve()
#     find_matches(root_dir, matches, regex)

def find_matches2(path, listbox, regex):
    """recursive function that crawls through directories and appends filenames to listbox that match the regular expression"""
    for x in os.listdir(path):
        p = os.path.join(path, x)
        if os.path.isdir(p):
            try:
                a = find_matches2(p, listbox, regex)
                paths.extend(a)
            except:
                pass
        if os.path.isfile(p):
            if re.search(regex, x):
                print(path + '\\' + x)
                listbox.insert(END, path + '\\' + x)
                listbox.config()

def system_search2(listbox, regex):
    """populate listbox with filename matches"""
    root_dir = Path.home().parts[0]
    p = Path('.')
    p = p.resolve()
    find_matches2(root_dir, listbox, regex)

def search_button():
    """handle search button click, open new window displaying matches"""
    regex = entry.get()
    match_window = Toplevel(root)
    match_window.title(regex)
    match_window.geometry('500x500')
    listbox = Listbox(match_window, selectmode=EXTENDED)
    
    # matches = []
    # system_search(matches, regex)
    # system_search2(listbox, regex)
    matches_label = Label(match_window, text='Matches: ')
    count_label = Label(match_window, text=listbox.size())

    matches_label.pack(side=TOP, anchor=NW)
    count_label.pack(side=TOP, anchor=NW)

    y_scrollbar = Scrollbar(match_window)
    y_scrollbar.pack(side=RIGHT, fill=Y)
    listbox.config(yscrollcommand=y_scrollbar.set)
    y_scrollbar.config(command=listbox.yview)

    x_scrollbar = Scrollbar(match_window, orient=HORIZONTAL)
    x_scrollbar.pack(side=BOTTOM, fill=X)
    listbox.config(xscrollcommand=x_scrollbar.set)
    x_scrollbar.config(command=listbox.xview)

    listbox.pack(side=LEFT, expand=True, fill=BOTH)

    system_search2(listbox, regex)

def hit_enter(event):
    """allow the search button to be activated with enter key"""
    search_button()

root = Tk()
root.title('System File Search')
root.geometry('300x30')
root.resizable(False, False)

root.bind('<Return>', hit_enter)

label = Label(root, text='Filename')
entry = Entry(root, width=32)
button = Button(root, text='Search', command=search_button)

label.pack(side=LEFT)
entry.pack(side=LEFT)
button.pack(side=LEFT)

root.mainloop()