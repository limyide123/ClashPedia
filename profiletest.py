import tkinter as tk
import sqlite3
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import font
from tkinter import *
from ttkbootstrap import Style
from PIL import Image, ImageTk
from ttkbootstrap.scrolled import ScrolledFrame
import os
from tkinter import PhotoImage
import csv
import tkinter.messagebox as messagebox

window = ttk.Window(themename='solar')
window.title("ClashPedia")

top_frame = tk.Frame(window, bg='#c3c3c3')
top_frame.pack(side=tk.TOP)
top_frame.pack_propagate(False)
top_frame.configure(height='150' , width='1925')

lb = tk.Label(top_frame , text= 'ClashPedia (Clash Royale Encyclopedia)', font=('Showcard Gothic', 36, 'bold'))
lb.place(x=20 , y = 10)
lb.pack(padx=10 ,pady=20)

options_frame = tk.Frame(window, bg='#c3c3c3')
options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(height='800' , width='175')

main_frame = tk.Frame(window)
main_frame.pack(side=LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height='1000' ,width='1750')

logo_dir = "design_photo"
logo_filename = "logo.png"
logo_path = os.path.join(logo_dir, logo_filename)

logo_img = Image.open(logo_path)
logo_img = logo_img.resize((160, 150), Image.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_img)

logo_label = tk.Label(top_frame, image=logo_photo, bg='#c3c3c3')
logo_label.place(x=10, y=20)  

