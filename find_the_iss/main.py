import requests
import json
import geocoder

url = 'http://api.open-notify.org/iss-now.json'

data = json.loads(requests.get(url).text)
'''
Sample Output:
{"timestamp": 1652139467, "iss_position": {"longitude": "150.0956", "latitude": "-29.4221"}, "message": "success"}
'''

print(type(data))

g = geocoder.ip('me')
print(g.latlng)