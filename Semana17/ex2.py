import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET

total = 0
counter = 0

url = "http://py4e-data.dr-chuck.net/comments_1071020.xml"
print("Retrieving", url)

data = urllib.request.urlopen(url).read()

xml_tree = ET.fromstring(data)
total_count = xml_tree.findall(".//count")

for individual_count in total_count:
    integer = int(individual_count.text)
    total = total + integer
    counter = counter + 1

print("Retrieved", counter, "comments")
print("Sum:", total)
