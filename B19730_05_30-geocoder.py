"""Geocode with Geocoder"""

import geocoder
g = geocoder.osm("1403 Washington Ave, New Orleans, LA 70130")
print(g.geojson)
print()
print(g.wkt)
