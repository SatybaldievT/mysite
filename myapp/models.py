from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)

class Question(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.IntegerField(default= 0)
    view = models.IntegerField(default= 0)
    tags = models.ManyToManyField('Tag')
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

class Answer(models.Model):
    rating = models.IntegerField(default= 0)
    text = models.TextField()
    correct = models.BooleanField()
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

class Tag(models.Model):
    name = models.CharField(max_length=100)