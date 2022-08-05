from operator import truediv
from django.db import models

# Create your models here.
class Article(models.Model):
      title = models.CharField(max_length=100)
      image = models.ImageField()
      disc = models.TextField()
      create_at = models.DateTimeField(auto_now_add=True)
      update_at = models.DateTimeField(auto_now_add=True)


      def __str__(self):
            return self.title