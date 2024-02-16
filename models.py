from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_patient = models.BooleanField('Is patient', default=False)
    is_doctor = models.BooleanField('Is doctor', default=False)

class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='category/')
    add_date = models.DateTimeField(auto_now=True, null=True)


class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='post/')
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    summary = models.CharField(max_length=300)
    content = models.TextField()


def __str__(self):
    return self.title
