import tkinter as tk
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
import sqlite3
from tkinter import Tk, filedialog

def setup_database():
    conn = sqlite3.connect('clash_royale.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        directory TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS images (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_id INTEGER,
        filename TEXT,
        FOREIGN KEY (category_id) REFERENCES categories (id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS profilecards (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        rarity TEXT,
        elixir INTEGER,
        card_type TEXT,
        arena TEXT,
        description TEXT,
        hitpoints INTEGER,
        damage INTEGER,
        card_range INTEGER,
        stun_duration REAL,
        shield TEXT,
        movement_speed TEXT,
        radius REAL,
        image_path TEXT
    )
    ''')

    conn.commit()
    conn.close()


setup_database()

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
    
def get_data_from_db(query, param=None):
    
    conn = sqlite3.connect('clash_royale.db')
    cursor = conn.cursor()
    if param:
        cursor.execute(query, (param,))
    else:
        cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    return data

def clear_main_frame(frame=None):
    if frame:
        for widget in frame.winfo_children():
            widget.destroy()
            
    else:
        for widget in main_frame.winfo_children():
            widget.destroy()

def show_categories(category):

    clear_main_frame()

    if category == 'elixir':

        query = """
        SELECT elixir, image_path FROM profile_cards
        ORDER BY 
        CASE 
            WHEN elixir = '1' THEN 1
            WHEN elixir = '2' THEN 2
            WHEN elixir = '3' THEN 3
            WHEN elixir = '4' THEN 4 
            WHEN elixir = '5' THEN 5
            WHEN elixir = '6' THEN 6
            WHEN elixir = '7' THEN 7
            WHEN elixir = '8' THEN 8
            WHEN elixir = '9' THEN 9
            WHEN elixir = '10' THEN 10
        END
        """

        data = get_data_from_db(query)

        titles = ["Elixir_1",
                  "Elixir_2",
                  "Elixir_3",
                  "Elixir_4",
                  "Elixir_5",
                  "Elixir_6",
                  "Elixir_7",
                  "Elixir_8",
                  "Elixir_9",
                  "Elixir_10"
                  ]
        
    elif category == 'arena':

        query = """
        SELECT arena, image_path FROM profile_cards
        ORDER BY 
        CASE 
            WHEN arena = '0' THEN 1
            WHEN arena = '1' THEN 2
            WHEN arena = '2' THEN 3
            WHEN arena = '3' THEN 4 
            WHEN arena = '4' THEN 5
            WHEN arena = '5' THEN 6
            WHEN arena = '6' THEN 7
            WHEN arena = '7' THEN 8
            WHEN arena = '8' THEN 9
            WHEN arena = '9' THEN 10
            WHEN arena = '10' THEN 11
            WHEN arena = '11' THEN 12
            WHEN arena = '12' THEN 13
            WHEN arena = '13' THEN 14
            WHEN arena = '14' THEN 15
            WHEN arena = '15' THEN 16
            WHEN arena = '16' THEN 17
            WHEN arena = '17' THEN 18
            WHEN arena = '18' THEN 19
        END
        """

        data = get_data_from_db(query)

        titles = ["Arena 0",
                  "Arena 1",
                  "Arena 2",
                  "Arena 3",
                  "Arena 4",
                  "Arena 5",
                  "Arena 6",
                  "Arena 7",
                  "Arena 8",
                  "Arena 9",
                  "Arena 10",
                  "Arena 11",
                  "Arena 12", 
                  "Arena 13",
                  "Arena 14",
                  "Arena 15",
                  "Arena 16",
                  "Arena 17",
                  "Arena 18",]
        
    elif category == 'type':

        query = """
        SELECT type, filename FROM images 
        ORDER BY 
        CASE 
            WHEN type = 'Spells' THEN 1
            WHEN type = 'Troop' THEN 2
            WHEN type = 'Buildings' THEN 3
        END
        """

        data = get_data_from_db(query)

        titles = ["Spells",
                  "Troop",
                  "Buildings"]

    elif category == 'rarity':

        query = """
        SELECT rarity, image_path FROM profile_cards
        ORDER BY 
        CASE 
            WHEN rarity = 'common' THEN 1
            WHEN rarity = 'rare' THEN 2
            WHEN rarity = 'epic' THEN 3
            WHEN rarity = 'legendary' THEN 4
            WHEN rarity = 'champion' THEN 5
            WHEN rarity = 'funny' THEN 6
        END
        """

        data = get_data_from_db(query)

        titles = ["common",
                  "rare",
                  "epic",
                  "legendary",
                  "champion",
                  "funny"]

    button_frame = tk.Frame(main_frame)
    button_frame.pack(fill=tk.X, padx=10, pady=5)

    type_button = ttk.Button(button_frame, text='Type', command=lambda: show_categories('type'))
    type_button.pack(side=tk.LEFT, padx=5)

    arena_button = ttk.Button(button_frame, text='Arena', command=lambda: show_categories('arena'))
    arena_button.pack(side=tk.LEFT, padx=5)

    elixir_button = ttk.Button(button_frame, text='Elixir', command=lambda: show_categories('elixir'))
    elixir_button.pack(side=tk.LEFT, padx=5)

    rarity_button = ttk.Button(button_frame, text='Rarity', command=lambda: show_categories('rarity'))
    rarity_button.pack(side=tk.LEFT, padx=5)

    category_frame = ScrolledFrame(main_frame, autohide=True)
    category_frame.pack(fill=tk.BOTH, expand=tk.YES, padx=10, pady=10)
    

    current_title = None
    row = 0
    col = 0

    for title, filename in data:

        if title != current_title:

            if current_title is not None:

                row += 1  
            current_title = title
            title_label = tk.Label(category_frame, text=current_title, font=("Showcard Gothic", 16, "bold"))
            title_label.grid(row=row, column=0, columnspan=13, pady=(10, 0), sticky="w")
            row += 1
            col = 0

        img_path = os.path.join("clash-royale-card-elixir", filename)

        if os.path.isfile(img_path):

            img = Image.open(img_path)
            img = img.resize((90, 120), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)

            panel = tk.Label(category_frame, image=img, compound=tk.LEFT, bd=0, padx=5, pady=5)
            panel.image = img
            panel.grid(row=row, column=col, sticky="w")

            panel.bind("<Button-1>", lambda event, img_path=img_path: show_image(event, img_path))

            col += 1
            if col >= 13:
                row += 1
                col = 0

def categories_page(category=None):

    clear_main_frame()

    button_frame = tk.Frame(main_frame)
    button_frame.pack(fill=tk.X, padx=10, pady=5)

    type_button = ttk.Button(button_frame, text='Type', command=lambda: show_categories('type'))
    type_button.pack(side=tk.LEFT, padx=5)

    arena_button = ttk.Button(button_frame, text='Arena', command=lambda: show_categories('arena'))
    arena_button.pack(side=tk.LEFT, padx=5)

    elixir_button = ttk.Button(button_frame, text='Elixir', command=lambda: show_categories('elixir'))
    elixir_button.pack(side=tk.LEFT, padx=5)

    rarity_button = ttk.Button(button_frame, text='Rarity', command=lambda: show_categories('rarity'))
    rarity_button.pack(side=tk.LEFT, padx=5)

    if category:
        show_categories(category)

    else:
        show_categories('rarity')


def show_image(event, image_path):
    print(f"Image path: {image_path}") 

    image_window = tk.Toplevel()
    image_window.title("Card Image")
    image_window.geometry("600x900")

    img = Image.open(image_path)
    img = img.resize((150, 200), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)

    image_label = tk.Label(image_window, image=img)
    image_label.image = img
    image_label.pack(pady=10)

    card_details_frame = ttk.Frame(image_window)
    card_details_frame.pack(padx=20, pady=(0, 20), fill=tk.X)

    conn = sqlite3.connect('clash_royale.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT name, rarity, elixir, card_type, arena, description, hitpoints, damage, 
               card_range, stun_duration, shield, movement_speed, radius
        FROM profile_cards
        WHERE image_path = ?
    ''', (os.path.basename(image_path),))
    card_data = cursor.fetchone()
    conn.close()

    print(f"Card data: {card_data}")  

    label_font = ("Showcard Gothic", 8)
    value_font = ("Arial", 8, "bold")

    if card_data:
        labels = [
            "Name", "Rarity", "Elixir", "Card Type", "Arena", "Description", 
            "Hitpoints", "Damage", "Card Range", "Stun Duration", "Shield", 
            "Movement Speed", "Radius"
        ]

        for i, (label, value) in enumerate(zip(labels, card_data)):
            label_widget = ttk.Label(card_details_frame, text=f"{label}:", font=label_font)
            label_widget.grid(row=i*2, column=0, sticky="w", padx=(0, 10), pady=5)

            if label == "Description":
                value_widget = ttk.Label(card_details_frame, text=value, font=value_font, wraplength=400)  # Adjust wraplength as needed
            else:
                value_widget = ttk.Label(card_details_frame, text=value, font=value_font)
                
            value_widget.grid(row=i*2, column=1, sticky="w", padx=(0, 10), pady=5)

            # Add a separator line
            separator = ttk.Separator(card_details_frame, orient='horizontal')
            separator.grid(row=i*2 + 1, column=0, columnspan=2, sticky='ew', pady=(5, 5))

    else:
        error_label = ttk.Label(card_details_frame, text="No data found for this card.", font=label_font)
        error_label.grid(row=0, column=0, sticky="w", padx=(0, 10), pady=5)


# Global dictionary to store image paths for each deck
decks = {f"Deck_{i+1}": [] for i in range(10)}
boxes = []

def update_deck_display(container_frame, selected_images):
    for widget in container_frame.winfo_children():
        if isinstance(widget, tk.Frame) and not any(isinstance(w, tk.Label) for w in widget.winfo_children()):
            widget.destroy()

    row_frame = tk.Frame(container_frame)
    row_frame.pack(pady=5)
    col = 0

    for img_path in selected_images:
        img = Image.open(img_path)
        img = img.resize((90, 120), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)

        box = tk.Frame(row_frame, width=90, height=120, bg='lightgray', borderwidth=1, relief='solid')
        box.pack(side='left', padx=5)
        box.pack_propagate(False)

        label = tk.Label(box, image=img)
        label.image = img
        label.pack(expand=True)

        col += 1
        if col >= 4:
            row_frame = tk.Frame(container_frame)
            row_frame.pack(pady=5)
            col = 0

def on_box_click(deck_label, selected_images):
    new_window = tk.Toplevel(window, width=1000, height=1925)
    build_deck_page(new_window, selected_images, deck_label['text'].replace(" ", "_"), deck_label.master)

def deck_builder_page():
    deck_builder_frame = ScrolledFrame(main_frame, autohide=True)
    deck_builder_frame.pack(fill=BOTH, expand=YES, padx=10, pady=10)

    box_frame = tk.Frame(deck_builder_frame)
    box_frame.pack(pady=10, padx=10)

    for i in range(10):
        container_frame = tk.Frame(box_frame, width=500, height=400, bg='white', borderwidth=1, relief='solid')
        container_frame.grid(row=i//3, column=i%3, padx=5, pady=5)
        container_frame.pack_propagate(False)

        deck_label = tk.Label(container_frame, text=f'Deck {i+1}', font=('Showcard Gothic', 16, 'bold'))
        deck_label.pack(side='top', pady=10)

        selected_images = decks[deck_label['text'].replace(" ", "_")]  # Reference the correct list for the deck
        deck_label.bind("<Button-1>", lambda e, deck_label=deck_label, selected_images=selected_images: on_box_click(deck_label, selected_images))

        # Update the deck display initially
        update_deck_display(container_frame, selected_images)

        result_button = tk.Button(container_frame, text='Result', width=10, height=1, bg='gray', fg='white')
        result_button.pack(side='bottom', pady=20)

def build_deck_page(new_window, selected_image_paths, deck_name, container_frame, category=None):
    new_window.geometry("1250x800")
    new_window.transient(window)

    def clear_frame(frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def show_categories(frame, category):
        clear_frame(frame)

        if category == 'elixir':

            query = """
            SELECT elixir, image_path FROM profile_cards
            ORDER BY 
            CASE 
                WHEN elixir = '1' THEN 1
                WHEN elixir = '2' THEN 2
                WHEN elixir = '3' THEN 3
                WHEN elixir = '4' THEN 4 
                WHEN elixir = '5' THEN 5
                WHEN elixir = '6' THEN 6
                WHEN elixir = '7' THEN 7
                WHEN elixir = '8' THEN 8
                WHEN elixir = '9' THEN 9
                WHEN elixir = '10' THEN 10
            END
            """

            data = get_data_from_db(query)

            titles = ["Elixir_1",
                    "Elixir_2",
                    "Elixir_3",
                    "Elixir_4",
                    "Elixir_5",
                    "Elixir_6",
                    "Elixir_7",
                    "Elixir_8",
                    "Elixir_9",
                    "Elixir_10"
                    ]
            
        elif category == 'arena':

            query = """
            SELECT arena, image_path FROM profile_cards
            ORDER BY 
            CASE 
                WHEN arena = '0' THEN 1
                WHEN arena = '1' THEN 2
                WHEN arena = '2' THEN 3
                WHEN arena = '3' THEN 4 
                WHEN arena = '4' THEN 5
                WHEN arena = '5' THEN 6
                WHEN arena = '6' THEN 7
                WHEN arena = '7' THEN 8
                WHEN arena = '8' THEN 9
                WHEN arena = '9' THEN 10
                WHEN arena = '10' THEN 11
                WHEN arena = '11' THEN 12
                WHEN arena = '12' THEN 13
                WHEN arena = '13' THEN 14
                WHEN arena = '14' THEN 15
                WHEN arena = '15' THEN 16
                WHEN arena = '16' THEN 17
                WHEN arena = '17' THEN 18
                WHEN arena = '18' THEN 19
            END
            """

            data = get_data_from_db(query)

            titles = ["Arena 0",
                    "Arena 1",
                    "Arena 2",
                    "Arena 3",
                    "Arena 4",
                    "Arena 5",
                    "Arena 6",
                    "Arena 7",
                    "Arena 8",
                    "Arena 9",
                    "Arena 10",
                    "Arena 11",
                    "Arena 12", 
                    "Arena 13",
                    "Arena 14",
                    "Arena 15",
                    "Arena 16",
                    "Arena 17",
                    "Arena 18",]
            
        elif category == 'type':

            query = """
            SELECT type, filename FROM images 
            ORDER BY 
            CASE 
                WHEN type = 'Spells' THEN 1
                WHEN type = 'Troop' THEN 2
                WHEN type = 'Buildings' THEN 3
            END
            """

            data = get_data_from_db(query)

            titles = ["Spells",
                    "Troop",
                    "Buildings"]

        elif category == 'rarity':

            query = """
            SELECT rarity, image_path FROM profile_cards
            ORDER BY 
            CASE 
                WHEN rarity = 'common' THEN 1
                WHEN rarity = 'rare' THEN 2
                WHEN rarity = 'epic' THEN 3
                WHEN rarity = 'legendary' THEN 4
                WHEN rarity = 'champion' THEN 5
                WHEN rarity = 'funny' THEN 6
            END
            """

            data = get_data_from_db(query)

            titles = ["common",
                    "rare",
                    "epic",
                    "legendary",
                    "champion",
                    "funny"]

        button_frame = tk.Frame(frame)
        button_frame.pack(fill=tk.X, padx=10, pady=5)

        type_button = ttk.Button(button_frame, text='Type', command=lambda: show_categories(frame, 'type'))
        type_button.pack(side=tk.LEFT, padx=5)

        arena_button = ttk.Button(button_frame, text='Arena', command=lambda: show_categories(frame, 'arena'))
        arena_button.pack(side=tk.LEFT, padx=5)

        elixir_button = ttk.Button(button_frame, text='Elixir', command=lambda: show_categories(frame, 'elixir'))
        elixir_button.pack(side=tk.LEFT, padx=5)

        rarity_button = ttk.Button(button_frame, text='Rarity', command=lambda: show_categories(frame, 'rarity'))
        rarity_button.pack(side=tk.LEFT, padx=5)

        category_frame = ScrolledFrame(frame, autohide=True)
        category_frame.pack(fill=tk.BOTH, expand=tk.YES, padx=10, pady=10)

        current_title = None
        row = 0
        col = 0

        for title, filename in data:
            if title != current_title:
                if current_title is not None:
                    row += 1  
                current_title = title
                title_label = tk.Label(category_frame, text=current_title, font=("Showcard Gothic", 16, "bold"))
                title_label.grid(row=row, column=0, columnspan=13, pady=(10, 0), sticky="w")
                row += 1
                col = 0

            img_path = os.path.join("clash-royale-card-elixir", filename)

            if os.path.isfile(img_path):
                img = Image.open(img_path)
                img = img.resize((90, 120), Image.LANCZOS)
                img = ImageTk.PhotoImage(img)

                panel = tk.Label(category_frame, image=img, compound=tk.LEFT, bd=0, padx=5, pady=5)
                panel.image = img
                panel.grid(row=row, column=col, sticky="w")

                panel.bind("<Button-1>", lambda event, img_path=img_path: on_image_click(event, img_path))

                col += 1
                if col >= 13:
                    row += 1
                    col = 0

        def on_image_click(event, img_path):
            if img_path not in selected_image_paths:
                if len(selected_image_paths) < 8:
                    selected_image_paths.append(img_path)
                    row, col = 0, 0
                    clear_frame(deck_frame)
                    for img_path in selected_image_paths:
                        img = Image.open(img_path)
                        img = img.resize((90, 120), Image.LANCZOS)
                        img = ImageTk.PhotoImage(img)

                        panel = tk.Label(deck_frame, image=img, compound=tk.LEFT, bd=0, padx=5, pady=5)
                        panel.image = img
                        panel.grid(row=row, column=col)

                        col += 1
                        if col >= 13:
                            col = 0
                            row += 1

                        panel.bind("<Button-1>", lambda event, img_path=img_path: remove_image_from_deck(event, img_path))
                else:
                    messagebox.showwarning("Limit Reached", "You can only choose 8 cards.")
            else:
                messagebox.showwarning("Repeated Card", "You have already chosen this card.")

        def remove_image_from_deck(event, img_path):
            selected_image_paths.remove(img_path)
            row, col = 0, 0
            clear_frame(deck_frame)
            for img_path in selected_image_paths:
                img = Image.open(img_path)
                img = img.resize((90, 120), Image.LANCZOS)
                img = ImageTk.PhotoImage(img)

                panel = tk.Label(deck_frame, image=img, compound=tk.LEFT, bd=0, padx=5, pady=5)
                panel.image = img
                panel.grid(row=row, column=col)

                col += 1
                if col >= 13:
                    col = 0
                    row += 1

                panel.bind("<Button-1>", lambda event, img_path=img_path: remove_image_from_deck(event, img_path))

        def save_deck():
            decks[deck_name] = list(selected_image_paths)  # Update the correct deck with the selected images
            messagebox.showinfo("Success", f"{deck_name} has been saved with {len(selected_image_paths)} cards.")
            update_deck_display(container_frame, selected_image_paths)

        def clear_deck():
            selected_image_paths.clear()
            clear_frame(deck_frame)

        deck_frame = tk.Frame(new_window)
        deck_frame.pack(side=BOTTOM, fill=X)

        save_button = tk.Button(button_frame, text="Save", command=save_deck)
        save_button.pack(side=RIGHT, padx=10)

        clear_button = tk.Button(button_frame, text='Clear', command=clear_deck)
        clear_button.pack(side=RIGHT, padx=10)
        
    if category:
        show_categories(new_window, category)
    else:
        show_categories(new_window, 'rarity')

def display_deck_images(container_frame, selected_image_paths):
    def clear_frame(frame):
        for widget in frame.winfo_children():
            widget.destroy()
    clear_frame(container_frame)
    row, col = 0, 0
    row_frame = tk.Frame(container_frame)
    row_frame.pack(pady=5)
    for img_path in selected_image_paths:
        img = Image.open(img_path)
        img = img.resize((90, 120), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)

        box = tk.Frame(row_frame, width=90, height=120, bg='lightgray', borderwidth=1, relief='solid')
        box.pack(side='left', padx=5)
        box.pack_propagate(False)

        label = tk.Label(box, image=img)
        label.image = img
        label.pack(expand=True)

        col += 1
        if col >= 4:
            row_frame = tk.Frame(container_frame)
            row_frame.pack(pady=5)
            col = 0

def save_card_to_file(name, rarity, elixir, card_type, arena, description, hitpoints, damage, card_range, stun_duration, shield, movement_speed, radius, image_path=None):
    if not name or not rarity or not elixir or not card_type or not arena or not description:
        messagebox.showwarning("Input Error", "Name, Rarity, Elixir, Type, Arena, and Description are required fields.")
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

    conn = sqlite3.connect('clash_royale.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO profile_cards (name, rarity, elixir, card_type, arena, description, hitpoints, damage, card_range, stun_duration, shield, movement_speed, radius, image_path)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (name, rarity, elixir, card_type, arena, description.strip(), hitpoints, damage, card_range, stun_duration, shield, movement_speed, radius, image_path))

    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Card saved successfully.")

def upload_image():
    root = Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(title="Select an image", filetypes=[('Image files', '*.png *.jpg *.jpeg')])
    root.destroy()  # Close the file explorer window
    return file_path


def profile_maker_page():
    profile_maker_frame = ScrolledFrame(main_frame, padding=5, height=10, autohide=True)
    profile_maker_frame.pack(fill=BOTH, expand=YES)

    title_label = tk.Label(profile_maker_frame, text="Profile Maker", font=('Showcard Gothic', 25, 'bold'))
    title_label.pack(pady=10)

    form_frame = tk.Frame(profile_maker_frame)
    form_frame.pack(pady=10, padx=10)

    name_label = tk.Label(form_frame, text="Card Name:")
    name_label.grid(row=0, column=0, padx=5, pady=5)
    name_entry = tk.Entry(form_frame)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    rarity_label = tk.Label(form_frame, text="Rarity:")
    rarity_label.grid(row=1, column=0, padx=5, pady=5)
    rarity_entry = tk.Entry(form_frame)
    rarity_entry.grid(row=1, column=1, padx=5, pady=5)

    elixir_label = tk.Label(form_frame, text="Elixir Cost:")
    elixir_label.grid(row=2, column=0, padx=5, pady=5)
    elixir_entry = tk.Entry(form_frame)
    elixir_entry.grid(row=2, column=1, padx=5, pady=5)

    type_label = tk.Label(form_frame, text="Card Type:")
    type_label.grid(row=3, column=0, padx=5, pady=5)
    type_entry = tk.Entry(form_frame)
    type_entry.grid(row=3, column=1, padx=5, pady=5)

    arena_label = tk.Label(form_frame, text="Arena:")
    arena_label.grid(row=4, column=0, padx=5, pady=5)
    arena_entry = tk.Entry(form_frame)
    arena_entry.grid(row=4, column=1, padx=5, pady=5)

    description_label = tk.Label(form_frame, text="Description:")
    description_label.grid(row=5, column=0, padx=5, pady=5)
    description_text = tk.Text(form_frame, height=5, width=40)
    description_text.grid(row=5, column=1, padx=5, pady=5)

    hitpoints_label = tk.Label(form_frame, text="Hitpoints:")
    hitpoints_label.grid(row=6, column=0, padx=5, pady=5)
    hitpoints_entry = tk.Entry(form_frame)
    hitpoints_entry.grid(row=6, column=1, padx=5, pady=5)

    damage_label = tk.Label(form_frame, text="Damage:")
    damage_label.grid(row=7, column=0, padx=5, pady=5)
    damage_entry = tk.Entry(form_frame)
    damage_entry.grid(row=7, column=1, padx=5, pady=5)

    range_label = tk.Label(form_frame, text="Range:")
    range_label.grid(row=8, column=0, padx=5, pady=5)
    range_entry = tk.Entry(form_frame)
    range_entry.grid(row=8, column=1, padx=5, pady=5)

    stun_duration_label = tk.Label(form_frame, text="Stun Duration:")
    stun_duration_label.grid(row=9, column=0, padx=5, pady=5)
    stun_duration_entry = tk.Entry(form_frame)
    stun_duration_entry.grid(row=9, column=1, padx=5, pady=5)

    shield_label = tk.Label(form_frame, text="Shield:")
    shield_label.grid(row=10, column=0, padx=5, pady=5)
    shield_entry = tk.Entry(form_frame)
    shield_entry.grid(row=10, column=1, padx=5, pady=5)

    movement_speed_label = tk.Label(form_frame, text="Movement Speed:")
    movement_speed_label.grid(row=11, column=0, padx=5, pady=5)
    movement_speed_entry = tk.Entry(form_frame)
    movement_speed_entry.grid(row=11, column=1, padx=5, pady=5)

    radius_label = tk.Label(form_frame, text="Radius:")
    radius_label.grid(row=12, column=0, padx=5, pady=5)
    radius_entry = tk.Entry(form_frame)
    radius_entry.grid(row=12, column=1, padx=5, pady=5)

    save_button = tk.Button(form_frame, text="Save", command=lambda: save_card_to_file(
        name_entry.get(),
        rarity_entry.get(),
        elixir_entry.get(),
        type_entry.get(),
        arena_entry.get(),
        description_text.get("1.0", tk.END),
        hitpoints_entry.get(),
        damage_entry.get(),
        range_entry.get(),
        stun_duration_entry.get(),
        shield_entry.get(),
        movement_speed_entry.get(),
        radius_entry.get()
    ))
    save_button.grid(row=13, column=0, columnspan=2, pady=10)

    upload_button = ttk.Button(form_frame, text="Upload Image", command=upload_image)
    upload_button.grid(row=14, column=1, padx=5)

    profile_maker_frame.pack() 



welcome_button = ttk.Button(options_frame , text= 'Welcome' , command=lambda:switch_page(welcome_switch_page,welcome_page))
welcome_button.place(x=20 , y= 20, width=130)
welcome_switch_page = tk.Label(options_frame, text='', bg='#c3c3c3')
welcome_switch_page.place(x=3, y=20, width=5, height =40)

categories_button = ttk.Button(options_frame , text= 'Categories' , command=lambda:switch_page(categories_switch_page,categories_page))
categories_button.place(x=20 , y= 80, width=130)
categories_switch_page = tk.Label(options_frame, text='', bg='#c3c3c3')
categories_switch_page.place(x=3, y=80, width=5, height =40)

deck_builder_button = ttk.Button(options_frame , text= 'Deck Builder' , command=lambda:switch_page(deck_builder_switch_page,deck_builder_page))
deck_builder_button.place(x=20 , y= 140, width=130, height=40)
deck_builder_switch_page = tk.Label(options_frame, text='', bg='#c3c3c3')
deck_builder_switch_page.place(x=3, y=140, width=5, height =40)

profile_maker_button = ttk.Button(options_frame, text='Profile Maker', command=lambda: switch_page(profile_maker_switch_page, profile_maker_page))
profile_maker_button.place(x=20, y=200, width=130, height=40)
profile_maker_switch_page = tk.Label(options_frame, text='', bg='#c3c3c3')
profile_maker_switch_page.place(x=3, y=200, width=5, height=40)


window.mainloop()
