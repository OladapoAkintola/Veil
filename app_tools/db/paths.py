from pathlib import Path

from platformdirs import PlatformDirs

app = PlatformDirs(
    appname="Veil",
    version="1.0",
    appauthor="Akintola Oladapo",
)

DATA_DIR = Path(app.user_data_dir) / "data"
CACHE_DIR = Path(app.user_cache_dir) / "cache"
ENCRYPTION_DIR = DATA_DIR / "data" / "encryption"
ENCRYPTION_DIR.mkdir(parents=True, exist_ok=True)
CACHE_DIR.mkdir(parents=True, exist_ok=True)
