from django.db import models
from authentication.models import *
# Create your models here.
class UserFeedback(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    feedback = models.CharField(max_length=200)
    rating = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.user.user.username} {self.rating}"