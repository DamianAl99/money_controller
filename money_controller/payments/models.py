from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Groups_Pay(models.Model):
  Title_groups = models.CharField(max_length=200)
  description = models.TextField(max_length=1000)
  created = models.DateTimeField(auto_now_add=True)
  budget = models.FloatField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.Title_groups + ' - ' + self.user.username

class Add_Text_Admin(models.Model):
  text = models.CharField(max_length=200)