def hide_switch_page():
    welcome_switch_page.config(bg='#c3c3c3')
    categories_switch_page.config(bg='#c3c3c3')
    avg_elixir_cal_switch_page.config(bg='#c3c3c3')
    deck_builder_switch_page.config(bg='#c3c3c3')
    profile_maker_switch_page.config(bg='#c3c3c3')


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

    text_label = tk.Label(welcome_frame, text='Welcome to ClashPedia, your ultimate guide to Clash Royale!\nExplore cards, strategies, updates, and much more.', font=('Showcard Gothic', 23, 'bold'))
    text_label.pack(pady=10)

    banner_path = "design_photo/banner.png"
    image = Image.open(banner_path)
    image = ImageTk.PhotoImage(image)

    image_label = tk.Label(welcome_frame, image=image)
    image_label.image = image
    image_label.pack()

    tutorial_of_cards_label = tk.Label(welcome_frame, text='What is "CLASH ROYALE?"', font=('Rockwell Extra Bold', 15, 'bold'))
    tutorial_of_cards_label.pack(pady=10, anchor='w', padx=20)

    tutorial_of_cards_text = """
    Winning Battles:
    - Get more Crowns than your opponent by destroying their Crown Towers.
    - Destroying the opponent's King's Tower instantly gives you 3 Crowns and wins the game.
    - If no King's Tower is destroyed, the player with more Crowns at the end of the 3-minute period wins.
    - If neither player has more Crowns, the game goes into Overtime.
    - Overtime ends if a Crown Tower is destroyed, deciding the winner.
    - If all towers have identical health, a tiebreaker occurs where towers rapidly lose health until one is destroyed.

    Trophies and Rewards:
    - Winning earns Trophies, while losing loses them.
    - Trophies unlock new Arenas and higher Leagues.
    - New Arenas offer new Cards and better rewards.
    - Victory in Challenges and Tournaments earns rewards and progresses in the event.

    Clan Wars:
    - In a stalemate, a coin flip decides the winner.
    - Trophies contribute to Clan War standings and rewards.1. Troops: These are units that can move and attack.
        2. Spells: These are temporary effects that can be cast anywhere on the battlefield.
        3. Buildings: These are stationary structures that decay over time.
        4. Tower Troops: These are troops that stay on your Crown Towers and attack enemy troops.
    """
    tutorial_of_cards_info = tk.Label(welcome_frame, text=tutorial_of_cards_text, justify='left')
    tutorial_of_cards_info.pack(pady=5, anchor='w', padx=40)  

    types_frame = tk.Frame(welcome_frame, bg="white", bd=2, relief=tk.GROOVE)
    types_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

    tutorial_of_cards_label = tk.Label(types_frame, text='Types of Cards:', font=('Rockwell Extra Bold', 15, 'bold'))
    tutorial_of_cards_label.pack(pady=10, anchor='w', padx=20)

    tutorial_of_cards_text = """
    1. Troops: These are units that can move and attack.
    2. Spells: These are temporary effects that can be cast anywhere on the battlefield.
    3. Buildings: These are stationary structures that decay over time.
    4. Tower Troops: These are troops that stay on your Crown Towers and attack enemy troops.
    """
    tutorial_of_cards_info = tk.Label(types_frame, text=tutorial_of_cards_text, justify='left')
    tutorial_of_cards_info.pack(pady=5, anchor='w', padx=40)

    rarities_frame = tk.Frame(welcome_frame, bg="white", bd=2, relief=tk.GROOVE)
    rarities_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

    rarities_and_levels_label = tk.Label(rarities_frame, text='Rarities and Levels:', font=('Rockwell Extra Bold', 15, 'bold'))
    rarities_and_levels_label.pack(pady=10, anchor='w', padx=20)

    rarities_and_levels_text = """
    - Common: Levels 1 to 15
    - Rare: Levels 3 to 15
    - Epic: Levels 6 to 15
    - Legendary: Levels 9 to 15
    - Champion: Levels 11 to 15
    """
    rarities_and_levels_info = tk.Label(rarities_frame, text=rarities_and_levels_text, justify='left')
    rarities_and_levels_info.pack(pady=5, anchor='w', padx=40)

    champion_frame = tk.Frame(welcome_frame, bg="white", bd=2, relief=tk.GROOVE)
    champion_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

    champion_cards_label = tk.Label(champion_frame, text='Champion Cards:', font=('Rockwell Extra Bold', 15, 'bold'))
    champion_cards_label.pack(pady=10, anchor='w', padx=20)

    champion_cards_text = """
    - Unique troops with special abilities.
    - Can be activated by tapping an icon on the screen, costing Elixir.
    - Abilities have a cooldown after use.
    - Not affected by regular card cycle rules.
    - Only one Champion card allowed in a deck.
    - Mirror cannot spawn Champions.
    - Cloned Champions can't use abilities.
    """
    champion_cards_info = tk.Label(champion_frame, text=champion_cards_text, justify='left')
    champion_cards_info.pack(pady=5, anchor='w', padx=40)

    ranges_frame = tk.Frame(welcome_frame, bg="white", bd=2, relief=tk.GROOVE)
    ranges_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

    ranges_label = tk.Label(ranges_frame, text='Ranges:', font=('Rockwell Extra Bold', 15, 'bold'))
    ranges_label.pack(pady=10, anchor='w', padx=20)

    ranges_text = """
    - Melee: Short (0.8 tiles or less)
    - Melee: Medium (1.2 tiles)
    - Melee: Long (1.6 tiles)
    - Ranged (2 or more tiles)
    """
    ranges_info = tk.Label(ranges_frame, text=ranges_text, justify='left')
    ranges_info.pack(pady=5, anchor='w', padx=40)

    welcome_frame.pack()
    
def categories_page():
    categories_frame = ScrolledFrame(main_frame)
    categories_frame.pack(fill=BOTH, expand=YES, padx=10, pady=10)
    lb = tk.Label(categories_frame, text= 'Categories')
    lb.grid(row=0, column=0, columnspan=13, padx=10, pady=20)

    categories_folder = "clash-royale-card-elixir"
    categories = [("Common", "common"), ("Rare", "rare"), ("Epic", "epic"), ("Legendary", "legendary"), ("Champion", "champion"), ("Funny", "funny")]

    for i, (section, category) in enumerate(categories):

        category_frame = tk.Frame(categories_frame, bg="white", bd=2, relief=tk.GROOVE)
        category_frame.grid(row=i*5, column=0, columnspan=13, padx=10, pady=10, sticky='ew')

        lb = tk.Label(category_frame, text=section, font=('Showcard Gothic', 15, 'bold'))
        lb.grid(row=0, column=0, columnspan=13, padx=10, pady=10, sticky='ew')

        category_folder = os.path.join(categories_folder, category)
        for j in range(4):
            for k in range(13):
                filename = f"card_{j*13+k+1}.png"
                image_path = os.path.join(category_folder, filename)
                if os.path.exists(image_path):
                    img = Image.open(image_path)
                    img = img.resize((90, 120), Image.LANCZOS)
                    img = ImageTk.PhotoImage(img)
                    panel = tk.Label(category_frame, image=img, compound=tk.LEFT, bd=0, padx=5, pady=5)
                    panel.image = img
                    panel.grid(row=j+1, column=k, padx=5, pady=5)

                    panel.bind("<Button>", lambda e, img=img: show_image(e, img))

    categories_frame.pack()

