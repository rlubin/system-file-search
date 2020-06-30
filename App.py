import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.button = tk.Button(self)
        self.button['text'] = 'Search'
        self.button['command'] = self.say_hi
        self.button.pack(side='bottom')

        self.label = tk.Label(self)
        self.label['text'] = 'Filename'
        self.label.pack(side='left')

        self.entry = tk.Entry(self, bd = 5)
        self.entry.pack(side='right')

    def say_hi(self):
        print(self.entry.get())

root = tk.Tk()
app = App(master=root)
app.mainloop()