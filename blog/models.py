from django.db import models

# Create your models here.
# Create a Blog Models
class Blog(models.Model):
    image=models.ImageField(upload_to='images/')
    body=models.TextField()
    title=models.CharField(max_length=10000)
    date = models.DateTimeField()

    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:100]
    def pub_date(self):
        return self.date.strftime('%b %e %Y')