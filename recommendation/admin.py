from django.contrib import admin

# Register your models here.
from .models import Movie, QuestionAnswer, Category, User, UserSession, Question, CategoryState, MovieCategoryState, SessionQuestion


class CategoryStatesAdmin(admin.TabularInline):
    model = CategoryState

class CategoryAdmin(admin.ModelAdmin):
    inlines = (CategoryStatesAdmin,)

class QuestionAnswerAdmin(admin.TabularInline):
    model = QuestionAnswer

class QuestionAdmin(admin.ModelAdmin):
    inlines = (QuestionAnswerAdmin, )


class MovieCategoryStateAdmin(admin.TabularInline):
    model = MovieCategoryState

class MovieAdmin(admin.ModelAdmin):
    inlines = (MovieCategoryStateAdmin, )
    list_display = ('title', 'description', 'image_url')

@admin.register(SessionQuestion)
class SessionQuestionAdmin(admin.ModelAdmin):
    pass


class ViewOnlyAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(CategoryState)
class CategoryStatesViewOnly(admin.ModelAdmin):
    pass


class UserSessionAdmin(admin.ModelAdmin):
    list_display = ('user', 'message_id', 'created_at', 'updated_at')


admin.site.register(Movie, MovieAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(User)
admin.site.register(Question, QuestionAdmin)

# register view only for convenience

admin.site.register(UserSession, UserSessionAdmin)
