"""Pet model module for WindowGotchi."""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict
import random


class Stage(Enum):
    """Life stages for the pet."""

    EGG = "Egg"
    BABY = "Baby"
    CHILD = "Child"
    TEEN = "Teen"
    ADULT = "Adult"
    DEAD = "Dead"


@dataclass
class Pet:
    """Represents a virtual pet and its state."""

    age_minutes: int = 0
    stage: Stage = Stage.EGG
    hunger_hearts: int = 4
    happiness_hearts: int = 4
    discipline_percent: int = 0
    weight: int = 5
    care_mistakes: int = 0
    is_sick: bool = False
    poop_count: int = 0

    minutes_since_last_hunger: int = field(default=0, init=False)
    minutes_since_last_happy: int = field(default=0, init=False)
    minutes_since_last_poop: int = field(default=0, init=False)
    medicine_doses_left: int = field(default=0, init=False)

    def tick(self, minutes: int = 1) -> None:
        """Advance time for the pet by the given number of minutes."""
        for _ in range(minutes):
            self.age_minutes += 1
            self.minutes_since_last_hunger += 1
            self.minutes_since_last_happy += 1
            self.minutes_since_last_poop += 1

            if self.minutes_since_last_hunger >= 60:
                if self.hunger_hearts > 0:
                    self.hunger_hearts -= 1
                self.minutes_since_last_hunger = 0
                if self.hunger_hearts == 0:
                    self.care_mistakes += 1

            if self.minutes_since_last_happy >= 70:
                if self.happiness_hearts > 0:
                    self.happiness_hearts -= 1
                self.minutes_since_last_happy = 0
                if self.happiness_hearts == 0:
                    self.care_mistakes += 1

            if self.minutes_since_last_poop >= 180:
                self.poop_count += 1
                self.minutes_since_last_poop = 0

            if (self.poop_count >= 3 or self.weight > 20) and not self.is_sick:
                self.is_sick = True
                self.medicine_doses_left = random.choice([1, 2])

            self._maybe_evolve()

    def feed(self, food_type: str) -> bool:
        """Feed the pet a meal or snack."""
        if food_type == "meal":
            if self.hunger_hearts >= 4:
                return False
            self.hunger_hearts += 1
            self.weight += 1
            return True
        if food_type == "snack":
            if self.happiness_hearts < 4:
                self.happiness_hearts += 1
            self.weight += 2
            if self.weight > 20 and not self.is_sick:
                self.is_sick = True
                self.medicine_doses_left = random.choice([1, 2])
            return True
        return False

    def play_game(self, rounds_won: int) -> None:
        """Play a game with the pet."""
        if rounds_won >= 3 and self.happiness_hearts < 4:
            self.happiness_hearts += 1
        if self.weight > 1:
            self.weight -= 1

    def clean_poop(self) -> None:
        """Clean all poop from the pet area."""
        self.poop_count = 0

    def give_medicine(self) -> None:
        """Cure the pet if it is sick."""
        if self.is_sick:
            if self.medicine_doses_left > 0:
                self.medicine_doses_left -= 1
            if self.medicine_doses_left <= 0:
                self.is_sick = False

    def discipline(self) -> None:
        """Discipline the pet."""
        self.discipline_percent = min(100, self.discipline_percent + 25)

    def _maybe_evolve(self) -> None:
        """Handle stage evolution based on age."""
        if self.stage == Stage.EGG and self.age_minutes >= 5:
            self.stage = Stage.BABY
        elif self.stage == Stage.BABY and self.age_minutes >= 65:
            self.stage = Stage.CHILD
        elif self.stage == Stage.CHILD and self.age_minutes >= 3 * 24 * 60:
            self.stage = Stage.TEEN
        elif self.stage == Stage.TEEN and self.age_minutes >= 6 * 24 * 60:
            self.stage = Stage.ADULT

    def to_dict(self) -> Dict[str, object]:
        """Return a dictionary representing this pet."""
        return {
            "age_minutes": self.age_minutes,
            "stage": self.stage.value,
            "hunger_hearts": self.hunger_hearts,
            "happiness_hearts": self.happiness_hearts,
            "discipline_percent": self.discipline_percent,
            "weight": self.weight,
            "care_mistakes": self.care_mistakes,
            "is_sick": self.is_sick,
            "poop_count": self.poop_count,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, object]) -> "Pet":
        """Create a Pet from saved data."""
        pet = cls()
        pet.age_minutes = int(data.get("age_minutes", 0))
        pet.stage = Stage(data.get("stage", Stage.EGG.value))
        pet.hunger_hearts = int(data.get("hunger_hearts", 4))
        pet.happiness_hearts = int(data.get("happiness_hearts", 4))
        pet.discipline_percent = int(data.get("discipline_percent", 0))
        pet.weight = int(data.get("weight", 5))
        pet.care_mistakes = int(data.get("care_mistakes", 0))
        pet.is_sick = bool(data.get("is_sick", False))
        pet.poop_count = int(data.get("poop_count", 0))
        return pet
