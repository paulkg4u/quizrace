from django.conf.urls import patterns, include, url
from django.contrib.auth import admin
from django.conf import settings
urlpatterns = ('',

	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', include('quizrace.urls')),
	url(r'^quizathon/', include('quizrace.urls')),
	url(r'^accounts/', include('registration.backends.simple.urls')),
	
	)