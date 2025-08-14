import os
import sys
import shlex
import subprocess
from typing import Tuple

from config import get_settings


Settings = get_settings()


def is_windows() -> bool:
    return sys.platform.startswith("win")


def open_app(app_name: str) -> Tuple[bool, str]:
    name = app_name.strip().lower()
    exe = Settings.windows_apps.get(name) if is_windows() else Settings.linux_apps.get(name)

    if not exe:
        return False, f"Unknown app: {app_name}. Configure it in settings."

    try:
        if is_windows():
            # Use 'start' via cmd to respect PATH and app associations
            cmd = f'start "" {shlex.quote(exe)}'
            subprocess.Popen(cmd, shell=True)
        else:
            subprocess.Popen([exe])
        return True, f"Opened {app_name}."
    except Exception as exc:
        return False, f"Failed to open {app_name}: {exc}"


def close_app(app_name: str) -> Tuple[bool, str]:
    name = app_name.strip().lower()
    exe = Settings.windows_apps.get(name) if is_windows() else Settings.linux_apps.get(name)

    if not exe:
        return False, f"Unknown app: {app_name}. Configure it in settings."

    try:
        if is_windows():
            # Force close by image name
            cmd = ["taskkill", "/IM", exe, "/F"]
            proc = subprocess.run(cmd, capture_output=True, text=True)
            if proc.returncode == 0:
                return True, f"Closed {app_name}."
            return False, proc.stderr.strip() or proc.stdout.strip() or f"Failed to close {app_name}."
        else:
            # Best-effort kill by name
            cmd = ["pkill", "-f", exe]
            proc = subprocess.run(cmd, capture_output=True, text=True)
            if proc.returncode == 0:
                return True, f"Closed {app_name}."
            return False, proc.stderr.strip() or proc.stdout.strip() or f"Failed to close {app_name}."
    except Exception as exc:
        return False, f"Failed to close {app_name}: {exc}"