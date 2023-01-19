from django.db import models
from payments.models import Groups_Pay

# Create your models here.

class Payout(models.Model):
  pay_title = models.CharField(max_length=200)
  created = models.DateTimeField(auto_now_add=True)
  price = models.FloatField()
  status = models.BooleanField(default=False)
  group = models.ForeignKey(Groups_Pay, on_delete=models.CASCADE)

  def __str__(self):
    return self.group.user.get_username()

