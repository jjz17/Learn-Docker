from cmath import inf
import json

# with open('json_data.json') as infile:
#     data = json.loads(infile.read())
#     print(type(data))
#     print(data)


# Opening JSON file
f = open('json_data.json',)
   
# returns JSON object as 
# a dictionary
data = json.load(f)
   
print(type(data))
   
# Closing file
f.close()