def show_image(event, img):
    image_window = tk.Toplevel()
    image_window.title("Card Image")
    image_window.geometry("600x800")

    image_label = tk.Label(image_window, image=img)
    image_label.pack(padx=100, pady=100)

def avg_elixir_cal_page():
    avg_elixir_cal_frame = ScrolledFrame(main_frame, autohide=True)
    avg_elixir_cal_frame.pack(fill=BOTH, expand=YES, padx=10, pady=10)
    lb = tk.Label(avg_elixir_cal_frame , text= 'Average Elixir Calculator', font=('Showcard Gothic', 20, 'bold'))
    lb.place(x=20 , y = 10)
    lb.pack(padx=10 ,pady=20)
    
    categories = [("Elixir 1", "Elixir_1", 1), ("Elixir 2", "Elixir_2", 2), ("Elixir 3", "Elixir_3", 3), ("Elixir 4", "Elixir_4", 4), ("Elixir 5", "Elixir_5", 5), ("Elixir 6", "Elixir_6", 6), ("Elixir 7", "Elixir_7", 7), ("Elixir 8", "Elixir_8", 8), ("Elixir 9", "Elixir_9", 9)]

    for section, category, value in categories:
        lb = tk.Label(avg_elixir_cal_frame, text=section, font=('Rockwell Extra Bold', 15, 'bold'))
        lb.pack(padx=10, pady=10)        
        for i in range(3):
            row_frame = tk.Frame(avg_elixir_cal_frame)
            row_frame.pack()
            for j in range(11):
                try:
                    image_path = f"average_elixir_calculator_images/{category}/card_{i*11 + j + 1}.png"
                    img = Image.open(image_path)
                    img = img.resize((90, 120), Image.LANCZOS)
                    img = ImageTk.PhotoImage(img)
                    panel = tk.Label(row_frame, image=img, compound=tk.LEFT, bd=0, padx=5, pady=5)
                    panel.image = img
                    panel.pack(side=tk.LEFT)

                    var = tk.BooleanVar()
                    checkbutton = ttk.Checkbutton(row_frame, variable=var, command=lambda v=var, p=panel, val = value, cat=category: elixir_checkbutton_click(v, p, val, cat))
                    checkbutton.pack(side=tk.LEFT, padx=5, pady=5)

                except FileNotFoundError:
                    break

    results_btn = tk.Button(avg_elixir_cal_frame, text="Results", command=cal_results)
    results_btn.pack(padx=10, pady=10)
    avg_elixir_cal_frame.pack()

elixir_num_selected = 0

elixir_category_counts={
    "Elixir_1":0,
    "Elixir_2":0,
    "Elixir_3":0,
    "Elixir_4":0,
    "Elixir_5":0,
    "Elixir_6":0,
    "Elixir_7":0,
    "Elixir_8":0,
    "Elixir_9":0
}

def elixir_checkbutton_click(var, panel, val, category):
    global elixir_num_selected
    if var.get():
        # Check if total selected cards exceed 8
        if elixir_num_selected >= 8:
            messagebox.showwarning("Limit Exceeded", "You can only select up to 8 cards.")
            var.set(False)
            return
        elixir_category_counts[category] += val
        elixir_num_selected += 1
        panel.config(state='normal')
    else:
        elixir_category_counts[category] -= val
        elixir_num_selected -= 1
        panel.config(state='normal')

