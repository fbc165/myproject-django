from django.contrib import admin
from crud.models import Question
#Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator', 'image' )  # Exibe 'title' e 'creator' na lista de exibição

admin.site.register(Question, QuestionAdmin)

