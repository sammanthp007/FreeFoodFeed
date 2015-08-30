from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from django.contrib.auth.models import User
from .models import PersonType, EventType

# Create your views here.

def index_view(request):
	cache = EventType.objects.all()
	if (request.user and request.user.is_authenticated()):
		return redirect('foodfeed:dashboard')
	return render(request, 'foodfeed/index.html', {'title': 'foodfeed:login', 'username' : request.user, 'events':cache})

def signup_view(request, username='', error='', email=''):
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		verify_password = request.POST['verify_password']
		email = request.POST['email']
		try:
			wrong = []
			err = ""
			if UsernameValidated(username, wrong) and PasswordValidated(password, verify_password, wrong) and EmailValidated(email, wrong):
				user = User.objects.create_user(username=username, email=email, password=password)
				user.save()
				person = PersonType(user=user)
				person.save()
				user.backend = "django.contrib.auth.backends.ModelBackend"
				login(request, user)
				return redirect('foodfeed:dashboard')
			else:
				for wrongs in wrong:
					err += wrongs
				error="%(wrong)s is not correct" % {"wrong" : err}
		except ValueError:
				error="The user " + username + " already exists."
	return render(request, 'foodfeed/signup.html', {'title' : 'HU-Nutn : Sign Up', 'username' : username, 'error' : error, 'email' : email})



@login_required
def dashboard_view(request):
	title = "foodfeed:dashboard"
	cache = EventType.objects.all()
	return render(request, 'foodfeed/dashboard.html', {'title':title, 'username': request.user, 'event' : cache})

@login_required
def add_event_view(request):
	if request.user.username == "admin":
		title = "foodfeed:addevent"
		if request.GET:
			name = request.GET['name']
			organizers1 = request.GET['organizers1']
			organizers2 = request.GET['organizers2']
			st1 = request.GET['st1']
			st2 = request.GET['st2']
			zipcode = request.GET['zipcode']
			if zipcode:
				zipcode = int(zipcode)
			else:
				zipcode = 0
			city = request.GET['city']
			state = request.GET['state']
			description = request.GET['description']
			date = request.GET['date']
			event_time = request.GET['event-time']
			finished = request.GET['finished']
			if finished.lower() == 'y':
				finished = True
			else:
				finished = False
			#need exception handlening here to make the data that I put to be in correct syntax
			event = EventType(name=name, organizer1=organizers1, organizer2=organizers2, venue_st1=st1, venue_st2=st2,zip_code=zipcode,venue_city=city, venue_state=state, description=description, date1=date, time1=event_time, finished=finished)
			event.save()
		return render(request, 'foodfeed/addevent.html', {'title':title})
	else:
		return redirect('foodfeed:dashboard')

import re

def PasswordValidated(password, verify_password, wrong):
	if (password == verify_password) and (re.match(r'[A-Za-z0-9!@#$%^&+_=-]{5,20}', password)):
		return True
	wrong.append("password")
	return False

def UsernameValidated(username, wrong):
	if re.match(r'^[A-Za-z0-9_.-]{3,30}$', username):
		return True
	wrong.append("username")
	return False

def EmailValidated(email, wrong):
	if re.match(r'^[A-Za-z0-9]+@[A-Za-z0-9.]+$', email):
		if ("howard.edu" in email.lower()):
			return True
	wrong.append("email")
	return False