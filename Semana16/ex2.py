import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup

html = urllib.request.urlopen(
    "http://py4e-data.dr-chuck.net/comments_1071018.html").read()
soup = BeautifulSoup(html, "html.parser")

total = 0
comments_amount = 0

numbers = soup('span')
for number in numbers:
    num_int = int(number.contents[0])
    total = total + num_int
    comments_amount = comments_amount + 1

print("Count", comments_amount)
print("Sum", total)
