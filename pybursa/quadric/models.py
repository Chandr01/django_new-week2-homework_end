from django.db import models


# Create your models here.
class Quadric_logik(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True)
    packag = models.CharField(max_length=10)
    name_subscribe = models.BooleanField()
    comment = models.TextField(max_length=1000)
    is_active = models.BooleanField(default=True)
    date_apply = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
