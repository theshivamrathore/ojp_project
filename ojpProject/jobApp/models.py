from django.db import models

# Create your models here.

class Registration_model(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile_number = models.BigIntegerField()
    email_id = models.EmailField(max_length=50)
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)

class Govtjob_detail_model(models.Model):
    company = models.CharField(max_length=100)
    post_name = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    total_post = models.IntegerField()
    location = models.CharField(max_length=100)
    last_date = models.CharField(max_length=100)
