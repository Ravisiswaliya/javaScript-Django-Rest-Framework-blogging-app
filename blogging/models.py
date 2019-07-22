from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=2000)
    image = models.ImageField(upload_to = "images/", default='images/office.jpg')
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    discription = models.CharField(max_length=3000)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title
