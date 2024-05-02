import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import font
from tkinter import *
from ttkbootstrap import Style
from PIL import Image, ImageTk
from ttkbootstrap.scrolled import ScrolledFrame

window = ttk.Window(themename='solar')
window.title("ClashPedia")

top_frame = tk.Frame(window, bg='#c3c3c3')
top_frame.pack(side=tk.TOP)
top_frame.pack_propagate(False)
top_frame.configure(height='150' , width='1925')

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
    welcome_frame = ScrolledFrame(main_frame, padding=5, height=10, autohide=True)
    welcome_frame.pack(fill=BOTH, expand=YES)
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

def checkbutton_click():
    print()    

def deck_builder_page():
    deck_builder_frame = ScrolledFrame(main_frame, autohide=True)
    deck_builder_frame.pack(fill=BOTH, expand=YES, padx=10, pady=10)
    lb = tk.Label(deck_builder_frame, text='Deck Builder')
    lb.place(x=20, y=10)
    lb.pack(padx=10, pady=20)

    categories = [("Win Condition", "WinCondition", 1, 2), ("Spells", "Spells", 1, 3), ("Mini Tanks", "MiniTanks", 0, 2), ("Buildings", "Buildings", 0, 2), ("Damage Units", "DamageUnits", 2, 4)]

    for section, category, min_val, max_val in categories:
        lb = tk.Label(deck_builder_frame, text=section)
        lb.pack(padx=10, pady=10)        
        for i in range(4):
            row_frame = tk.Frame(deck_builder_frame)
            row_frame.pack()
            for j in range(13):
                try:
                    image_path = f"deck_builder_images/{category}/card_{i*13 + j + 1}.png"
                    img = Image.open(image_path)
                    img = img.resize((90, 120), Image.LANCZOS)
                    img = ImageTk.PhotoImage(img)
                    panel = tk.Label(row_frame, image=img, compound=tk.LEFT, bd=0, padx=5, pady=5)
                    panel.image = img
                    panel.pack(side=tk.LEFT)

                    var = tk.BooleanVar()
                    checkbutton = ttk.Checkbutton(row_frame, variable=var, command=lambda v=var, p=panel, min_val=min_val, max_val=max_val, cat=category: on_checkbutton_click(v, p, min_val, max_val, cat))
                    checkbutton.pack(side=tk.LEFT, padx=5, pady=5)

                except FileNotFoundError:
                    break

    results_btn = tk.Button(deck_builder_frame, text="Results", command=show_results)
    results_btn.pack(padx=10, pady=10)

num_selected = 0  # Define a global variable to keep track of the number of selected items

category_counts = {
    "WinCondition": 0,
    "Spells": 0,
    "MiniTanks": 0,
    "Buildings": 0,
    "DamageUnits": 0
}

def on_checkbutton_click(var, panel, min_val, max_val, category):
    global num_selected
    if var.get():
        # Check if total selected cards exceed 8
        if num_selected >= 8:
            messagebox.showwarning("Limit Exceeded", "You can only select up to 8 cards.")
            var.set(False)
            return
        
        category_counts[category] += 1
        num_selected += 1
        panel.config(state='normal')
    else:
        category_counts[category] -= 1
        num_selected -= 1
        panel.config(state='normal')

def show_results():
    results = []
    categories = [("Win Condition", "WinCondition", 1, 2), ("Spells", "Spells", 1, 3), ("Mini Tanks", "MiniTanks", 0, 2), ("Buildings", "Buildings", 0, 2), ("Damage Units", "DamageUnits", 2, 4)]

    for section, category, min_val, max_val in categories:
        if category_counts[category] < min_val or category_counts[category] > max_val:
            results.append(f"{section}: bad")
        else:
            results.append(f"{section}: good")

    messagebox.showinfo("Results", "\n".join(results))


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