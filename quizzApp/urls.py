from django.urls import path

from .views import Quiz

urlpatterns = [
    path('', Quiz.as_view(), name='quiz'),
    #path('past',views.PastQuizzes,name='PastQuizzes'),
    #path('live', views.ActiveQuizzes, name='ActiveQuizzes'),
    #path('next', views.FutureQuizzes, name='FutureQuizzes')
]