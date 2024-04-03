from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=12)
    gender = models.CharField(max_length=20, choices=[('male', 'Male'), ('female', 'Female',)])
    photo = models.FileField(upload_to='user_pic/', null=True, blank=True, help_text="file formats['jpg', 'jpeg', 'png', 'gif'] and file size should be less then 10mb")
    datetime = models.DateField(auto_now_add=True)

# Create your models here.
