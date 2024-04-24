import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import font
from tkinter import *
from ttkbootstrap import Style

window = ttk.Window(themename='solar')
window.title("ClashPedia")

options_frame = tk.Frame(window, bg='#c3c3c3')
options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(height='800' , width='175')

main_frame = tk.Frame(window)
main_frame.pack(side=LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height='1000' ,width='1750')

def hide_switch_page():
    welcome_switch_page.config(bg='#c3c3c3')
    categories_switch_page.config(bg='#c3c3c3')
    avg_elixir_cal_switch_page.config(bg='#c3c3c3')
    deck_builder_switch_page.config(bg='#c3c3c3')


def delete_page():
    for frame in main_frame.winfo_children():
        frame.destroy()


def switch_page(lb ,page):
    hide_switch_page()
    lb.configure(bg='#158aff')
    delete_page()
    page()


def welcome_page():
    welcome_frame = tk.Frame(main_frame)
    lb = tk.Label(welcome_frame , text= 'ClashPedia (Clash Royale Encyclopedia)')
    lb.place(x=20 , y = 10)
    lb.pack(padx=10 ,pady=20)

    text_label = tk.Label(welcome_frame, text='Welcome to ClashPedia, your ultimate guide to Clash Royale!\nExplore cards, strategies, updates, and much more.')
    text_label.pack(pady=10)

    instruction_label = tk.Label(welcome_frame, text='Select an option from the menu to get started.')
    instruction_label.pack(pady=10)
    welcome_frame.pack()

def categories_page():
    categories_frame = tk.Frame(main_frame)
    lb = tk.Label(categories_frame , text= 'Categories')
    lb.place(x=20 , y = 10)
    lb.pack(padx=10 ,pady=20)
    categories_frame.pack()

def avg_elixir_cal_page():
    avg_elixir_cal_frame = tk.Frame(main_frame)
    lb = tk.Label(avg_elixir_cal_frame , text= 'Average Elixir Calculator')
    lb.place(x=20 , y = 10)
    lb.pack(padx=10 ,pady=20)
    avg_elixir_cal_frame.pack()

def deck_builder_page():
    deck_builder_frame = tk.Frame(main_frame)
    lb = tk.Label(deck_builder_frame, text='Deck Builder')
    lb.place(x=20, y=10)
    lb.pack(padx=10, pady=20)
    deck_builder_frame.pack()


welcome_button = ttk.Button(options_frame , text= 'Welcome' , command=lambda:switch_page(welcome_switch_page,welcome_page))
welcome_button.place(x=20 , y= 20, width=130)
welcome_switch_page = tk.Label(options_frame, text='', bg='#c3c3c3')
welcome_switch_page.place(x=3, y=20, width=5, height =40)

categories_button = ttk.Button(options_frame , text= 'Categories' , command=lambda:switch_page(categories_switch_page,categories_page))
categories_button.place(x=20 , y= 80, width=130)
categories_switch_page = tk.Label(options_frame, text='', bg='#c3c3c3')
categories_switch_page.place(x=3, y=80, width=5, height =40)

avg_elixir_cal_button = ttk.Button(options_frame , text= 'Average Elixir\nCalculator' , command=lambda:switch_page(avg_elixir_cal_switch_page,avg_elixir_cal_page))
avg_elixir_cal_button.place(x=20 , y= 140, width=130, height=60)
avg_elixir_cal_switch_page = tk.Label(options_frame, bg='#c3c3c3')
avg_elixir_cal_switch_page.place(x=3, y=140, width=5, height =60)

deck_builder_button = ttk.Button(options_frame , text= 'Deck Builder' , command=lambda:switch_page(deck_builder_switch_page,deck_builder_page))
deck_builder_button.place(x=20 , y= 220, width=130, height=40)
deck_builder_switch_page = tk.Label(options_frame, text='', bg='#c3c3c3')
deck_builder_switch_page.place(x=3, y=220, width=5, height =40)

window.mainloop()