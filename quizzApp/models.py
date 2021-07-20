from django.db import models

# Create your models here.

class Quiz(models.Model):

    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quizies"

    quiz_title = models.CharField(max_length=128)
    quiz_starttime = models.DateTimeField()
    quiz_endtime = models.DateTimeField()

    def __str__(self):
        return str(self.id)

class Question(models.Model):
    question_text = models.CharField(max_length=300)
    quiz = models.ForeignKey(Quiz, related_name = 'Quiz_Set', on_delete = models.CASCADE)
    question_image = models.ImageField(null = True, blank = True, upload_to = "images/")
    isMCQ = models.BooleanField(blank=True, default=True)
    question_number = models.IntegerField(blank=True)

    def __str__(self):
        return str(self.id)


class MCQ(models.Model):
    option_text = models.CharField(max_length=300)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question,related_name="Question_Set",on_delete=models.CASCADE)
