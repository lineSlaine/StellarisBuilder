from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    image = models.ImageField(upload_to='images/user/avatar/', blank=True, null=True)


class SaveListStellaris(models.Model):
    save_id = models.AutoField(primary_key=True,)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, default='My Empire')
