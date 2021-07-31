from django.db import models

# Create your models here.
class Songs(models.Model):
	album=models.ImageField(upload_to='albums/')
	song=models.FileField(upload_to='albums/')
	#songname=models.CharField(max_length=50)
	#def __str__(self):
	#	return str(self.id)+','+self.songname
	class Meta:
		db_table="Songs"

class Users(models.Model):
	 name=models.CharField(max_length=50)
	 email=models.EmailField(max_length=100)
	 phoneno=models.IntegerField()
	 gender=models.CharField(max_length=10)
	 dob=models.DateField()
	 nickname=models.CharField(max_length=30)
	 psw=models.CharField(max_length=30)

	 class Meta:
	 	db_table="Users"
 





