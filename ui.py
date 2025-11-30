import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os

class LauncherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("3D Racing Game Launcher")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        
        # Style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Header
        header = tk.Label(root, text="3D Racing Game", font=("Helvetica", 24, "bold"), pady=20)
        header.pack()
        
        # Main Frame
        main_frame = tk.Frame(root)
        main_frame.pack(pady=20)
        
        # Level Selection
        tk.Label(main_frame, text="Select Level:", font=("Helvetica", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.level_var = tk.StringVar(value="City")
        level_combo = ttk.Combobox(main_frame, textvariable=self.level_var, values=["City", "Desert", "Night"], state="readonly")
        level_combo.grid(row=0, column=1, padx=10, pady=10)
        
        # Car Selection
        tk.Label(main_frame, text="Select Car Color:", font=("Helvetica", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.car_var = tk.StringVar(value="red")
        car_combo = ttk.Combobox(main_frame, textvariable=self.car_var, values=["red", "blue", "green", "yellow", "black", "white"], state="readonly")
        car_combo.grid(row=1, column=1, padx=10, pady=10)
        
        # Buttons Frame
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=20)
        
        play_btn = tk.Button(btn_frame, text="START GAME", font=("Helvetica", 14, "bold"), bg="#4CAF50", fg="white", width=15, command=self.launch_game)
        play_btn.pack(side=tk.LEFT, padx=10)
        
        settings_btn = tk.Button(btn_frame, text="Settings", font=("Helvetica", 12), width=10, command=self.open_settings)
        settings_btn.pack(side=tk.LEFT, padx=10)
        
        exit_btn = tk.Button(btn_frame, text="Exit", font=("Helvetica", 12), width=10, bg="#f44336", fg="white", command=root.quit)
        exit_btn.pack(side=tk.LEFT, padx=10)
        
        # Footer
        footer = tk.Label(root, text="Controls: WASD / Arrows to Drive | ESC to Exit", font=("Helvetica", 10), fg="gray")
        footer.pack(side=tk.BOTTOM, pady=10)

    def launch_game(self):
        level = self.level_var.get()
        car_color = self.car_var.get()
        
        print(f"Launching game with Level={level}, Car={car_color}")
        
        # Properly destroy the Tkinter window before starting Ursina
        # This is critical - Tkinter must be completely cleaned up
        self.root.quit()  # Stop the mainloop
        self.root.destroy()  # Destroy the window
        
        # Now import and run the game engine in the same process
        # We import here to avoid conflicts with Tkinter
        try:
            from game_engine import start_game
            start_game(level=level, car_color=car_color)
        except Exception as e:
            print(f"Error launching game: {e}")
            import traceback
            traceback.print_exc()

    def open_settings(self):
        messagebox.showinfo("Settings", "Settings menu not implemented yet.\n\nGraphics: High\nSound: On")

if __name__ == "__main__":
    root = tk.Tk()
    app = LauncherApp(root)
    root.mainloop()
