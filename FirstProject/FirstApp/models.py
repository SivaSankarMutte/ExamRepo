from django.db import models

# Create your models here.

class Register(models.Model): #models.Model converts this class to db table or collection
	name=models.CharField(max_length=50)
	email=models.EmailField(max_length=50)

	def __str__(self):
		return str(self.id)+" "+self.name

class SignUp(models.Model):
	fname=models.CharField(max_length=50)
	age=models.IntegerField()

	class Meta:
		db_table='signup'

class Tour(models.Model):
	cityname=models.CharField(max_length=50)
	photo=models.FileField()
	description=models.TextField()
	price=models.BigIntegerField()

	class Meta:
		db_table="Tour"

	def __str__(self):
		return str(self.id)+','+self.cityname

class ModelFields(models.Model):
	Name=models.CharField(max_length=50)
	phoneno=models.BigIntegerField()
	email=models.EmailField(max_length=50)
	#binNum=models.BinaryField()
	HaveLaptop=models.BooleanField(default=False)
	dob=models.DateField()
	cur_time=models.DateTimeField(auto_now=True)
	Petrol_rate=models.DecimalField(max_digits=5,decimal_places=3)
	Duration=models.DurationField()
	SSCCertificate=models.FileField()
	#sscGrade=models.FloatField()
	photo=models.ImageField()
	FavNum=models.IntegerField()
	HaveAnyLoan=models.NullBooleanField()
	Enter_Positive_Number=models.PositiveIntegerField()
	Enter_Small_Positive=models.SmallIntegerField()
	Address=models.TextField()
	Time=models.TimeField(auto_now=True)

	class Meta:
		db_table="ModelFields"

	def __str__(self):
		return str(self.id)+' '+self.Name


