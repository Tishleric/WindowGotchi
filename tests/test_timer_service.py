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

    def test_pause_and_resume(self) -> None:
        pet = Pet()
        timer = PetTimer(pet, interval_seconds=0.1)
        timer.start()
        time.sleep(0.15)
        timer.pause()
        age_after_pause = pet.age_minutes
        time.sleep(0.2)
        self.assertEqual(pet.age_minutes, age_after_pause)
        timer.resume()
        time.sleep(0.15)
        timer.stop()
        self.assertGreater(pet.age_minutes, age_after_pause)


if __name__ == "__main__":
    unittest.main()
