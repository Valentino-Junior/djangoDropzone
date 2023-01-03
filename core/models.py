from django.db import models

# Create your models here.

class Image(models.Model):
    image=models.ImageField(upload_to='images/')
    # date = models.DateTimeField( auto_now_add=True)

    class Meta:
        ordering=['-date']

    def __str__(self):
        return str(self.date)