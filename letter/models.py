from django.db import models

# Create your models here.

class Letters(models.Model) :
    title = models.CharField(max_length=200)
    content = models.TextField(blank=False)

    def __str__(self):
        return self.title