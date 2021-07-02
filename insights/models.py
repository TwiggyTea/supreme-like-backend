from django.db.models.deletion import CASCADE
from supreme_like_django.settings import AUTH_USER_MODEL
from django.db import models
from django.conf import settings
    
    
class Insight(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    choiceOne = models.CharField(max_length=100, default="one")
    choiceOneTime = models.IntegerField(default=0)
    choiceTwo = models.CharField(max_length=100, default="two")
    choiceTwoTime = models.IntegerField(default=0)
    choiceThree = models.CharField(max_length=100, default="three")
    choiceThreeTime = models.IntegerField(default=0)
    choiceFour = models.CharField(max_length=100, default="four")
    choiceFourTime = models.IntegerField(default=0)
    choiceFive = models.CharField(max_length=100, default="five")
    choiceFiveTime = models.IntegerField(default=0)