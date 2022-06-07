from django.db import models

# Create your models here.

"""All models saved with dbsqlite3
@Author: Adarsh Koppa Manjunath"""

class Feedback(models.Model):
    username=models.CharField(max_length=200)
    user_email=models.CharField(max_length=300)
    subject=models.CharField(max_length=400)
    feedback=models.TextField()
    
    def __str__(self):
        return self.username

class UserPortal(models.Model):
    
    username=models.CharField(primary_key=True,max_length=200)
    topic=models.CharField(max_length=200)
    urls=models.TextField()
    updatedate=models.CharField(max_length=300)
    sentiment=models.CharField(max_length=200)

    def __str__(self):
        return   self.username



