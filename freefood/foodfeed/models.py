from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class PersonType(models.Model):
	def __str__(self):
		return self.user.username

	user = models.OneToOneField(settings.AUTH_USER_MODEL)	#user have firstname lastname email password and username 
	signed_up = models.DateTimeField(auto_now_add=True)
	profile_update = models.DateTimeField(auto_now=True)

class EventType(models.Model):
	def __str__(self):
		return self.name

	name = models.TextField(default='NA')
	organizer1 = models.TextField(default='NA')
	organizer2 = models.TextField(default='NA')
	organizer3 = models.TextField(default='NA')
	organizer4 = models.TextField(default='NA')
	organizer5 = models.TextField(default='NA')
	organizer6 = models.TextField(default='NA')
	organizer7 = models.TextField(default='NA')
	organizer8 = models.TextField(default='NA')
	organizer9 = models.TextField(default='NA')
	organizer10 = models.TextField(default='NA')
	venue_st1 = models.TextField(default='NA')
	venue_st2 = models.TextField(default='NA')
	zip_code = models.IntegerField(default=0)
	venue_city = models.TextField(default='NA')
	venue_state = models.TextField(default='NA')
	venue_country = models.TextField(default='NA')
	description = models.TextField(default='NA')
	date1 = models.TextField(default='2015-09-01')
	time1 = models.TextField(default='00:00')
	date2 = models.TextField(default='2015-09-01')
	time2 = models.TextField(default='00:00')
	foodtype = models.TextField(default='light refreshment')
	finished = models.BooleanField(default=False)
