from django.db import models
from django.utils import timezone

# Create your models here.

class Image(models.Model):
    image=models.ImageField(upload_to='images/')
    date = models.DateTimeField(default=timezone.now())

    class Meta:
        ordering=['-date']

    def __str__(self):
        return str(self.image)