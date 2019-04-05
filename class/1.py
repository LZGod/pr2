import urllib.request
#req = urllib.request.Request('https://api.vk.com/method/wall.get?owner_id=1&count=19&v=5.74&access_token=8423c2448423c2448423c244d08441f2a1884238423c244dee1644d9e90529494134bf8&offset=2')
req = urllib.request.Request('https://api.vk.com/method/wall.getComments?owner_id=1&post_id=2442097&count=2&v=5.74&access_token=8423c2448423c2448423c244d08441f2a1884238423c244dee1644d9e90529494134bf8')
response = urllib.request.urlopen(req)
result = response.read().decode('utf-8')
print(result)
import json
data = json.loads(result)
#print(data['response']['items'][]['text'])
