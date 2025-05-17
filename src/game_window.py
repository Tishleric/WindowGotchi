"""Tkinter UI for the direction guessing game."""

from __future__ import annotations

import tkinter as tk

from .guess_game import DirectionGuessGame
from .pet_model import Pet


class GuessGameWindow:
    """A simple left/right guessing game window."""

    def __init__(self, parent: tk.Tk, pet: Pet, rounds: int = 5, on_close=None) -> None:
        self.pet = pet
        self.game = DirectionGuessGame(rounds=rounds)
        self.on_close = on_close

        self.win = tk.Toplevel(parent)
        self.win.title("Guess Game")

        tk.Label(self.win, text="Guess my direction!").pack(pady=5)
        btn_frame = tk.Frame(self.win)
        btn_frame.pack()
        tk.Button(btn_frame, text="Left", width=10, command=lambda: self.make_guess("left")).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Right", width=10, command=lambda: self.make_guess("right")).pack(side=tk.LEFT, padx=5)
        self.feedback = tk.StringVar()
        tk.Label(self.win, textvariable=self.feedback).pack(pady=5)

    def make_guess(self, guess: str) -> None:
        won, correct = self.game.play_round(guess)
        if won:
            self.feedback.set(f"Correct! It was {correct}.")
        else:
            self.feedback.set(f"Wrong! It was {correct}.")

        if self.game.is_over():
            self.pet.play_game(self.game.rounds_won)
            if self.on_close:
                self.on_close()
            tk.Button(self.win, text="Close", command=self.win.destroy).pack(pady=5)
            # Disable buttons
            for child in self.win.winfo_children():
                if isinstance(child, tk.Frame):
                    for btn in child.winfo_children():
                        btn.configure(state=tk.DISABLED)

