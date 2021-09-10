from django.db import models


class Course(models.Model):
    about = models.CharField(max_length=1024)
    duration = models.IntegerField()
    name = models.CharField(max_length=64)
    url_image = models.CharField(max_length=128)

    is_active = models.BooleanField()
