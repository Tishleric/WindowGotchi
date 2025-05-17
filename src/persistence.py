"""Persistence utilities for WindowGotchi."""

import json
import os
from typing import Optional

from .pet_model import Pet

DEFAULT_SAVE_PATH = os.path.join(os.path.expanduser("~"), ".windowgotchi", "pet_state.json")


def save_pet(pet: Pet, filepath: Optional[str] = None) -> None:
    """Save pet state to JSON file."""
    path = filepath or DEFAULT_SAVE_PATH
    directory = os.path.dirname(path) or "."
    os.makedirs(directory, exist_ok=True)
    temp_path = path + ".tmp"
    with open(temp_path, "w", encoding="utf-8") as f:
        json.dump(pet.to_dict(), f)
    os.replace(temp_path, path)


def load_pet(filepath: Optional[str] = None) -> Pet:
    """Load pet state from JSON file."""
    path = filepath or DEFAULT_SAVE_PATH
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return Pet.from_dict(data)
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        return Pet()
