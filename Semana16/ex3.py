import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup

url = "http://py4e-data.dr-chuck.net/known_by_Nia.html"

count_str = input("Enter count: ")
position_str = input("Enter position: ")

count = int(count_str)
position = int(position_str) - 1

aux = 0

# it stops on count
while aux <= count:
    print("Retrieving:", url)

    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")

    # find the link we want and saves it to url for the loop
    anchors = soup("a")
    anchor = anchors[position].get("href", None)
    url = anchor

    aux = aux + 1
