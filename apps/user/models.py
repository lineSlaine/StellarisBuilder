from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    image = models.ImageField(upload_to='images/user/avatar/', blank=True, null=True)


class SaveListStellaris(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    save = models.AutoField(primary_key=True)
