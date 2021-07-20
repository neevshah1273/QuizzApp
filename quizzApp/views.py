from django.shortcuts import render
from django.http import HttpResponse
from .models import Quiz
from rest_framework import generics
from .serializers import QuizSerializer


# Create your views here.

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

class Quiz(generics.ListAPIView):

    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()