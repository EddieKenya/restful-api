from django.db import models

# Create your models here.
from django.contrib.auth.models import User

# Create your models here.
class Profile (models.Model):
    GENDER_CHOICE =(
        ('male','Male'),
        ('female', 'Female'),
        ('others', 'Others')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    second_name = models.CharField(max_length= 50, null=True, blank=True)
    created = models.DateTimeField( auto_now=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE, null=True)
    profileimg = models.ImageField(upload_to='profileimg',default='blank-prof.jpg')
    location = models.CharField(max_length=100, blank=True)
    about = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.user.username



class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length= 300)
    content= models.TextField()
    image = models.FileField(upload_to= 'image.jpg', blank=True, null=True)
    date_published = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title