from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
	#views.index refers to the def named 'index' in views.py
	url(r'^$', views.index, name='index'),
	url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
	url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
	url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
	url(r'^test/$', views.testhome, name='test-home'),
	url(r'^test/(?P<arg>\w+)/$', views.test, name='testing'),

)

