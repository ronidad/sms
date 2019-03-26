from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs = {'pk':self.pk})


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    names = models.CharField(max_length=50,default="user")
    sender_Id = models.CharField(max_length=11,default='ROBERMS')
    access_code = models.CharField(max_length=11,default='710083')
    service_id = models.CharField(max_length=50, default="6015752000133434")
    business_name = models.CharField(max_length=100, default="Buiness Name")




    def __str__(self):
        return f'{self.user.username} profile'

    def save(*args, **kwargs):
        super(*args, **kwargs).save(*args, **kwargs)


class Outgoing(models.Model):
    user = models.CharField(max_length=50)
    service_id  = models.CharField(max_length=50)
    access_code  = models.CharField(max_length=50)
    phone_numbers = models.TextField()
    text_message = models.TextField(max_length=600)

    def __str__(self):
        return f'{self.Outgoing.text_message}'

    def get_absolute_url(self):
        return reverse('profile')

class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    user = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Ingredience Categories"

    def __unicode__(self):
        return self.name



class Look(models.Model):
    title= models.CharField(max_length=200, unique=True)
    content= models.TextField()

class Upload(models.Model):
    author = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    csv = models.FileField(upload_to='csv/', null = True, blank=True)

    def __str__(self):
        return self.csv
