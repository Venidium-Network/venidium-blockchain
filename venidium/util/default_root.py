import os
from pathlib import Path

DEFAULT_ROOT_PATH = Path(os.path.expanduser(os.getenv("VENIDIUM_ROOT", "~/.venidium/mainnet"))).resolve()

DEFAULT_KEYS_ROOT_PATH = Path(os.path.expanduser(os.getenv("VENIDIUM_KEYS_ROOT", "~/.venidium_keys"))).resolve()
