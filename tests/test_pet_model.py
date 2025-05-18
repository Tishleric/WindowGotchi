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

    def test_initial_stage(self) -> None:
        pet = Pet()
        self.assertEqual(pet.stage, Stage.EGG)

    def test_hatch_after_five_minutes(self) -> None:
        pet = Pet()
        pet.tick(5)
        self.assertEqual(pet.stage, Stage.BABY)

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


    def test_tick_sickness_from_poop(self) -> None:
        pet = Pet()
        pet.poop_count = 3
        with patch('random.choice', return_value=1):
            pet.tick()
        self.assertTrue(pet.is_sick)
        self.assertEqual(pet.medicine_doses_left, 1)

    def test_tick_sickness_from_weight(self) -> None:
        pet = Pet()
        pet.weight = 25
        with patch('random.choice', return_value=2):
            pet.tick()
        self.assertTrue(pet.is_sick)
        self.assertEqual(pet.medicine_doses_left, 2)

    def test_medicine_two_doses(self) -> None:
        pet = Pet()
        pet.is_sick = True
        pet.medicine_doses_left = 2
        pet.give_medicine()
        self.assertTrue(pet.is_sick)
        pet.give_medicine()
        self.assertFalse(pet.is_sick)

    def test_medicine_single_dose(self) -> None:
        pet = Pet()
        pet.is_sick = True
        pet.medicine_doses_left = 1
        pet.give_medicine()
        self.assertFalse(pet.is_sick)



if __name__ == "__main__":
    unittest.main()
