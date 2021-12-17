from django.db import models
import datetime

# Create your models here.
class Task(models.Model):
    img=models.ImageField(upload_to="images")
    name=models.CharField(max_length=100)
    rate=models.IntegerField()
    datetime=models.DateTimeField(default=datetime.datetime.today)
    def __str__(self):
        return self.name