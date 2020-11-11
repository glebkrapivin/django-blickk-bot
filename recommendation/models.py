from django.db import models
from django.core.exceptions import ValidationError
from typing import List

class Category(models.Model):
    text = models.CharField(max_length=256)
    coef = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.text


class CategoryState(models.Model):
    text = models.CharField(max_length=256, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.category.text + ": " + self.text


class Question(models.Model):
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.text


class QuestionAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=256)
    value = models.ForeignKey(CategoryState, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def clean(self):
        category = self.question.category
        if category != self.value.category:
            raise ValidationError(
                f"question has category {category}, answer {self.value.category}"
            )

    def __str__(self):
        return self.text

class User(models.Model):
    tg_id = models.IntegerField(unique=True)
    properties = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return str(self.tg_id)

class UserSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message_id = models.IntegerField(unique=True)

    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return f"{self.user.tg_id}-{self.message_id}"

class SessionQuestion(models.Model):
    user_session = models.ForeignKey(UserSession, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(
        QuestionAnswer, on_delete=models.CASCADE, blank=True, null=True
    )
    is_current = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def get_answers(self) -> List[str]:
        return [q.text for q in self.question.questionanswer_set.all()]

    def get_text(self):
        return self.question.text

class Movie(models.Model):
    title = models.TextField()
    description = models.TextField()
    image_url = models.URLField()

    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.title


class MovieCategoryState(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    state = models.ForeignKey(CategoryState, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def clean(self):
        if self.state.category != self.category:
            raise ValidationError(
                f"movie has category {self.category}, state {self.state.category}"
            )

class Recommendation(models.Model):
    user_session = models.ForeignKey(UserSession, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)