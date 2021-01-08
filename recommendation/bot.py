from settings.config import BOT_TOKEN
from recommendation.services import UserSessionService, UserService
from recommendation.models import SessionQuestion, Recommendation, Message
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from typing import List

bot = telebot.TeleBot(BOT_TOKEN)

INTRO_TEXT = "Привет, хотите получить четкую рекомендацию фильмов?"
INTRO_ANSWERS = ["Начать!"]

START_OVER = 'Начать с начала'
WANT_MORE = "Хочу еще"
RECOMMENDATION_ANSWERS = [START_OVER, WANT_MORE]


def gen_markup(answers: List[str]) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    markup.row_width = len(answers)
    for answer in answers:
        markup.add(InlineKeyboardButton(answer, callback_data=answer))
    return markup


@bot.message_handler(commands=["start"])
def send_welcome(message: telebot.types.Message):
    """Answer first message when user just starts the bot with an introduction"""
    bot.send_message(
        message.chat.id, INTRO_TEXT, reply_markup=gen_markup(INTRO_ANSWERS)
    )


@bot.callback_query_handler(func=lambda call: True)
def edit_message(call: telebot.types.CallbackQuery):
    user_id = call.from_user.id
    user = UserService(user_id=user_id)
    message_id = call.message.message_id
    chat_id = call.message.chat.id
    if call.data == START_OVER:
        bot.send_message(
            call.message.chat.id,
            INTRO_TEXT,
            reply_markup=gen_markup(INTRO_ANSWERS),
        )
    session = UserSessionService(message_id=message_id, user=user)
    q = session.step(call.data)

    # simple way to log messages, coming from user
    # change from call.data to raw json coming from api for later analysis
    msg = Message(session=session.session, payload=call.data)
    msg.save()

    ## Надо еще чето сделать, если вдруг такое же сообщение прилетает
    # он типа не меняет его и тогда все крашитс, надо посмотреть, как отлавливать
    if isinstance(q, SessionQuestion):
        text = q.get_text()
        answers = q.get_answers()
        bot.edit_message_text(
            text,
            chat_id=chat_id,
            message_id=message_id,
            reply_markup=gen_markup(answers),
        )
    else:
        from random import randint
        bot.edit_message_text(
            "Here is recommendation" + str(randint(1, 100)),
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=gen_markup(RECOMMENDATION_ANSWERS),
        )


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
