from django.db import models

# Create your models here.

class user1(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=50)
    class Meta:
        db_table="user1"