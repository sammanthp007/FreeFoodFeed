from django.conf.urls import url

from django.contrib.auth.views import login

from . import views

urlpatterns = [
	url(r'^$', views.index_view, name='index'),
	url(r'^dashboard$', views.dashboard_view, name='dashboard'),
	#these are from the authentication views, actually i need to make it so but these actually are not
	url(r'^login/$', 'django.contrib.auth.views.login', name='login', kwargs={'template_name' : 'foodfeed/login.html'}),
	url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout', kwargs={'next_page' : '/'}),
	#url(r'^password_change/$', 'django.contrib.auth.views.password_change', name='password_change', kwargs={'template_name' : 'foodfeed/password_change.html', 'post_change_redirect': 'foodfeed:password_change_done'})
	#url(r'^password_change_done/$', 'django.contrib.auth.views.password_change_done', name='password_change_done', kwargs={'template_name' : 'foodfeed:dashboard'})
	#url()
	url(r'^addevent/$', views.add_event_view, name='addevent'),
	url(r'^signup/$', views.signup_view, name='signup'),
]