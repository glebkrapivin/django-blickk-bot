from django.db import models

# Create your models here.

class Category(models.Model):
    text = models.CharField(max_length=256)
    coef = models.FloatField()

    def __str__(self):
        return self.text

class CategoryState(models.Model):
    text = models.CharField(max_length=256)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Question(models.Model):
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class QuestionAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=256)
    value = models.ForeignKey(CategoryState, on_delete=models.CASCADE)


class User(models.Model):
    tg_id = models.IntegerField(unique=True)
    properties = models.TextField(blank=True)


class UserSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message_id = models.IntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)



class SessionQuestion(models.Model):
    user_session = models.ForeignKey(UserSession, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(QuestionAnswer, on_delete=models.CASCADE, blank=True, null=True)
    is_current= models.BooleanField(default=False)




class Movie(models.Model):
    title = models.TextField()
    description = models.TextField()
    image_url = models.URLField()
    def __str__(self):
        return self.title

class MovieCategoryState(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    state = models.ForeignKey(CategoryState, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Recommendation(models.Model):
    user_session = models.ForeignKey(UserSession, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


