import os
from dotenv import load_dotenv

load_dotenv()

# Bot Token (from environment variables)
BOT_TOKEN = os.getenv("BOT_TOKEN", "8518786655:AAE2lcfvoVXP9TvbGs_4U1soFWqWIUJZ52s")

# Channel and link configuration
TELEGRAM_CHANNEL = os.getenv("TELEGRAM_CHANNEL", "https://t.me/IPAY9AUS")
FREE_SPIN_URL = os.getenv("FREE_SPIN_URL", "https://ipay9aud.com/RFIPAY9BOT1")
FREE_CREDIT_URL = os.getenv("FREE_CREDIT_URL", "https://ipay9aud.com/RFIPAY9BOT1")

# Promotional images (local file paths - hardcoded in code)
FREE_SPIN_IMAGE_PATH = "public/free_spin.jpg"
HOT_GAME_TIPS_IMAGE_PATH = "public/hot_game_tips.jpg"

# Bot information
BOT_NAME = "Ipay9 Promo Bot"
BOT_DESCRIPTION = "Ipay9 Marketing Assistant - Provides latest promotions and event information"
