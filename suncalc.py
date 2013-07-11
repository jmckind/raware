from ephem import *

san_antonio = Observer()
san_antonio.lat = '29.416667'
san_antonio.lon = '-98.5'

sun = Sun()
sun.compute(san_antonio)

print "The sun's azimuth is %s. The sun's altitude is %s." % (sun.az, sun.alt)

local_sunrise = localtime(san_antonio.next_rising(sun)).strftime('%I:%M %p')
local_sunset = localtime(san_antonio.next_setting(sun)).strftime('%I:%M %p')

if local_sunrise > local_sunset:
	print "Today's sunset is at %s. Tomorrow's sunrise is at %s." % (local_sunset, local_sunrise)
else:
	print "Today's sunrise is at %s. Today's sunset is at %s. " % (local_sunrise, local_sunset)
