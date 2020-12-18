import json
import urllib.request
import urllib.parse
import urllib.error

api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

params = dict()
params["key"] = api_key
params["address"] = "Saint Petersburg State University"

url = serviceurl + urllib.parse.urlencode(params)

data = urllib.request.urlopen(url).read().decode()
data_json = json.loads(data)

print(data_json["results"][0]["place_id"])
