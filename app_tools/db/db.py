from pathlib import Path

from peewee import *

from .paths import DATA_DIR

db_path = Path(DATA_DIR) / "veil.db"
db = SqliteDatabase(
    db_path,
    pragmas={
        "journal_mode": "wal",
        "foreign_keys": 1,
        "cache_size": -64_000,  # 64MB
    }
)
