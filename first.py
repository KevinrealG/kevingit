from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
number = re.findall(b'>([0-9]+)', html)
list=[]
for n in number:
    x=n.decode()
    y=int(x)
    list.append(y)
print(sum(list))
