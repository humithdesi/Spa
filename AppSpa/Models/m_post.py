from django.db import models
import uuid
class Tag(models.Model):
    name=models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.name
class Post(models.Model):
    title=models.CharField(max_length=200,blank=False)
    description=models.TextField()
    content=models.TextField()
    tag=models.ManyToManyField(Tag)
    image=models.ImageField(upload_to='media',default=None,blank=True)
    slug=models.SlugField(unique=True)
    def __str__(self):
        return self.title