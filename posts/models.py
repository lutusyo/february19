from django.db import models

# Create your models here.

class Post(models.Model):
    text   = models.TextField()
    amount = models.CharField(max_length=56, blank=True, null=True)


    def __str__(self):
        return self.text[:50]

