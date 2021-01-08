# for dumb testing like python recommendations/services.py

import os
import sys
import json
import logging
import random
from typing import Union

import django
from django.core.exceptions import ObjectDoesNotExist

from recommendation.models import (
    UserSession,
    User,
    SessionQuestion,
    Category, Question,
    Recommendation,
    MovieCategoryState,
    Movie
)

DEFAULT_COEFF = 0.5

sys.path.append('/Users/gkrapivin/django-blick-bot/django_blickk_bot')
os.environ["DJANGO_SETTINGS_MODULE"] = "django_blickk_bot.settings"

django.setup()
######


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
        self.movies = Movie.objects.all()
        self.movie_recommendations = [
            Recommendation(user_session=self.session, movie=movie)
            for movie in self.movies
        ]
        print(self.session.user.properties)
        if self.session.user.properties:
            self.properties = json.loads(self.session.user.properties)
        else:
            self.properties = {}
        self.recommendations_queue = []
        self.movie_weights = []

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

    def _set_movie_weights(self):
        mask = [1.0 for _ in self.movies]
        for idx, movie in enumerate(self.movies):
            for property_name, property_dict in self.properties.items():
                coeff_ = property_dict.get('coeff', DEFAULT_COEFF)
                matching_properties = MovieCategoryState.objects.filter(
                    movie=movie,
                    state=property_dict.get('value', ''),
                    category=property_name
                )
                if not matching_properties:
                    coeff_ = 1 - coeff_
                mask[idx] *= coeff_
        self.movie_weights = mask

    def _set_recommendation_queue(self):
        movie_weights = self.movie_weights.copy()
        movies_idx = list(range(len(self.movies)))
        for _ in movies_idx:
            cur_choice = random.choices(movies_idx, weights=movie_weights, k=1)[0]
            cur_recommendation = self.movie_recommendations[cur_choice]
            self.recommendations_queue.append(cur_recommendation)
            movie_weights[cur_choice] = 0

    def get_recommendation(self) -> Recommendation:
        if not self.movie_weights:
            self._set_movie_weights()
        if not self.recommendations_queue:
            self._set_recommendation_queue()
        print(self.recommendations_queue)
        recommendation = self.recommendations_queue.pop(0)
        return recommendation

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
