"""Tests for managers."""

import unittest
from unittest.mock import patch


from src.audio_manager import AudioManager
from src.notification_manager import NotificationManager


class TestNotificationManager(unittest.TestCase):
    def test_notify_and_tray(self) -> None:
        nm = NotificationManager()

        with patch.object(nm, "_send_os_notification") as mock_send:
            nm.notify("title", "msg")
            mock_send.assert_called_once_with("title", "msg")

        self.assertEqual(nm.last_notification, ("title", "msg"))
        nm.update_tray("hungry")
        self.assertEqual(nm.tray_status, "hungry")


class TestAudioManager(unittest.TestCase):
    def test_play_and_mute(self) -> None:
        am = AudioManager()
        am.play_sound("feed")
        self.assertEqual(am.last_sound, "feed")
        am.mute()
        am.play_sound("alert")
        self.assertEqual(am.last_sound, "feed")
        am.unmute()
        am.play_sound("alert")
        self.assertEqual(am.last_sound, "alert")


if __name__ == "__main__":
    unittest.main()
