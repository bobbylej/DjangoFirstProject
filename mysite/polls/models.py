from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime
import sys
#import imp
#imp.reload(sys)
reload(sys)
sys.setdefaultencoding('utf8')


'''
# Create your models here.
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.question_text
	def was_published_recently(self):
		return self.pub_date >= timezone.now()-datetime.timedelta(days=1)
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolead = True
	was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text
'''

class Function(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    desc = models.CharField(max_length=255, default=None, blank=True, null=True)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Man'),
        ('W', 'Women'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=None, blank=True, null=True)
    phone = models.PositiveIntegerField(validators=[MinValueValidator(0)], default=None, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    zip_code = models.CharField(max_length=6, default=None, blank=True, null=True)
    street = models.CharField(max_length=30, default=None, blank=True, null=True)
    no_building = models.CharField(max_length=6, default=None, blank=True, null=True)
    no_local = models.CharField(max_length=6, default=None, blank=True, null=True)
    employee_func = models.ForeignKey(Function, default=None, blank=True, null=True)
    photo = models.CharField(max_length=200, default=None, blank=True, null=True)
'''
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
	client = models.ForeignKey(CustomUser)
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

class Gym(models.Model):
	phone = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    	city = models.CharField(max_length=30)
    	zip_code = models.CharField(max_length=6)
    	street = models.CharField(max_length=30)
    	no_building = models.CharField(max_length=6)
    	no_local = models.CharField(max_length=6, default=None, blank=True, null=True)
	open_time = models.TimeField(default=None, blank=True, null=True)
	close_time = models.TimeField(default=None, blank=True, null=True)

	def __str__(self):
        	parts = (self.city, ' ', self.street, ' ', self.no_building, '/', self.no_local)
        	return "".join(str(s) for s in parts if s is not None) 

class GymActivity(models.Model):
	activity = models.ForeignKey(Activity)
	gym = models.ForeignKey(Gym)
	instructor = models.ForeignKey(CustomUser, limit_choices_to={'groups__name': "employees", 'employee_func__name': "Instruktor"}, related_name="employee_gym_activity")
	start = models.DateTimeField()
	end = models.DateTimeField()
	max_people = models.PositiveIntegerField(validators=[MinValueValidator(0)], default=None, blank=True, null=True)
	clients = models.ManyToManyField(CustomUser, limit_choices_to={'groups__name': "clients"}, related_name="client_gym_activity", default=None, blank=True, null=True)

    	def __str__(self):
        	parts = (self.activity, ' - ', self.gym)
        	return "".join(str(s) for s in parts if s is not None) 
'''
