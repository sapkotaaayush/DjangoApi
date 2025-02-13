from django.db import models

# Create your models here.
class Blogpost(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
