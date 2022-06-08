import json
import requests
import time

file = open('json_data.json')
data = json.load(file)
# print(type(data))
# print(data)

# API link
url = 'http://api.open-notify.org/iss-now.json'
new_data = {}

for _ in range(1):
    iss_data = json.loads(requests.get(url).text)
    iss_loc = iss_data['iss_position']
    iss_latlon = {'lat': float(iss_loc['latitude']), 'lon': float(iss_loc['longitude'])}
    new_data[int(time.time())] = (iss_latlon)
    # print('running...')
    time.sleep(30)

# Append new data to existing data
data.update(new_data)
# print(data)
# json_string = json.dumps(data)

with open('json_data.json', 'w') as outfile:
    json.dump(data, outfile)

print('working')