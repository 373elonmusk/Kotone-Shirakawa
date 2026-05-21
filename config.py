import os

# ─── Telegram Bot Credentials ───────────────────────────────────────────────
BOT_TOKEN       = os.environ.get("BOT_TOKEN", "")
TELEGRAM_API    = os.environ.get("TELEGRAM_API", "")
TELEGRAM_HASH   = os.environ.get("TELEGRAM_HASH", "")
ADMINS          = list(map(int, os.environ.get("ADMINS", "5864846606").split()))

# ─── Channel / Chat IDs ─────────────────────────────────────────────────────
FSUB_ID         = int(os.environ.get("FSUB_ID", "0"))
DUMP_CHAT_ID    = int(os.environ.get("DUMP_CHAT_ID", "0"))

# ─── Database (MongoDB) ─────────────────────────────────────────────────────
DB_URI          = os.environ.get("DB_URI", "")      # Render env var: DB_URI
DB_NAME         = os.environ.get("DB_NAME", "terabot")

# ─── Shortlink / Token Verification ─────────────────────────────────────────
SHORTLINK_URL   = os.environ.get("SHORTLINK_URL", "ziplinker.net")
SHORTLINK_API   = os.environ.get("SHORTLINK_API", "")
VERIFY_EXPIRE   = int(os.environ.get("VERIFY_EXPIRE", 43200))   # seconds (default 12 hrs)
IS_VERIFY       = os.environ.get("IS_VERIFY", "True").lower() == "true"
TUT_VID         = os.environ.get("TUT_VID", "https://t.me/ultroid_official/18")
