"""Simplified notification manager."""


class NotificationManager:
    """Manage notifications and tray status."""

    def __init__(self) -> None:
        self.last_notification = None
        self.tray_status = None

    def notify(self, title: str, message: str) -> None:
        """Record a notification."""
        self.last_notification = (title, message)
        print(f"[Notify] {title}: {message}")

    def update_tray(self, status: str) -> None:
        """Update tray status."""
        self.tray_status = status
        print(f"[Tray] Status set to: {status}")
