"""Timer service to update the pet at regular intervals."""

import threading
import time
from typing import Optional

from .pet_model import Pet


class PetTimer:
    """Background timer that calls `Pet.tick`."""

    def __init__(self, pet: Pet, interval_seconds: int = 60) -> None:
        self.pet = pet
        self.interval = interval_seconds
        self._stop_event = threading.Event()
        self._thread: Optional[threading.Thread] = None

    def _run(self) -> None:
        while not self._stop_event.wait(self.interval):
            minutes = max(1, int(self.interval / 60))
            self.pet.tick(minutes=minutes)

    def start(self) -> None:
        """Start the timer."""
        if self._thread and self._thread.is_alive():
            return
        self._stop_event.clear()
        self._thread = threading.Thread(target=self._run, daemon=True)
        self._thread.start()

    def stop(self) -> None:
        """Stop the timer."""
        self._stop_event.set()
        if self._thread:
            self._thread.join()
            self._thread = None
