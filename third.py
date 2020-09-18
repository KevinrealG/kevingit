import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
def Retrievi(url,p):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    lis=[]
    for tag in tags:
        lis.append(tag.get('href', None))
    return lis[p-1]

url = input('Enter - ')
count=input("Enter count: ")
position=input("Enter position: ")
p=int(position)
c=int(count)
urls=[url]
u=url
for i in range(c):
    u=Retrievi(u,p)
    urls.append(u)
for ur in urls:
    print("Retrievig: ",ur)
