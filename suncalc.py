from ephem import *

_default_locations = [
	'Chicago',
	'Atlanta',
	'New York',
	'London',
	'Frankfurt',
	'New Delhi',
	'Hong Kong',
	'Tokyo',
	'Los Angeles'
]

def fetch_observers(locations = _default_locations):
	result = []
	for location in locations:
		result.append(city(location))
	return result

def observe_body(observer, body):
	body.compute(observer)
	
	print observer.name
	print "\tAltitude: %s Azimuth: %s" % (body.alt, body.az)

	local_sunrise = localtime(observer.next_rising(body))
	local_sunset = localtime(observer.next_setting(body))

	fmt_sunrise = local_sunrise.strftime('%I:%M %p')
	fmt_sunset = local_sunset.strftime('%I:%M %p')

	if local_sunrise > local_sunset:
		print "\tSetting at %s. Rising at %s." % (fmt_sunset, fmt_sunrise)
	else:
		print "\tRising at %s. Setting at %s. " % (fmt_sunrise, fmt_sunset)

def observe_sun_altitude(observer):
	sun = Sun()
	sun.compute(observer)
	return sun.alt

def display_body_stats(body):
	print body.name
	for observer in fetch_observers():
		observe_body(observer, body)

def display_sunniest_location():
	locations = [
		'Dallas',
		'Chicago',
		'Washington',
		'London',
		'Hong Kong',
		'Sydney'
	]

	observers = fetch_observers(locations)
	observers.sort(key=observe_sun_altitude, reverse=True)

	print "The sunniest location is %s" % observers[0].name

def main():
	display_body_stats(Sun())
	display_sunniest_location()

if __name__ == "__main__":
    main()