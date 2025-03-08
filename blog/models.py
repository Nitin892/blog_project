from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=3000)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title[:50]
    

#  post, author, text, and created_date.


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username