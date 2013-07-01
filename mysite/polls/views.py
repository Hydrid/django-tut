# Create your views here.

from django.http import HttpResponse
from polls.models import Poll
from django.shortcuts import render

def index(request):
	latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
	#output = ', '.join([p.question for p in latest_poll_list])
	context = {'latest_poll_list': latest_poll_list}
	return render(request, 'polls/index.html', context)

def detail(request, poll_id):
	p = Poll.objects.get(id=poll_id)
	context = {'poll' : p}
	return render(request, 'polls/details.html', context)

def results(request, poll_id):
	return HttpResponse("You're looking at the results of poll %s" % poll_id)

def vote(request, poll_id):
	return HttpResponse("You're voting on poll %s" % poll_id)

def test(request, arg):
	return HttpResponse("This is a test page for " + arg)

def testhome(request):
	return HttpResponse("Enter a url to test for")

