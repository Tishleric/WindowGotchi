"""Notification manager with optional system tray integration."""

from __future__ import annotations

import threading
from typing import Callable, Dict, Optional

try:  # Optional dependency for desktop notifications
    from plyer import notification as plyer_notification
except Exception:  # pragma: no cover - library may be missing
    plyer_notification = None

try:  # Optional dependency for tray icon
    import pystray
    from PIL import Image, ImageDraw
except Exception:  # pragma: no cover - library may be missing
    pystray = None  # type: ignore
    Image = ImageDraw = None  # type: ignore


class NotificationManager:
    """Manage system notifications and tray status."""

    def __init__(self) -> None:
        self.last_notification: Optional[tuple[str, str]] = None
        self.tray_status: Optional[str] = None
        self._tray_icon: Optional["pystray.Icon"] = None
        self._tray_actions: Dict[str, Callable[[], None]] = {}

    # ------------------------------------------------------------------
    # Notification handling
    # ------------------------------------------------------------------
    def _send_os_notification(self, title: str, message: str) -> None:
        """Send a notification using plyer if available."""

        if plyer_notification is not None:
            plyer_notification.notify(
                title=title,
                message=message,
                app_name="WindowGotchi",
                timeout=5,
            )

    def notify(self, title: str, message: str) -> None:
        """Record and dispatch a notification."""

        self.last_notification = (title, message)
        self._send_os_notification(title, message)
        print(f"[Notify] {title}: {message}")

    # ------------------------------------------------------------------
    # Tray handling
    # ------------------------------------------------------------------
    def update_tray(self, status: str) -> None:
        """Update tray status and tooltip if tray is running."""

        self.tray_status = status
        print(f"[Tray] Status set to: {status}")
        if self._tray_icon is not None:
            self._tray_icon.title = f"WindowGotchi - {status}"

    def add_quick_action(self, name: str, callback: Callable[[], None]) -> None:
        """Register a quick action for the tray icon."""

        self._tray_actions[name] = callback
        if self._tray_icon is not None:
            self._tray_icon.menu = self._build_menu()

    # ------------------------------------------------------------------
    # Tray icon management helpers
    # ------------------------------------------------------------------
    def _build_menu(self) -> "pystray.Menu":
        """Create a pystray Menu from registered actions."""

        if pystray is None:
            raise RuntimeError("pystray is not available")
        items = [pystray.MenuItem(name, action) for name, action in self._tray_actions.items()]
        return pystray.Menu(*items) if items else pystray.Menu()

    def _create_default_icon(self) -> "Image.Image":
        """Create a simple icon image for the tray."""

        if Image is None:
            raise RuntimeError("Pillow is not available")
        image = Image.new("RGB", (16, 16), "white")
        draw = ImageDraw.Draw(image)
        draw.rectangle((0, 0, 15, 15), fill="black")
        return image

    def start_tray_icon(self) -> None:
        """Start the system tray icon if dependencies are available."""

        if pystray is None or Image is None:
            print("[Tray] pystray or Pillow not available; tray icon disabled")
            return
        if self._tray_icon is not None:
            return
        icon_image = self._create_default_icon()
        self._tray_icon = pystray.Icon(
            "WindowGotchi",
            icon_image,
            title="WindowGotchi",
            menu=self._build_menu(),
        )
        threading.Thread(target=self._tray_icon.run, daemon=True).start()

    def stop_tray_icon(self) -> None:
        """Stop and remove the tray icon if running."""

        if self._tray_icon is not None:
            self._tray_icon.stop()
            self._tray_icon = None
