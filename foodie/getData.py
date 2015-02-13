from ginger.settings import FACEBOOK_APP_ID, FACEBOOK_APP_SECRET
import urllib
import contextlib
from bs4 import BeautifulSoup
from urllib2 import urlopen
from simplejson import loads
from foodie.models import Event, Vendor
import re

def getVendors():
	url = "http://offthegridsf.com/vendors#food"
	with contextlib.closing(urllib.urlopen(url)) as urlobj:
		data = urlobj.read()
		soup = BeautifulSoup(data)
		vendors = soup.findAll("a", {"class": "otg-vendor-name-link"})
		for v in vendors:
				vName = v.get_text()
				if len(Vendor.objects.filter(name=vName)) ==0:
					newVendor = Vendor(name=vName)
					newVendor.save()

def getEvents():
	url = "https://graph.facebook.com/OffTheGridSF/events?key=value&access_token="+FACEBOOK_APP_ID+"|"+FACEBOOK_APP_SECRET+"&fields=description,end_time,name,start_time,id,location&limit=500"
	content = loads(urlopen(url).read())
	numberOfEvents = len(content['data'])
	for i in xrange(numberOfEvents):
		#check for duplicate events first
		if len(Event.objects.filter(eventId=content['data'][i]['id']))==0:
			#first save the Event
	 		currEvent = content['data'][i]
	 		evtName = currEvent['name'].replace('Off the Grid: ', '')
	 		newEvent = Event(eventId=currEvent['id'] , name=evtName, startTime=currEvent['start_time'], endTime=currEvent['end_time'], location=currEvent['location'])
	 		newEvent.save()
			description = replace(currEvent['description'])
			
			maxNameLen = 100 #this number was determined by testing the vendor name database, the max found was 68
			parseDescription = description.split('\n')
			for line in parseDescription: 
				if len(line) < 100 and len(line)>0:
					vendorMatch= Vendor.objects.filter(name=line.strip())

					#if a vendor with this name is found, associate it with this event
					if len(vendorMatch) > 0:
						newEvent.vendors.add(vendorMatch[0])
						vendorMatch[0].eventCount += 1
						vendorMatch[0].save()

#this function is cited from: http://stackoverflow.com/questions/6116978/python-replace-multiple-strings	
def replace(text):
	#remove \r, (truck), (Truck), (cart), (Cart), (Tent), (tent), '
	rep = {"\r": "", "(truck)": "", "(Truck)": "", "(Cart)": "", "(cart)": "", "(Tent)": "", "(tent)":"", "'": "" } # define desired replacements here
	
	# use these three lines to do the replacement
	rep = dict((re.escape(k), v) for k, v in rep.iteritems())
	pattern = re.compile("|".join(rep.keys()))
	text = pattern.sub(lambda m: rep[re.escape(m.group(0))], text)
	return text