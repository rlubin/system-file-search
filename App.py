import tkinter as tk
import search

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.button = tk.Button(self)
        self.button['text'] = 'Search'
        self.button['command'] = self.search_button
        self.button.pack(side='bottom')

        self.label = tk.Label(self)
        self.label['text'] = 'Filename'
        self.label.pack(side='left')

        self.entry = tk.Entry(self, bd = 5)
        self.entry.pack(side='right')

    def search_button(self):
        matches = []
        regex_exp = self.entry.get()
        match_window = tk.Toplevel(self)
        match_window.title(regex_exp)
        match_window.geometry("500x1000")
        tk.Label(match_window, text =matches).pack()
        search.system_search(matches, regex_exp)

root = tk.Tk()
root.geometry("350x50")
root.title("System File Search")
app = App(master=root)
app.mainloop()