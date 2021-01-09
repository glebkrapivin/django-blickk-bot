import os
import sys
from pathlib import Path

import dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

dotenv.load_dotenv(Path(BASE_DIR, 'settings', 'env'))

BOT_TOKEN = os.getenv('BOT_TOKEN')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

sys.path.append('/Users/nikolai/projects/django-blick-bot/django_blickk_bot')
os.environ["DJANGO_SETTINGS_MODULE"] = "django_blickk_bot.settings"
