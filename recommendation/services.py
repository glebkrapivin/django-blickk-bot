### for dumb testing like python recommendations/services.py
import os
import sys

sys.path.append('/Users/gkrapivin/django-blick-bot/django_blickk_bot')
os.environ["DJANGO_SETTINGS_MODULE"] = "django_blickk_bot.settings"
import django

django.setup()
######

from recommendation.models import UserSession, User, SessionQuestion, Category, Question, Recommendation
from typing import Union
import json
from django.core.exceptions import ObjectDoesNotExist
import logging

logger = logging.getLogger(__name__)


class UserService:
    def __init__(self, user_id: int, properties: dict = None) -> None:
        self.user, was_created = User.objects.get_or_create(tg_id=user_id)
        self.properties = properties or {}

    def set_properties(self) -> None:
        self.user.properties = json.dumps(self.properties)
        self.user.save()


class UserSessionService:
    def __init__(self, message_id: int, user: UserService) -> None:
        print(user.user)
        self.session, was_created = UserSession.objects.get_or_create(message_id=message_id, user=user.user)
        self.categories = Category.objects.all()
        self.questions = self.session.sessionquestion_set
        if not self.questions.count():
            self.add_session_questions()

    def add_session_questions(self) -> None:
        for category in self.categories:
            question = Question.objects.filter(category=category).order_by('?').first()
            if question:
                SessionQuestion(user_session=self.session, question=question).save()

    @property
    def has_next_question(self):
        return self.questions.filter(answer=None).count() > 0

    def get_next_question(self) -> SessionQuestion:
        "returns next question and marks it as a current one"
        for question in self.questions.all():
            if not question.answer:
                question.is_current = True
                question.save()
                return question

    def get_current_question(self) -> SessionQuestion:
        for question in self.questions.all():
            if question.is_current:
                return question

    @staticmethod
    def set_answer(session_question: SessionQuestion, text_answer: str) -> None:
        question = session_question.question
        try:
            answer = question.questionanswer_set.filter(text=text_answer).get()
        except ObjectDoesNotExist as e:
            logger.exception(e)
            return
        session_question.answer = answer
        session_question.is_current = False
        session_question.save()

    def get_recommendation(self) -> Recommendation:
        return 'NOT IMPL'

    def step(self, user_input: str = None) -> Union[SessionQuestion, Recommendation]:
        if not user_input:
            return self.get_next_question()

        current_question = self.get_current_question()
        if current_question:
            self.set_answer(current_question, user_input)

        if self.has_next_question:
            return self.get_next_question()
        else:
            return self.get_recommendation()


# logging.basicConfig()
# s = UserSessionService(message_id=1233324, user=UserService(user_id=1234))
# print(s.step())
# s.step('Russia')
# print(s.step('fowijfiowejf'))
