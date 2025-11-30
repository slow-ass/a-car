import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class FrontPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple car App")
        self.root.geometry("800x600")
        
        self.canvas = tk.Canvas(root, width=600, height=1000, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        
        self.load_background()
        self.add_widgets()
        
    def load_background(self):
        image_path = "tk.png"
        img = Image.open(image_path)
        img = img.resize((800, 600))
        self.bg_image = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")

    def add_widgets(self):
        self.canvas.create_window(
            400, 100,
            window=tk.Label(
                self.root,
                text="Welcome to the game",
                font=("Arial", 24, "bold"),
                bg="white",
                fg="#2c3e50",
                padx=30,
                pady=30
            )
        )

        start_button = tk.Button(
            self.root,
            text="Start",
            font=("Arial", 14),
            bg="#3498db",
            fg="white",
        )
        self.canvas.create_window(400, 200, window=start_button)

        end_button = tk.Button(
            self.root,
            text="Quit",
            font=("Arial", 14),
            bg="#3498db",
            fg="white",
            command=self.root.quit
        )
        self.canvas.create_window(400, 250, window=end_button)

        instr_button = tk.Button(
            self.root,
            text="Show Instruction",
            font=("Arial", 14),
            bg="#3498db",
            fg="white",
            command=self.show_instruction_page
        )
        self.canvas.create_window(400, 300, window=instr_button)

    def show_instruction_page(self):
        self.canvas.destroy()
        InstructionPage(self.root)


class InstructionPage:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(root, bg="white")
        self.frame.pack(fill="both", expand=True)

        tk.Label(
            self.frame,
            text=(
                "a → accelerate\n"
                "b → brake\n"
                "left button → move left\n"
                "right button → move right"
            ),
            font=("Arial", 18, "bold"),
            bg="white",
            fg="#2c3e50",
            padx=30,
            pady=30
        ).pack()

        tk.Button(
            self.frame,
            text="Back",
            font=("Arial", 14),
            bg="#3498db",
            fg="white",
            command=self.back_to_home
        ).pack(pady=20)

    def back_to_home(self):
        self.frame.destroy()
        FrontPage(self.root)


def main():
    root = tk.Tk()
    FrontPage(root)
    root.mainloop()

if __name__ == "__main__":
    main()
