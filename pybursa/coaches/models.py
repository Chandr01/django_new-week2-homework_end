from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class User2(models.Model):
    name = models.CharField(max_length=100, null=True)
    surname = models.CharField(max_length=100, null=True)
    #
    # def __str__(self):
    #     return self.surname

        # def __str__(self):
        #     return "{}".format(self.name)


class Coach(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True)
    GENDER = (('M', 'Male'), ('F', 'Female'))
    gender = models.CharField(max_length=2, choices=GENDER)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    skype = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    user2 = models.OneToOneField(User2, null=True)

    # first_name = models.ForeignObject(User.first_name)

    # class Meta:
    #     mdoel = User
    #
    #     def __str__(self):
    #         return "{}".format(self.first_name)

    # def __str__(self):
    #
    #     return '{}'.format(self.user2)
