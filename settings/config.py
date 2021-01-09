import os
import sys
from pathlib import Path

import dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

dotenv.load_dotenv(Path(BASE_DIR, 'settings', 'env'))

BOT_TOKEN = os.getenv('BOT_TOKEN')

sys.path.append('/Users/nikolai/projects/django-blick-bot/django_blickk_bot')
os.environ["DJANGO_SETTINGS_MODULE"] = "django_blickk_bot.settings"
