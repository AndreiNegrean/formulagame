import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import pathlib, os


class Home(ttk.Frame):
    def __init__(self, container, show_play, exit_app, **kwargs, ):
        super().__init__(container, **kwargs)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        home_buttons_frame = ttk.Frame(self)
        home_buttons_frame.columnconfigure(0, minsize=430)
        home_buttons_frame.rowconfigure(0, minsize=240)
        home_buttons_frame.rowconfigure(1, minsize=240)
        home_buttons_frame.grid(row=0, column=0, sticky='E')

        home_image_frame = ttk.Frame(self)
        home_image_frame.columnconfigure(0, minsize=850)
        home_image_frame.rowconfigure(0, minsize=480)
        home_image_frame.grid(row=0, column=0, sticky='W')

        path = pathlib.Path(__file__).parent.resolve()
        self.home_image = Image.open(f"{path}\driver_pilot_bg.png")
        self.home_bg_image = ImageTk.PhotoImage(self.home_image)

        self.image_label = ttk.Label(home_image_frame, image=self.home_bg_image)
        self.image_label.image = self.home_bg_image
        self.image_label.pack()
        self.play_button = ttk.Button(home_buttons_frame, text="PLAY", style='Menu.TButton', command=show_play)
        self.play_button.grid(row=0, column=0, sticky='NSEW')
        self.exit_button = ttk.Button(home_buttons_frame, text='EXIT', style='Menu.TButton', command=exit_app)
        self.exit_button.grid(row=1, column=0, sticky='NSEW')
