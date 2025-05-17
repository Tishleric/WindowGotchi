"""Tests for Pet model."""

import unittest

from src.pet_model import (
    Pet,
    Stage,
    HATCH_TIME_MINUTES,
    MAX_AGE_MINUTES,
    MAX_CARE_MISTAKES,
)


class TestPetModel(unittest.TestCase):
    """Test cases for the Pet class."""

    def test_feed_meal(self) -> None:
        pet = Pet()
        pet.hunger_hearts = 3
        self.assertTrue(pet.feed("meal"))
        self.assertEqual(pet.hunger_hearts, 4)
        self.assertFalse(pet.feed("meal"))

    def test_feed_snack(self) -> None:
        pet = Pet()
        pet.happiness_hearts = 3
        pet.feed("snack")
        self.assertEqual(pet.happiness_hearts, 4)
        self.assertTrue(pet.weight > 5)

    def test_play_game(self) -> None:
        pet = Pet()
        pet.happiness_hearts = 2
        pet.play_game(3)
        self.assertEqual(pet.happiness_hearts, 3)
        self.assertLess(pet.weight, 5)

    def test_tick_evolution(self) -> None:
        pet = Pet()
        pet.tick(65)
        self.assertEqual(pet.stage, Stage.CHILD)

    def test_egg_hatches(self) -> None:
        pet = Pet()
        self.assertEqual(pet.stage, Stage.EGG)
        pet.tick(HATCH_TIME_MINUTES)
        self.assertEqual(pet.stage, Stage.BABY)

    def test_death_by_old_age(self) -> None:
        pet = Pet()
        pet.stage = Stage.ADULT
        pet.age_minutes = MAX_AGE_MINUTES
        pet.tick(1)
        self.assertEqual(pet.stage, Stage.DEAD)

    def test_death_by_care_mistakes(self) -> None:
        pet = Pet()
        pet.care_mistakes = MAX_CARE_MISTAKES + 1
        pet.tick(1)
        self.assertEqual(pet.stage, Stage.DEAD)


if __name__ == "__main__":
    unittest.main()
