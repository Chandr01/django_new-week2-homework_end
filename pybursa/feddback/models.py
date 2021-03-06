from django.db import models
from django.utils import timezone


# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=2000)
    from_email = models.EmailField(null=True)
    create_date = models.DateTimeField(default=timezone.now(), null=True)

    def __str__(self):
        return str('{} - email:{}'.format(self.name, self.from_email))
