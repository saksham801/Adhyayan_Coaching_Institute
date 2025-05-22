from django.db import models

# Create your models here.
class founders(models.Model):
    name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    email = models.EmailField()
    college = models.CharField(max_length=100)
    image_url = models.URLField()


    def __str__(self):
        return self.name

class teams(models.Model):
    name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    email = models.EmailField()
    college = models.CharField(max_length=100)
    image_url = models.URLField()

    def __str__(self):
        return self.name


