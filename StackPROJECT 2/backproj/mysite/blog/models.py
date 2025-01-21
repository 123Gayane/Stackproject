from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Question(models.Model):
    question = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='questions')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    likes = models.ManyToManyField(User, related_name='liked_questions', blank=True)

    def __str__(self):
        return self.question


class Comment(models.Model):
    comment = models.TextField(default="hello")
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    likes = models.ManyToManyField(User, related_name='liked_comments', blank=True)

    def __str__(self):
        return self.comment
