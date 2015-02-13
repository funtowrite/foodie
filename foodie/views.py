from django.shortcuts import render
from django.template import RequestContext, loader
from foodie.models import Vendor, Event
# Create your views here.
from django.http import HttpResponse
from django.utils import timezone
import datetime

#home page
def index(request):
    template = loader.get_template('foodie/index.html')
    context = RequestContext(request, {
    })
    return HttpResponse(template.render(context))

#list of all vendors
def vendors(request):
	vendorsList = Vendor.objects.order_by('-eventCount')
	template=loader.get_template('foodie/vendors.html')
	context = RequestContext(request, {
		'vendorsList': vendorsList
	})
	return HttpResponse(template.render(context))

#list of all events
def events(request):
	today = timezone.now().date()
	eventsList = Event.objects.filter(endTime__gte=today).order_by('startTime')
	template = loader.get_template('foodie/events.html')
	context = RequestContext(request, {
		'eventsList': eventsList
	})
	return HttpResponse(template.render(context))

#to view the details of a single event
def event(request, event_id):
	event = Event.objects.get(id=event_id)
	template = loader.get_template('foodie/event.html')
	context = RequestContext(request, {
		'event': event, 
		'vendors': event.vendors.order_by('name')
	})
	return HttpResponse(template.render(context))

#to view the details of a single vendor
def vendor(request, vendor_id):
	vendor = Vendor.objects.get(id=vendor_id)
	template = loader.get_template('foodie/vendor.html')
	context = RequestContext(request, {
		'vendor': vendor, 
		'events': vendor.event_set.order_by('-startTime')
	})
	return HttpResponse(template.render(context))

