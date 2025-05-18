"""Tests for the guessing game logic."""

import unittest

from src.guess_game import DirectionGuessGame


class TestDirectionGuessGame(unittest.TestCase):
    """Test cases for DirectionGuessGame."""

    def test_rounds_and_wins(self) -> None:
        game = DirectionGuessGame(rounds=3, directions=["left", "right", "right"])
        self.assertFalse(game.is_over())

        won, correct = game.play_round("left")
        self.assertTrue(won)
        self.assertEqual(correct, "left")
        self.assertEqual(game.rounds_won, 1)

        won, correct = game.play_round("left")
        self.assertFalse(won)
        self.assertEqual(correct, "right")
        self.assertEqual(game.rounds_won, 1)

        won, correct = game.play_round("right")
        self.assertTrue(won)
        self.assertEqual(correct, "right")
        self.assertTrue(game.is_over())
        self.assertEqual(game.rounds_won, 2)

        with self.assertRaises(ValueError):
            game.play_round("left")


if __name__ == "__main__":
    unittest.main()
