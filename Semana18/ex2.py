import json
import urllib.request
import urllib.parse
import urllib.error

total = 0

url = "http://py4e-data.dr-chuck.net/comments_1071021.json"
print("Retrieving", url)

data = urllib.request.urlopen(url).read().decode()
data_json = json.loads(data)

for comment in data_json["comments"]:
    total = total + int(comment["count"])

print(total)
