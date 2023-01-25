from django.db import models


class Picture(models.Model):
    """
    Model for `Picture` objects.
    """
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.title
