import requests
import json
 
purl = 'http://127.0.0.1:5000/upload'
files = {'the_file':open('test1.jpg', 'rb')}
ret = requests.post(purl, files = files) 
#response = requests.post(url, data = json.dumps(body), headers = headers)
print(ret.text)
print(ret.status_code)
