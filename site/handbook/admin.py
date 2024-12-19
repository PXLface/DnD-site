from django.contrib import admin

from .models import Question, Choice

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QiestonAdmin(admin.ModelAdmin):
    fieldsets = [
        ("fefefefefefe", {"fields": ["question_text"]}),
        ("ththth", {"fields": ["pub_date"]})
                     
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]

class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = [
        ("fefefefefefe", {"fields": ["question", "choice_text"]}),
        ("ththth", {"fields": ["votes"]})
        
    ]
    
    
    

admin.site.register(Question, QiestonAdmin)
admin.site.register(Choice)