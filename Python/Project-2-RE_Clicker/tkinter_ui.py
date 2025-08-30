#############################################################
#
#   tkinter_ui.py is used to manage all about UI
#
#############################################################

import os
import tkinter as tk
from tkinter import ttk

from classAll import Player
from functionsAll import (
    create_random_enemy, attack_enemy_with_player,
    enemy_status
)

#############################################################

ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")

def human_xp_summary(player: Player) -> str:
    return f"{player.name}  |  Level {player.level}  |  XP {player.xp}"

class GameUI:
    # Just to initialize the screen
    def __init__(self, root):
        self.root = root
        self.root.title("RE:Clicker")
        self.root.geometry("720x720")
        self.root.configure(bg="#0f1115")

        # Style dark like Sunj Jinwoo......
        style = ttk.Style(self.root)
        style.theme_use("clam")
        style.configure("TFrame", background="#0f1115")
        style.configure("TLabel", background="#0f1115", foreground="#e6edf3", font=("Segoe UI", 11))
        style.configure("Title.TLabel", font=("Segoe UI Semibold", 14))
        style.configure("Sub.TLabel", foreground="#9aa4ad")
        style.configure("HP.Horizontal.TProgressbar", troughcolor="#1a1f29", background="#59d185")
        style.configure("XP.Horizontal.TProgressbar", troughcolor="#1a1f29", background="#7aa2f7")
        style.configure("TButton", background="#1f2633", foreground="#e6edf3")
        style.map("TButton", background=[("active", "#273040")])

        # State (start without pseudo)
        self.player = Player("", 0)
        self.enemy = create_random_enemy()

        # Slime' sprite
        self.images = {
            "Slime1": tk.PhotoImage(file=os.path.join(ASSETS_DIR, "Slime1.png")).zoom(5, 5),
            "Slime2": tk.PhotoImage(file=os.path.join(ASSETS_DIR, "Slime2.png")).zoom(5, 5),
            "Slime3": tk.PhotoImage(file=os.path.join(ASSETS_DIR, "Slime3.png")).zoom(5, 5),
        }

        # Layout
        root.columnconfigure(0, weight=1)
        main = ttk.Frame(root, padding=16)
        main.grid(row=0, column=0, sticky="nsew")
        main.columnconfigure(0, weight=1)

        # Title
        ttk.Label(main, text="RE:Clicker – The BEST Clicker RPG in Python with slime, a lot of slime...", style="Title.TLabel").grid(row=0, column=0, pady=(0,10))

        # Enemy card
        enemy_card = ttk.Frame(main, padding=12)
        enemy_card.grid(row=1, column=0, sticky="ew", pady=(0,14))
        enemy_card.columnconfigure(0, weight=1)

        self.enemy_img_label = ttk.Label(enemy_card, image=self.images[self.enemy.name])
        self.enemy_img_label.grid(row=0, column=0, pady=(4,8))

        self.enemy_text = tk.StringVar(value=enemy_status(self.enemy))
        ttk.Label(enemy_card, textvariable=self.enemy_text, style="Sub.TLabel").grid(row=1, column=0, pady=(0,6))

        self.hp_bar = ttk.Progressbar(enemy_card, style="HP.Horizontal.TProgressbar",
                                      orient="horizontal", length=360, mode="determinate",
                                      maximum=self.enemy.max_hp, value=self.enemy.hp)
        self.hp_bar.grid(row=2, column=0, pady=(2,8))

        # Buttons row (attack + reset)
        buttons_frame = ttk.Frame(main)
        buttons_frame.grid(row=2, column=0, pady=(4,12))

        self.attack_btn = ttk.Button(buttons_frame, text="Attack", command=self.on_attack)
        self.attack_btn.grid(row=0, column=0, padx=6)
        self.attack_btn.bind("<Key>", lambda e: "break")

        self.reset_btn = ttk.Button(buttons_frame, text="Reset", command=self.on_reset)
        self.reset_btn.grid(row=0, column=1, padx=6)

        # Player info / XP
        player_card = ttk.Frame(main, padding=12)
        player_card.grid(row=3, column=0, sticky="ew")
        player_card.columnconfigure(0, weight=1)

        self.player_text = tk.StringVar(value=human_xp_summary(self.player))
        ttk.Label(player_card, textvariable=self.player_text).grid(row=0, column=0, pady=(0,6))

        self.xp_bar = ttk.Progressbar(player_card, style="XP.Horizontal.TProgressbar",
                                      orient="horizontal", length=360, mode="determinate",
                                      maximum=100, value=(self.player.xp % 100))
        self.xp_bar.grid(row=1, column=0)

        # Ask pseudo at start
        self.root.after(100, self.ask_name)

    # Popup to ask pseudo
    def ask_name(self):
        popup = tk.Toplevel(self.root)
        popup.title("Choose your pseudo")
        popup.geometry("300x120")
        popup.configure(bg="#0f1115")

        tk.Label(popup, text="Enter your pseudo:", bg="#0f1115", fg="white").pack(pady=10)
        entry = tk.Entry(popup)
        entry.pack(pady=5)

        def confirm():
            name = entry.get().strip()
            if name:
                self.player.name = name
                self.player_text.set(human_xp_summary(self.player))
                popup.destroy()

        tk.Button(popup, text="OK", command=confirm).pack(pady=5)

    # Reset player to 0 XP + new pseudo
    def on_reset(self):
        self.player = Player("", 0)
        self.player_text.set(human_xp_summary(self.player))
        self.xp_bar.config(value=0)
        self.root.after(100, self.ask_name)

    # Actions
    def on_attack(self):
        dmg, dead, xp_gain = attack_enemy_with_player(self.player, self.enemy)

        self.enemy_text.set(f"{self.enemy.name} | HP: {self.enemy.hp} | {'Dead' if self.enemy.dead else 'Alive'}   (−{dmg})")
        self.hp_bar.config(maximum=self.enemy.max_hp, value=self.enemy.hp)

        if dead:
            self.player.add_xp_amount(xp_gain)
            self.player_text.set(human_xp_summary(self.player))
            self.xp_bar.config(value=(self.player.xp % 100))

            self.enemy = create_random_enemy()
            self.enemy_img_label.config(image=self.images[self.enemy.name])
            self.enemy_text.set(enemy_status(self.enemy))
            self.hp_bar.config(maximum=self.enemy.max_hp, value=self.enemy.hp)

# To put an appel on the main.py
def run():
    root = tk.Tk()
    GameUI(root)
    root.mainloop()
