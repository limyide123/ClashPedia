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

    types_of_cards_label = tk.Label(welcome_frame, text='Types of Cards:')
    types_of_cards_label.pack(pady=10, anchor='w', padx=20)

    types_of_cards_text = """
    1. Troops: These are units that can move and attack.
    2. Spells: These are temporary effects that can be cast anywhere on the battlefield.
    3. Buildings: These are stationary structures that decay over time.
    4. Tower Troops: These are troops that stay on your Crown Towers and attack enemy troops.
    """
    types_of_cards_info = tk.Label(welcome_frame, text=types_of_cards_text, justify='left')
    types_of_cards_info.pack(pady=5, anchor='w', padx=40)

    rarities_and_levels_label = tk.Label(welcome_frame, text='Rarities and Levels:')
    rarities_and_levels_label.pack(pady=10, anchor='w', padx=20)

    rarities_and_levels_text = """
    - Common: Levels 1 to 15
    - Rare: Levels 3 to 15
    - Epic: Levels 6 to 15
     Legendary: Levels 9 to 15
    - Champion: Levels 11 to 15
    """
    rarities_and_levels_info = tk.Label(welcome_frame, text=rarities_and_levels_text, justify='left')
    rarities_and_levels_info.pack(pady=5, anchor='w', padx=40)

    champion_cards_label = tk.Label(welcome_frame, text='Champion Cards:')
    champion_cards_label.pack(pady=10, anchor='w', padx=20)

    champion_cards_text = """
    - Unique troops with special abilities.
    - Can be activated by tapping an icon on the screen, costing Elixir.
     Abilities have a cooldown after use.
    - Not affected by regular card cycle rules.
    - Only one Champion card allowed in a deck.
    - Mirror cannot spawn Champions.
    - Cloned Champions can't use abilities.
    """
    champion_cards_info = tk.Label(welcome_frame, text=champion_cards_text, justify='left')
    champion_cards_info.pack(pady=5, anchor='w', padx=40)

    ranges_label = tk.Label(welcome_frame, text='Ranges:')
    ranges_label.pack(pady=10, anchor='w', padx=20)

    ranges_text = """
    - Melee: Short (0.8 tiles or less)
    - Melee: Medium (1.2 tiles)
    - Melee: Long (1.6 tiles)
    - Ranged (2 or more tiles)
    """
    ranges_info = tk.Label(welcome_frame, text=ranges_text, justify='left')
    ranges_info.pack(pady=5, anchor='w', padx=40)



    welcome_frame.pack()

