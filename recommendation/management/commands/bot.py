from django.core.management.base import BaseCommand
from recommendation.bot import bot
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "starts bot, wrtting in aiogram"

    def handle(self, *args, **options):
        while True:
            try:
                bot.polling()
            except KeyboardInterrupt:
                break
            except Exception as e:
                logging.exception(e)
