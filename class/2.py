import urllib.request
from datetime import datetime
import json
#req = urllib.request.Request('https://api.vk.com/method/wall.get?owner_id=1&count=2&v=5.74&access_token=8423c2448423c2448423c244d08441f2a1884238423c244dee1644d9e90529494134bf8&offset=2')
#response = urllib.request.urlopen(req)
#result = response.read().decode('utf-8')
#data = json.loads(result)
#text = data['response']['items'][1]['text']
#utc = datetime.fromtimestamp(tim) 
#print(utc)
users = set()
offsets = [0, 1000, 2000, 3000, 4000, 5000]
token = '8423c2448423c2448423c244d08441f2a1884238423c244dee1644d9e90529494134bf8'
version = '5.92'
group = 'dormitory8hse'

for off in offsets:
    req = urllib.request.Request('https://api.vk.com/method/groups.getMembers?group_id=%s&access_token=%s&v=%s&offset=%s'  % (group, token, version, off))
    response = urllib.request.urlopen(req)
    result = response.read().decode('utf-8')
    data = json.loads(result) 
    users = users | set(data['response']['items'])
print(len(users))
