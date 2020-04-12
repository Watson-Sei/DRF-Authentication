from django.db import models


class Message(models.Model):
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.message
