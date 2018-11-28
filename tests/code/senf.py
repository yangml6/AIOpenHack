import requests
import json
 
purl = 'http://104.215.148.185:5000/upload'
files = {'the_file':open('/Users/yml/Desktop/bc.jpg', 'rb')}
ret = requests.post(purl, files = files) 
#response = requests.post(url, data = json.dumps(body), headers = headers)
print(ret.text)
print(ret.status_code)
