"""Tests for Pet model."""

import unittest

from src.pet_model import Pet, Stage


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

    def test_misbehavior_increases_care_mistake(self) -> None:
        pet = Pet()
        pet.tick(30)  # triggers misbehavior
        self.assertTrue(pet.misbehaving)
        pet.tick(10)  # ignore for too long
        self.assertFalse(pet.misbehaving)
        self.assertEqual(pet.care_mistakes, 1)

    def test_discipline_clears_misbehavior(self) -> None:
        pet = Pet()
        pet.tick(30)
        pet.discipline()
        self.assertFalse(pet.misbehaving)
        self.assertGreater(pet.discipline_percent, 0)


if __name__ == "__main__":
    unittest.main()
