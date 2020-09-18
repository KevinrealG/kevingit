import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter - ')
data = urllib.request.urlopen(url, context=ctx).read()
info = json.loads(data)
print('Retrieved', len(data), 'characters')


sum=0
for item in info['comments']:
    sum+=int(item['count'])

print("Sum: ",sum)
