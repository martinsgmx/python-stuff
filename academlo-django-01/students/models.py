from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    born_date = models.DateField()
    nationality = models.CharField(max_length=64, null=True, default=None)
    profile_pic = models.CharField(max_length=256, null=True, default="https://cdn4.iconfinder.com/data/icons/professions-1-2/151/8-512.png")
    email = models.CharField(max_length=128, null=True, default=None)

    is_active = models.BooleanField()
