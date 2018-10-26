from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=200, default='Vegetables')
    created_at = models.DateTimeField(default=datetime.now, blank=True)


    def __str__(self):
        return self.title + ' - ' + self.content
