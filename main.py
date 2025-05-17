#!/usr/bin/env python3
"""Simple Tkinter-based WindowGotchi application."""

import tkinter as tk

from src.audio_manager import AudioManager
from src.notification_manager import NotificationManager
from src.persistence import load_pet, save_pet
from src.pet_model import Pet
from src.timer_service import PetTimer
from src.game_window import GuessGameWindow


class WindowGotchiApp:
    """Main application class."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.pet: Pet = load_pet()
        self.nm = NotificationManager()
        self.am = AudioManager()
        self.status = tk.StringVar()
        tk.Label(root, textvariable=self.status, font=("Courier", 12)).pack(pady=10)
        btn_frame = tk.Frame(root)
        btn_frame.pack()
        tk.Button(btn_frame, text="Feed Meal", command=self.feed_meal).pack(side=tk.LEFT)
        tk.Button(btn_frame, text="Feed Snack", command=self.feed_snack).pack(side=tk.LEFT)
        tk.Button(btn_frame, text="Play", command=self.play).pack(side=tk.LEFT)
        tk.Button(btn_frame, text="Clean", command=self.clean).pack(side=tk.LEFT)
        tk.Button(btn_frame, text="Medicine", command=self.medicine).pack(side=tk.LEFT)
        self.timer = PetTimer(self.pet, interval_seconds=60)
        self.timer.start()
        self.update_status()
        root.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self) -> None:
        self.timer.stop()
        save_pet(self.pet)
        self.root.destroy()

    def update_status(self) -> None:
        self.status.set(
            f"Stage: {self.pet.stage.value} Age(min): {self.pet.age_minutes}\n"
            f"Hungry: {self.pet.hunger_hearts}/4 Happy: {self.pet.happiness_hearts}/4\n"
            f"Weight: {self.pet.weight} Poop: {self.pet.poop_count}"
        )
        if self.pet.hunger_hearts == 0 or self.pet.happiness_hearts == 0:
            self.nm.notify("WindowGotchi", "Needs attention!")
            self.am.play_sound("alert")
        self.root.after(10000, self.update_status)

    def feed_meal(self) -> None:
        if self.pet.feed("meal"):
            self.am.play_sound("feed")
        else:
            self.am.play_sound("deny")
        self.update_status()

    def feed_snack(self) -> None:
        self.pet.feed("snack")
        self.am.play_sound("snack")
        self.update_status()

    def play(self) -> None:
        self.am.play_sound("game")
        GuessGameWindow(self.root, self.pet, on_close=self.update_status)

    def clean(self) -> None:
        self.pet.clean_poop()
        self.am.play_sound("clean")
        self.update_status()

    def medicine(self) -> None:
        self.pet.give_medicine()
        self.am.play_sound("medicine")
        self.update_status()


def main() -> None:
    root = tk.Tk()
    root.title("WindowGotchi")
    WindowGotchiApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