def cal_results():
    total_elixir = sum(elixir_category_counts.values())
    average_elixir = total_elixir / 8  # Assuming the user selects exactly 8 cards

    feedback = ""
    if 0.1 <= average_elixir <= 2.0:
        feedback = "You're a fast cycle guy"
    elif 2.1 <= average_elixir <= 3.2:
        feedback = "You're either using 2.6 hog or 2.9 mortar"
    elif 3.3 <= average_elixir <= 4.1:
        feedback = "You're not dependent on cycle decks now"
    elif 4.2 <= average_elixir <= 4.7:
        feedback = "Woah, that's a bit too expensive"
    elif 4.8 <= average_elixir <= 5.6:
        feedback = "Are you trolling at this point?"
    else:
        feedback = "I'm certain you're playing 7x elixir"

    messagebox.showinfo("Average Elixir and Feedback", f"Average Elixir: {average_elixir:.2f}\nFeedback: {feedback}")

def deck_builder_page():
    deck_builder_frame = ScrolledFrame(main_frame, autohide=True)
    deck_builder_frame.pack(fill=BOTH, expand=YES, padx=10, pady=10)
    lb = tk.Label(deck_builder_frame, text='Deck Builder', font=('Showcard Gothic', 15, 'bold'))
    lb.place(x=20, y=10)
    lb.pack(padx=10, pady=20)

    categories = [("Win Condition", "WinCondition", 1, 2), ("Spells", "Spells", 1, 3), ("Mini Tanks", "MiniTanks", 0, 2), ("Buildings", "Buildings", 0, 2), ("Damage Units", "DamageUnits", 2, 4)]

    for section, category, min_val, max_val in categories:
        category_frame = tk.Frame(deck_builder_frame, bg="white", bd=2, relief=tk.GROOVE)
        category_frame.pack(pady=10, padx=10, fill=tk.X)
        
        lb = tk.Label(category_frame, text=section)
        lb.pack(padx=10, pady=10)        
        for i in range(4):
            row_frame = tk.Frame(category_frame, bg="white")
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

num_selected = 0 
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


def profile_maker_page():
    profile_maker_frame = ScrolledFrame(main_frame, padding=5, height=10, autohide=True)
    profile_maker_frame.pack(fill=BOTH, expand=YES)

    title_label = tk.Label(profile_maker_frame, text="Profile Maker", font=('Showcard Gothic', 23, 'bold'))
    title_label.pack(pady=10)

    form_frame = tk.Frame(profile_maker_frame)
    form_frame.pack(pady=10, padx=10)

    name_label = tk.Label(form_frame, text="Card Name:")
    name_label.grid(row=0, column=0, padx=5, pady=5)
    name_entry = tk.Entry(form_frame)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    elixir_label = tk.Label(form_frame, text="Elixir Cost:")
    elixir_label.grid(row=1, column=0, padx=5, pady=5)
    elixir_entry = tk.Entry(form_frame)
    elixir_entry.grid(row=1, column=1, padx=5, pady=5)

    type_label = tk.Label(form_frame, text="Card Type:")
    type_label.grid(row=2, column=0, padx=5, pady=5)
    type_entry = tk.Entry(form_frame)
    type_entry.grid(row=2, column=1, padx=5, pady=5)

    description_label = tk.Label(form_frame, text="Description:")
    description_label.grid(row=3, column=0, padx=5, pady=5)
    description_text = tk.Text(form_frame, height=5, width=40)
    description_text.grid(row=3, column=1, padx=5, pady=5)

    hitpoints_label = tk.Label(form_frame, text="Hitpoints:")
    hitpoints_label.grid(row=4, column=0, padx=5, pady=5)
    hitpoints_entry = tk.Entry(form_frame)
    hitpoints_entry.grid(row=4, column=1, padx=5, pady=5)

    damage_label = tk.Label(form_frame, text="Damage:")
    damage_label.grid(row=5, column=0, padx=5, pady=5)
    damage_entry = tk.Entry(form_frame)
    damage_entry.grid(row=5, column=1, padx=5, pady=5)

    range_label = tk.Label(form_frame, text="Range:")
    range_label.grid(row=6, column=0, padx=5, pady=5)
    range_entry = tk.Entry(form_frame)
    range_entry.grid(row=6, column=1, padx=5, pady=5)

    stun_duration_label = tk.Label(form_frame, text="Stun Duration:")
    stun_duration_label.grid(row=7, column=0, padx=5, pady=5)
    stun_duration_entry = tk.Entry(form_frame)
    stun_duration_entry.grid(row=7, column=1, padx=5, pady=5)

    shield_label = tk.Label(form_frame, text="Shield:")
    shield_label.grid(row=8, column=0, padx=5, pady=5)
    shield_entry = tk.Entry(form_frame)
    shield_entry.grid(row=8, column=1, padx=5, pady=5)

    movement_speed_label = tk.Label(form_frame, text="Movement Speed:")
    movement_speed_label.grid(row=9, column=0, padx=5, pady=5)
    movement_speed_entry = tk.Entry(form_frame)
    movement_speed_entry.grid(row=9, column=1, padx=5, pady=5)

    radius_label = tk.Label(form_frame, text="Radius:")
    radius_label.grid(row=10, column=0, padx=5, pady=5)
    radius_entry = tk.Entry(form_frame)
    radius_entry.grid(row=10, column=1, padx=5, pady=5)

    save_button = tk.Button(form_frame, text="Save", command=lambda: save_card_to_file(
        name_entry.get(),
        elixir_entry.get(),
        type_entry.get(),
        description_text.get("1.0", tk.END),
        hitpoints_entry.get(),
        damage_entry.get(),
        range_entry.get(),
        stun_duration_entry.get(),
        shield_entry.get(),
        movement_speed_entry.get(),
        radius_entry.get()
    ))
    save_button.grid(row=11, column=0, columnspan=2, pady=10)

    profile_maker_frame.pack()


