from django.db import models

# Create your models here.

class Image(models.Model):
    imageType = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return  str(self.imageType)

class ImageFile(models.Model):
    pic = models.ForeignKey(Image, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/')
    date = models.DateTimeField( auto_now_add=True)

    class Meta:
        ordering=['-date']

    def __str__(self):
        return  str(self.date)