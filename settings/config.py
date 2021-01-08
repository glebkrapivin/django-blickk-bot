import os
from pathlib import Path

import dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

dotenv.load_dotenv(Path(BASE_DIR, 'settings', 'env'))

BOT_TOKEN = os.getenv('BOT_TOKEN')