def save_card_to_file(name, elixir, card_type, description, hitpoints, damage, card_range, stun_duration, shield, movement_speed, radius):
    if not name or not elixir or not card_type or not description:
        messagebox.showwarning("Input Error", "Name, Elixir, Type, and Description are required fields.")
        return

    try:
        elixir = int(elixir)
        hitpoints = int(hitpoints)
        damage = int(damage)
        card_range = int(card_range)
        stun_duration = float(stun_duration)
        radius = float(radius)
    except ValueError:
        messagebox.showwarning("Input Error", "Elixir, Hitpoints, Damage, Range, Stun Duration, and Radius must be numbers.")
        return

    card_data = [name, elixir, card_type, description.strip(), hitpoints, damage, card_range, stun_duration, shield, movement_speed, radius]

    with open('cards.txt', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(card_data)
    
    messagebox.showinfo("Success", "Card saved successfully.")


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

avg_elixir_cal_button = ttk.Button(options_frame , text= 'Average Elixir\nCalculator' , command=lambda:switch_page(avg_elixir_cal_switch_page,avg_elixir_cal_page))
avg_elixir_cal_button.place(x=20 , y= 140, width=130, height=60)
avg_elixir_cal_switch_page = tk.Label(options_frame, bg='#c3c3c3')
avg_elixir_cal_switch_page.place(x=3, y=140, width=5, height =60)

deck_builder_button = ttk.Button(options_frame , text= 'Deck Builder' , command=lambda:switch_page(deck_builder_switch_page,deck_builder_page))
deck_builder_button.place(x=20 , y= 220, width=130, height=40)
deck_builder_switch_page = tk.Label(options_frame, text='', bg='#c3c3c3')
deck_builder_switch_page.place(x=3, y=220, width=5, height =40)

profile_maker_button = ttk.Button(options_frame, text='Profile Maker', command=lambda: switch_page(profile_maker_switch_page, profile_maker_page))
profile_maker_button.place(x=20, y=280, width=130, height=40)
profile_maker_switch_page = tk.Label(options_frame, text='', bg='#c3c3c3')
profile_maker_switch_page.place(x=3, y=280, width=5, height=40)


window.mainloop()
