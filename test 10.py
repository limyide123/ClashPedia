import tkinter as tk
from PIL import Image, ImageTk

class categories:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.table()

    def table(self):
        rows = 4
        col = 5
        for i in range(rows):
            for j in range(col):
                fku = i * col + j
                if fku < len(self.y):
                    img_path = self.y[fku]
                    img = Image.open(img_path)  # Open each image file
                    img = img.resize((100, 100))
                    img = ImageTk.PhotoImage(img)

                    label = tk.Label(self.x, image=img)
                    label.image = img
                    label.grid(row=i, column=j, padx=3, pady=3)

def main():
    data = [
        "Buildings/card_1.png", "Buildings/card_2.png", "Buildings/card_3.png",
        "Buildings/card_4.png", "Buildings/card_5.png", "Buildings/card_6.png",
        "Buildings/card_7.png", "Buildings/card_8.png", "Buildings/card_9.png",
        "Buildings/card_10.png", "Buildings/card_11.png", "Buildings/card_12.png",
        "Buildings/card_13.png"
    ]

    root = tk.Tk()
    root.title("Table")
    
    z = categories(root, data)

    root.mainloop()

if __name__ == "__main__":
    main()


    