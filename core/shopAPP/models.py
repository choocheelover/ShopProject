from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
   name = models.CharField(max_length=200)
   price = models.IntegerField()
   description = models.TextField()

def __str__(self):
   return self.name

class Comment(models.Model):
   product = models.ForeignKey(Product, on_delete=models.CASCADE)
   author = models.ForeignKey(User, on_delete=models.CASCADE)
   text = models.TextField()
   created_at = models.DateTimeField(auto_now_add=True)
   likes = models.ManyToManyField(User, related_name='liked_comments', blank=True)

def __str__(self):
   return f'{self.author} — {self.product}'