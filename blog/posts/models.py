from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=200, default='Tutorials')
    fileUpload = models.FileField(upload_to='uploaded_image/', default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE,default='')
    created_at = models.DateTimeField(default=datetime.now, blank=True)


    def __str__(self):
        return self.title + ' - ' + self.content

    class Meta:
        verbose_name_plural = "Posts"
