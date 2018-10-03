from django.db import models

# Create your models here.
# Create a Blog Models
class Blog(models.Model):
    image=models.ImageField(upload_to='images/')
    body=models.TextField()
    title=models.CharField(max_length=10000)
    date = models.DateTimeField()
