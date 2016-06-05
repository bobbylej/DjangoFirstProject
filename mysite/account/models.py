from django.db import models
from django.conf import settings  
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#from polls.models import CustomUser

class Addition(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
        	return self.name

class Voucher(models.Model):
	name = models.CharField(max_length=30, primary_key=True)
	desc = models.CharField(max_length=255, default=None, blank=True, null=True)
	price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	days = models.PositiveIntegerField(validators=[MinValueValidator(0)], default=30)
	additions = models.ManyToManyField(Addition, default=None, blank=True, null=True)

    	def __str__(self):
        	return self.name

class ClientsVoucher(models.Model):
	client = models.ForeignKey(settings.AUTH_USER_MODEL)
	voucher = models.ForeignKey(Voucher)
	date_order = models.DateField()
	date_end = models.DateField()

	def __str__(self):
		parts = (self.client.username, ' - ', self.voucher.name)
        	return "".join(str(s) for s in parts if s is not None)

class Activity(models.Model):
	name = models.CharField(max_length=30, primary_key=True)
	desc = models.CharField(max_length=255, default=None, blank=True, null=True)

	def __str__(self):
        	return self.name 

class Photo(models.Model):
	link = models.CharField(max_length=200, primary_key=True)

	def __str__(self):
        	return self.link

class Muscle(models.Model):
	name = models.CharField(max_length=50, primary_key=True)

	def __str__(self):
        	return self.name

class Equipment(models.Model):
	name = models.CharField(max_length=30, primary_key=True)
	desc = models.CharField(max_length=255, default=None, blank=True, null=True)
	muscles = models.ManyToManyField(Muscle, default=None, blank=True, null=True)
	photos = models.ManyToManyField(Photo, default=None, blank=True, null=True)

	def __str__(self):
        	return self.name

class Gym(models.Model):
	phone = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    	city = models.CharField(max_length=30)
    	zip_code = models.CharField(max_length=6)
    	street = models.CharField(max_length=30)
    	no_building = models.CharField(max_length=6)
    	no_local = models.CharField(max_length=6, default=None, blank=True, null=True)
	open_time = models.TimeField(default=None, blank=True, null=True)
	close_time = models.TimeField(default=None, blank=True, null=True)
	equipments = models.ManyToManyField(Equipment, default=None, blank=True, null=True)
	photos = models.ManyToManyField(Photo, default=None, blank=True, null=True)

	def __str__(self):
        	parts = (self.city, ' ', self.street, ' ', self.no_building, '/', self.no_local)
        	return "".join(str(s) for s in parts if s is not None) 

class GymActivity(models.Model):
	activity = models.ForeignKey(Activity)
	gym = models.ForeignKey(Gym)
	instructor = models.ForeignKey(settings.AUTH_USER_MODEL, limit_choices_to={'groups__name': "employees", 'employee_func__name': "Instruktor"}, related_name="employee_gym_activity")
	start = models.DateTimeField()
	end = models.DateTimeField()
	max_people = models.PositiveIntegerField(validators=[MinValueValidator(0)], default=None, blank=True, null=True)
	clients = models.ManyToManyField(settings.AUTH_USER_MODEL, limit_choices_to={'groups__name': "clients"}, related_name="client_gym_activity", default=None, blank=True, null=True)

    	def __str__(self):
        	parts = (self.activity, ' - ', self.gym)
        	return "".join(str(s) for s in parts if s is not None)

