import os


def _require(key: str) -> str:
    val = os.environ.get(key)
    if not val:
        raise RuntimeError(f"Missing required environment variable: {key}")
    return val


# ── Telegram ──────────────────────────────────────────────────────────────────
API_ID: int = int(_require("31235022"))
API_HASH: str = _require("64a8cdb2c92d7ac433765af3e65dabb1")
BOT_TOKEN: str = _require("8667941299:AAFOilkpQZ0_9aCjpBHCIFVl0C5dytOVVy0")

# Optional: private channel ID for logging (e.g. -100123456789)
LOG_CHANNEL: int | None = int(os.environ["LOG_CHANNEL"]) if os.environ.get("LOG_CHANNEL") else None

# Developer profile URL shown in /start button
DEV_URL: str = os.environ.get("DEV_URL", "https://t.me/cantarella_wuwa")

# ── MongoDB ───────────────────────────────────────────────────────────────────
MONGO_URI: str = _require("mongodb+srv://Vasu:@Daemon990@cluster0.rv1vrmg.mongodb.net/?appName=Cluster0")
MONGO_DB: str = os.environ.get("MONGO_DB", "apple_music_bot")
