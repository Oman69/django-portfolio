from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    subtitle = models.CharField
    img = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Certificates(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    subtitle = models.CharField
    img = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title