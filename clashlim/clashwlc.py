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


