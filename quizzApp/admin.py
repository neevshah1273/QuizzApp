from django.contrib import admin

# Register your models here.

from . import models


#@admin.register(models.Quiz)

class AnswerInlineModel(admin.TabularInline):
    model = models.MCQ
    fields = [
        'option_text',
        'is_correct'
    ]

class QuestionInlineModel(admin.TabularInline):
    model = models.Question
    fields = [
        'question_text',
        'quiz',
        'question_image',
        'isMCQ',
        'question_number'
    ]
    inlines = [
        AnswerInlineModel,
    ]

@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'question_text',
        'quiz',
        'question_image',
        'isMCQ',
        'question_number'
    ]
    list_display = [
        'question_text',
        'quiz',
        'question_image',
        'isMCQ',
        'question_number'
    ]
    inlines = [
        AnswerInlineModel,
    ]

@admin.register(models.MCQ)

class MCQAdmin(admin.ModelAdmin):
    list_display = [
        'option_text',
        'is_correct',
        'question'
    ]

@admin.register(models.Quiz)
class QuizAdmin(admin.ModelAdmin):
    fields = [
        'quiz_title',
        'quiz_starttime',
        'quiz_endtime'
    ]
    list_display = [
        'quiz_title',
        'quiz_starttime',
        'quiz_endtime'
    ]
    inlines = [
        QuestionInlineModel
    ]

#admin.site.register(models.Quiz)
# admin.site.register(Question)
# admin.site.register(MCQ)
