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


class MovieCategoryStateAdmin(admin.StackedInline):
    model = MovieCategoryState


@admin.register(Movie)
class MovieAdmin(CustomModelAdmin):
    inlines = (MovieCategoryStateAdmin,)


@admin.register(SessionQuestion)
class SessionQuestionAdmin(CustomModelAdmin):
    pass


@admin.register(UserSession)
class UserSessionAdmin(CustomModelAdmin):
    list_display = ("user", "message_id", "created_at", "updated_at")


@admin.register(User)
class UserAdmin(CustomModelAdmin):
    pass