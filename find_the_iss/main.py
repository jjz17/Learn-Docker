import requests
import json
import geocoder
import haversine as hs
import math

url = 'http://api.open-notify.org/iss-now.json'

data = json.loads(requests.get(url).text)
'''
Sample Output:
{"timestamp": 1652139467, "iss_position": {"longitude": "150.0956", "latitude": "-29.4221"}, "message": "success"}
'''

print(type(data))

g = geocoder.ip('me')
# print(g.latlng)
my_latlon = g.latlng

iss_loc = data['iss_position']
iss_latlon = [float(iss_loc['latitude']), float(iss_loc['longitude'])]
# my_loc = {'longitude': my_latlon[1], 'latitude': my_latlon[0]}
print(iss_latlon, my_latlon)



def calculate_initial_compass_bearing(pointA, pointB):
    """
    Calculates the bearing between two points.
    The formulae used is the following:
        θ = atan2(sin(Δlong).cos(lat2),
                  cos(lat1).sin(lat2) − sin(lat1).cos(lat2).cos(Δlong))
    :Parameters:
      - `pointA: The tuple representing the latitude/longitude for the
        first point. Latitude and longitude must be in decimal degrees
      - `pointB: The tuple representing the latitude/longitude for the
        second point. Latitude and longitude must be in decimal degrees
    :Returns:
      The bearing in degrees
    :Returns Type:
      float
    """
    # if (type(pointA) != tuple) or (type(pointB) != tuple):
    #     raise TypeError("Only tuples are supported as arguments")

    lat1 = math.radians(pointA[0])
    lat2 = math.radians(pointB[0])

    diffLong = math.radians(pointB[1] - pointA[1])

    x = math.sin(diffLong) * math.cos(lat2)
    y = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1)
            * math.cos(lat2) * math.cos(diffLong))

    initial_bearing = math.atan2(x, y)

    # Now we have the initial bearing but math.atan2 return values
    # from -180° to + 180° which is not what we want for a compass bearing
    # The solution is to normalize the initial bearing as shown below
    initial_bearing = math.degrees(initial_bearing)
    compass_bearing = (initial_bearing + 360) % 360

    return compass_bearing

print(calculate_initial_compass_bearing(my_latlon, iss_latlon))

'''
Sanity Check:
http://dwtkns.com/pointplotter/

[50.724, 32.2597] [41.577, -73.4085]
41.352393970541186

32.2597,50.724
-73.4085,41.577


[39.4708, -75.7349] [41.577, -73.4085]
220.77847952512127

-75.7349,39.4708
-73.4085,41.577
'''