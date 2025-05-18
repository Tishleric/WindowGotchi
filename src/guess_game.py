"""Simple left/right guessing game logic."""

from __future__ import annotations

import random
from typing import List, Optional, Tuple


class DirectionGuessGame:
    """Game logic for guessing left or right."""

    def __init__(self, rounds: int = 5, directions: Optional[List[str]] = None) -> None:
        self.rounds = rounds
        self.directions = directions or []
        self.current_round = 0
        self.rounds_won = 0

    def _next_direction(self) -> str:
        if self.current_round < len(self.directions):
            return self.directions[self.current_round]
        return random.choice(["left", "right"])

    def play_round(self, guess: str) -> Tuple[bool, str]:
        """Play a single round. Returns (won, correct_direction)."""
        if self.current_round >= self.rounds:
            raise ValueError("Game is already over")

        correct = self._next_direction()
        won = guess.lower() == correct
        if won:
            self.rounds_won += 1
        self.current_round += 1
        return won, correct

    def is_over(self) -> bool:
        """Return True if the game has finished."""
        return self.current_round >= self.rounds
