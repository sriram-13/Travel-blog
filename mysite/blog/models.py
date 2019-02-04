from django.db import models

# Create your models here.


class Keyword(models.Model):
    keyword = models.CharField(max_length=20)

    def __str__(self):
        return self.keyword

class Blogpost(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    img = models.ImageField(upload_to='blog/static/')
    content = models.TextField()
    keywords = models.ManyToManyField(Keyword, related_name='blogposts')

    def __str__(self):
        return self.title