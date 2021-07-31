from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_comma_separated_integer_list

# Create your models here.

class User(AbstractUser):
	age=models.IntegerField(default=20)
	mobilenumber=models.CharField(max_length=10,null=True)
	uimg=models.ImageField(upload_to='Profilepics/',default='dummyProfile.png')
	t=[(1,'Guest'),(2,'Manager'),(3,'User')]
	role=models.IntegerField(choices=t,default=1)
	fav=models.CharField(validators=[validate_comma_separated_integer_list],max_length=200, blank=True, null=True,default='')
	rec=models.CharField(validators=[validate_comma_separated_integer_list],max_length=200, blank=True, null=True,default='')
	#likes=models.CharField(validators=[validate_comma_separated_integer_list],max_length=200, blank=True, null=True,default='')
