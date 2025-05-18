"""Tests for persistence utilities."""

import os
import unittest


from src.pet_model import Pet, Stage

from src.persistence import load_pet, save_pet


class TestPersistence(unittest.TestCase):
    """Test saving and loading."""

    def setUp(self) -> None:
        self.path = "test_state.json"
        if os.path.exists(self.path):
            os.remove(self.path)

    def tearDown(self) -> None:
        if os.path.exists(self.path):
            os.remove(self.path)

    def test_save_and_load(self) -> None:
        pet = Pet()
        pet.hunger_hearts = 2
        save_pet(pet, self.path)
        loaded = load_pet(self.path)
        self.assertEqual(loaded.hunger_hearts, 2)

        self.assertEqual(loaded.stage, pet.stage)


    def test_load_new_when_missing(self) -> None:
        pet = load_pet(self.path)
        self.assertIsInstance(pet, Pet)

        self.assertEqual(pet.stage, Stage.EGG)



if __name__ == "__main__":
    unittest.main()
