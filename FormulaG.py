import tkinter as tk
from home import Home
from play import Play
from tkinter import ttk
import pathlib, os

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

class Formula(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        style = ttk.Style()
        style.theme_use('clam')

        style.configure('Play.TFrame', background="white")
        style.configure('Menu.TButton',
                        background='#212121',
                        foreground='white',
                        font=('Helvetica', 15, 'bold')
                        )
        style.map('Menu.TButton',
                  background=[('active', '#af3a3a')])

        style.configure('Specs_title.TLabel', font=('Helvetica', 13, 'bold'), background='white')

        style.configure('Specs.TLabel', font=('Helvetica', 11), background='white')

        style.configure('Drivers_list.TLabel', font=('Helvetica', 9), background='white', foreground='black')
        style.map('Drivers_list.TLabel',
                  background=[('active', '#212121'), ('selected', '#212121'), ('!active', 'white')],
                  foreground=[('active', 'white'), ('selected', 'white'), ('!active', 'black')])

        style.configure('Score.TLabel', font=('Helvetica', 9, 'bold'), background='white')

        style.configure('Correct.TLabel', font=('Helvetica', 11), background='white', foreground='green')
        style.configure('Wrong.TLabel', font=('Helvetica', 11), background='white', foreground='red')

        style.configure('Play_button.TButton', font=('Helvetica', 11), background='#212121', foreground='white')
        style.map('Play_button.TButton',
                  background=[('active', '#af3a3a'), ('disabled', 'light gray')],
                  foreground=[('active', 'white'), ('disabled', 'gray')])

        self.title(' Guess the F1 Driver')
        self.geometry('1280x480')
        self.resizable(False, False)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        path = pathlib.Path(__file__).parent.resolve()
        icon_photo = tk.PhotoImage(file=f'{path}\windowimg.png')
        self.iconphoto(False, icon_photo)

        self.frames = {}

        self.home_frame = Home(self, lambda: self.show_frame(Play), lambda: self.exit_app())
        self.play_frame = Play(self)

        self.frames[Home] = self.home_frame
        self.frames[Play] = self.play_frame

        self.home_frame.grid(row=0, column=0, sticky='NSEW')
        self.play_frame.grid(row=0, column=0, sticky='NSEW')

        self.show_frame(Home)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()

    def exit_app(self):
        self.destroy()
        exit()

if __name__ == '__main__':
    root = Formula()
    root.mainloop()
