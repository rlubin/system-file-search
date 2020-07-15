import tkinter as tk
import search

def search_button():
    regex = entry.get()
    match_window = tk.Toplevel(root)
    match_window.title(regex)
    match_window.geometry("500x500")
    lb = tk.Listbox(match_window)
    lb.pack()
    matches = []
    search.system_search(matches, regex)
    # match_num = f'Matches: {len(matches)}'
    # label = tk.Label(match_window, textvariable=match_num)
    # label.pack()
    for item in matches:
        lb.insert(tk.END, item)

root = tk.Tk()
root.title("System File Search")
root.grid()

label = tk.Label(root, text='Filename')
entry = tk.Entry(root)
button = tk.Button(root, text='Search', command=search_button)

label.grid(row=0, column=0)
entry.grid(row=0, column=1)
button.grid(row=1, column=0, columnspan=2)

root.mainloop()