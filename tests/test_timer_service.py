"""Tests for timer service."""

import time
import unittest

from src.pet_model import Pet
from src.timer_service import PetTimer


class TestPetTimer(unittest.TestCase):
    """Test the PetTimer class."""

    def test_timer_ticks(self) -> None:
        pet = Pet()
        timer = PetTimer(pet, interval_seconds=0.1)
        timer.start()
        time.sleep(0.25)
        timer.stop()
        self.assertGreater(pet.age_minutes, 0)


if __name__ == "__main__":
    unittest.main()
