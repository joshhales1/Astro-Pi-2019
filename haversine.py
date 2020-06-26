"""
Needed this at somepoint, may come in handy later.
"""
from math import radians, sin, cos, asin, sqrt
def haversine(long1, lat1, long2, lat2):
    long1, lat1, long2, lat2 = map(radians, [long1, lat1, long2, lat2])
    long_difference = long2 - long1
    lat_difference  = lat2 - lat1

    a = sin(lat_difference/2)**2 + cos(lat1)*cos(lat2)*sin(long_difference/2)**2
    c = 2*asin(sqrt(a))

    return c
