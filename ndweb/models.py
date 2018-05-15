from django.db import models


class User(models.Model):
    user_id = models.CharField(max_length=200)
    user_password = models.CharField(max_length=200)
    user_email = models.CharField(max_length=200)


class File(models.Model):
    file_id = models.CharField(max_length=200)
    user_id = models.CharField(max_length=200)
    file_name = models.CharField(max_length=200)
    file_path = models.CharField(max_length=200)
    file_type = models.IntegerField();