from django.db import models


class User(models.Model):
    """ User Form """

    name = models.CharField('Name', max_length=50)
    email = models.EmailField('Email', max_length=120)
    phone = models.CharField(unique=True, max_length=15)

    def __str__(self):
        return self.name