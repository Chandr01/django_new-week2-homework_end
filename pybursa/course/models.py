from django.db import models


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    description = models.TextField(max_length=2000)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    subject = models.CharField(max_length=255)
    description = models.TextField(max_length=2000)
    course = models.ForeignKey(Course, null=True)
    order = models.PositiveIntegerField(null=True, unique=True)

    def __str__(self):
        return self.subject


class Students(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    skype = models.CharField(max_length=255, null=True)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name
