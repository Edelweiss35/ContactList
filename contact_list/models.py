from django.db import models
from django.urls import reverse


class Book(models.Model):
    name = models.TextField(max_length=200)
    e_mail = models.TextField(max_length=200)
    phone_number = models.TextField(max_length=200)

    def __str__(self):
        return self.name
