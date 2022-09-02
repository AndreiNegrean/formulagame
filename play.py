import time
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
from drivers import *
import random

class Play(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)


        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        play_image_frame = ttk.Frame(self, style='Play.TFrame')
        play_image_frame.columnconfigure(0, minsize=250)
        play_image_frame.columnconfigure(1, minsize=170)
        play_image_frame.columnconfigure(2, minsize=170)
        play_image_frame.columnconfigure(3, minsize=100)
        play_image_frame.columnconfigure(4, minsize=400)

        for i in range(0,12):
            play_image_frame.rowconfigure(i, minsize=40)


        play_image_frame.grid(row=0, column=0, sticky='NSEW')

        self.nationality_title_label = ttk.Label(play_image_frame, text = 'Nationality', style='Specs_title.TLabel')
        self.nationality_title_label.grid(row=2, column=0, sticky='W', padx=30)
        self.number_title_label = ttk.Label(play_image_frame, text='Number', style='Specs_title.TLabel')
        self.number_title_label.grid(row=5, column=0, sticky='W', padx=30)
        self.team_title_label = ttk.Label(play_image_frame, text='Team', style='Specs_title.TLabel')
        self.team_title_label.grid(row=8, column=0, sticky='W', padx=30)

        path = pathlib.Path(__file__).parent.resolve()

        drivers_list = init_drivers()

        def default_image():
            self.play_image = Image.open(f"{path}/driver_play_frame.png")
            self.play_bg_image = ImageTk.PhotoImage(self.play_image)

            self.image_label_about = ttk.Label(play_image_frame, image=self.play_bg_image, background='white')
            self.image_label_about.image = self.play_bg_image
            self.image_label_about.grid(row=0, column=4, rowspan=12, sticky='NSW', pady=60)

        def driver_image_update():
            self.image_label_about.grid_forget()
            self.driver_image = Image.open(f'{path}/drivers/{self.name}_image.jpg')
            self.driver_bg_image = ImageTk.PhotoImage(self.driver_image)

            self.driver_image_label = ttk.Label(play_image_frame, image=self.driver_bg_image, background='white')
            self.driver_image_label.image = self.driver_bg_image
            self.driver_image_label.grid(row=0, column=4, rowspan=12, sticky='NSW', pady=60)

        self.score_value = tk.StringVar(value=0)
        def score_update():
            score = int(self.score_value.get())
            if self.guess.get() == self.number:
                self.score_value.set(score+1)

        def check_if_gameover():
            if len(self.indexes) == 0:

                self.guess.set(None)
                self.score_label['text'] = 'Game is over! Your score is:'

                self.check_button.grid_forget()
                self.next_button.grid_forget()
                self.stage_label.grid_forget()

                self.new_game_button = ttk.Button(play_image_frame, text='New Game', command=reset_game, width=15, style='Play_button.TButton')
                self.new_game_button.grid(row=5, column=3, rowspan=4, sticky='NSEW', padx=30)

                self.exit_button = ttk.Button(play_image_frame, text='Exit', command=exit, width=15, style='Play_button.TButton')
                self.exit_button.grid(row=9, column=3, rowspan=2, sticky='NSEW', padx=30)

        def update_check_button():
            self.check_button['state'] = 'normal'

        def check_answear():

            if self.guess.get() == self.number:
                self.check_label_text.set('Correct')
                self.check_label = ttk.Label(play_image_frame, textvariable=self.check_label_text, style='Correct.TLabel')
                self.check_label.grid(row=3, column=3, rowspan=2, sticky='NS')
                self.image_label_about['image'] = None
                driver_image_update()
                score_update()
                self.check_button['state'] = 'disabled'
                self.next_button['state'] = 'normal'
                check_if_gameover()
            else:
                self.check_label_text.set('Wrong')
                self.check_label = ttk.Label(play_image_frame, textvariable=self.check_label_text, style='Wrong.TLabel')
                self.check_label.grid(row=3, column=3, rowspan=2, sticky='NS')
                score_update()
                self.check_button['state'] = 'disabled'
                self.next_button['state'] = 'normal'
                check_if_gameover()

        self.guess = tk.StringVar()
        self.check_label_text = tk.StringVar()
        self.check_label_text.set('')

        for i in range(0,10):

            self.radio = ttk.Radiobutton(play_image_frame,
                                    text=drivers_list[i].name,
                                    value=drivers_list[i].number,
                                    variable=self.guess,
                                    command=update_check_button,
                                    style='Drivers_list.TLabel'
                                    )
            self.radio.grid(row=i+1, column=1, sticky='NS', padx=10)

        for i in range(10,20):

            self.radio_two = ttk.Radiobutton(play_image_frame,
                                        text=drivers_list[i].name,
                                        value=drivers_list[i].number,
                                        variable=self.guess,
                                        command=update_check_button,
                                        style='Drivers_list.TLabel',
                                        )
            self.radio_two.grid(row=i+1-10, column=2, sticky='NS', padx=10)

        self.indexes = random.sample(range(0, 20), 10)

        def show_specs():

            i = self.indexes.pop()

            self.nationality = drivers_list[i].nationality
            self.number = drivers_list[i].number
            self.team = drivers_list[i].team
            self.name = drivers_list[i].name

            self.nationality_label = ttk.Label(play_image_frame, text = self.nationality, style='Specs.TLabel')
            self.nationality_label.grid(row=3, column=0, sticky='W', padx=30)
            self.number_label = ttk.Label(play_image_frame, text=self.number, style='Specs.TLabel')
            self.number_label.grid(row=6, column=0, sticky='W', padx=30)
            self.team_label = ttk.Label(play_image_frame, text=self.team, style='Specs.TLabel')
            self.team_label.grid(row=9, column=0, sticky='W', padx=30)

            show_stage()

            return self.number

        def update_specs():
            self.nationality_label.grid_forget()
            self.number_label.grid_forget()
            self.team_label.grid_forget()
            self.check_label_text.set('')
            try:
                self.driver_image_label.grid_forget()
            except:
                pass
            default_image()
            self.check_button['state'] = 'disabled'
            self.next_button['state'] = 'disabled'
            self.guess.set(None)  #Deselect radiobuttons
            self.stage_label.grid_forget()
            stg = int(self.stage.get())
            self.stage.set(stg + 1)

            show_specs()

        self.stage = tk.StringVar(value=1)
        def show_stage():
            self.stage_label_title = ttk.Label(play_image_frame, text='Stage:', style='Drivers_list.TLabel', width=14)
            self.stage_label_title.grid(row=0, column=0, rowspan=2)
            self.stage_label = ttk.Label(play_image_frame, textvariable=self.stage, style='Drivers_list.TLabel')
            self.stage_label.grid(row=0, column=0, rowspan=2, sticky='NS')

        def reset_game():
            self.nationality_label.grid_forget()
            self.number_label.grid_forget()
            self.team_label.grid_forget()
            self.check_button.grid(row=5, column=3, rowspan=4, sticky='NSEW', padx=30)
            self.next_button.grid(row=9, column=3, rowspan=2, sticky='NSEW', padx=30)
            self.new_game_button.grid_forget()
            self.exit_button.grid_forget()
            self.indexes = random.sample(range(0, 20), 10)

            self.check_button['state'] = 'normal'
            self.next_button['state'] = 'disabled'
            self.check_button['state'] = 'disabled'

            self.score_label['text'] = 'Your score is:'
            self.score_value = tk.StringVar(value=0)
            self.score_display['textvariable'] = self.score_value

            self.stage = tk.StringVar(value=1)
            self.stage_label['textvariable'] = self.stage

            self.check_label_text.set('')
            self.check_label['textvariable'] = self.check_label_text

            default_image()
            show_specs()


        self.score_label = ttk.Label(play_image_frame, text='Score is:', style='Score.TLabel')
        self.score_label.grid(row=1, column=3, sticky='NS')
        self.score_display = ttk.Label(play_image_frame, textvariable=self.score_value, style='Specs_title.TLabel')
        self.score_display.grid(row=2, column=3, stick='NS')

        self.check_button = ttk.Button(play_image_frame, text='Check', command=check_answear, width=15, style='Play_button.TButton')
        self.check_button.grid(row=5, column=3, rowspan=4, sticky='NSEW', padx=30)

        self.next_button = ttk.Button(play_image_frame, text='Next', command=update_specs, width=15, style='Play_button.TButton')
        self.next_button.grid(row=9, column=3, rowspan=2, sticky='NSEW', padx=30)

        self.check_button['state'] = 'disabled'
        self.next_button['state'] = 'disabled'

        show_specs()
        default_image()


