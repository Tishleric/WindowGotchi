"""Simplified audio manager."""


class AudioManager:
    """Manage sound playback."""

    def __init__(self) -> None:
        self.muted = False
        self.last_sound = None

    def play_sound(self, sound_name: str) -> None:
        """Play a sound if not muted."""
        if self.muted:
            return
        self.last_sound = sound_name
        print(f"[Sound] Played sound: {sound_name}")

    def mute(self) -> None:
        """Mute sounds."""
        self.muted = True

    def unmute(self) -> None:
        """Unmute sounds."""
        self.muted = False
