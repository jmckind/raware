from ephem import *

locations = {
	'Dallas/Ft. Worth': ('32.775833', '-96.796667'),
	'London': ('51.507222', '-0.1275'),
	'Hong Kong': ('22.24819', '114.20340'),
	'Australia': ('-23.484168', '134.119034'),
	'Los Angeles': ('34.05', '-118.25'),
	'New York': ('40.67', '-73.94'),
}

observers = dict()

for location in locations:
	coordinates = locations.get(location)

	o = Observer()
	o.lat, o.lon = coordinates

	observers[location] = o

sun = Sun()
	
for observer_name in observers:
	observer = observers[observer_name]

	sun.compute(observer)

	print observer_name
	print "\tAltitude: %s Azimuth: %s" % (sun.alt, sun.az)

	local_sunrise = localtime(observer.next_rising(sun)).strftime('%I:%M %p')
	local_sunset = localtime(observer.next_setting(sun)).strftime('%I:%M %p')

	if local_sunrise > local_sunset:
		print "\tToday's sunset is at %s. Tomorrow's sunrise is at %s." % (local_sunset, local_sunrise)
	else:
		print "\tToday's sunrise is at %s. Today's sunset is at %s. " % (local_sunrise, local_sunset)
