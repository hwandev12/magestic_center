from calendar import c
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.user.username)
class Candidate(models.Model):
    
    class Meta:
        verbose_name = 'Candidate'
        verbose_name_plural = 'Candidates Admittes'
        
    name = models.CharField(max_length=30)
    lastName = models.CharField(max_length=40)
    age = models.IntegerField(default=0)
    email = models.EmailField()
    job = models.CharField(max_length=20)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.user)


def create_post_save(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)    

post_save.connect(create_post_save, sender=User)