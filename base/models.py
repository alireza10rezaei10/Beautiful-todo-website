from django.db import models
from django.contrib.auth.models import User
# Create your models here.

def getcurrentusername(instance, filename):
    return f"images/avatars/{instance.user.username}/avatar/{filename}"

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, blank=True, upload_to=getcurrentusername)    

    def __str__(self):
        return str(self.user)


class deadlines(models.Model):
    title = models.CharField(max_length=200)
    hour = models.IntegerField()
    day = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
