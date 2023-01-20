from django.db import models
from.import views
from django.contrib.auth.models import User

# Create your models here.
class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    content = models.TextField()
    timestamp =models.DateTimeField(auto_now_add=True)