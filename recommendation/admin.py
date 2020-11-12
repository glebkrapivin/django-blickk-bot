from django.contrib import admin

# Register your models here.
from .models import (
    Movie,
    QuestionAnswer,
    Category,
    User,
    UserSession,
    Question,
    CategoryState,
    MovieCategoryState,
    SessionQuestion,
    Recommendation,
Message
)


class CustomModelAdmin(admin.ModelAdmin):
    " to show all fields in admin panel"

    def __init__(self, model, admin_site):
        self.list_display = [
            field.name for field in model._meta.fields if field.name != "id"
        ]
        super(CustomModelAdmin, self).__init__(model, admin_site)


class ViewOnlyAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class CategoryStatesAdmin(admin.TabularInline):
    model = CategoryState


@admin.register(Category)
class CategoryAdmin(CustomModelAdmin):
    inlines = (CategoryStatesAdmin,)


class QuestionAnswerAdmin(admin.TabularInline):
    model = QuestionAnswer


@admin.register(Question)
class QuestionAdmin(CustomModelAdmin):
    inlines = (QuestionAnswerAdmin,)


class MovieCategoryStateAdmin(admin.TabularInline):
    model = MovieCategoryState


@admin.register(Movie)
class MovieAdmin(CustomModelAdmin):
    inlines = (MovieCategoryStateAdmin,)


@admin.register(SessionQuestion)
class SessionQuestionAdmin(CustomModelAdmin):
    pass


class MessageAdmin(admin.TabularInline):
    model = Message

@admin.register(UserSession)
class UserSessionAdmin(CustomModelAdmin):
    inlines = (MessageAdmin, )



@admin.register(User)
class UserAdmin(CustomModelAdmin):
    pass
