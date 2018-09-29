
# coding: utf-8

# In[1]:

for i in range(1, 3):
    print(i)


# In[3]:

jsonstr = """{"song": "Roxanne",
              "artist": "The Police",
              "album": "The Very Best of 70s"
              "album artists": {"first": "The Police",
                                "second": "Rainbow",
                                "third": "Led Zeppelin"
                               }
             }"""
import json
data = json.loads(jsonstr)
print(type(data))


# In[5]:

jsonstr = """{"song": "Roxanne",
              "artist": "The Police",
              "album": "The Very Best of 70s"
              "album artists": {"first": "The Police", "second": "Rainbow","third": "Led Zeppelin"},
             }"""
import json
data = json.loads(jsonstr)
print(type(data))


# In[4]:

jsonstr = """{"song": "Roxanne",
              "artist": "The Police",
              "album": "The Very Best of 70s"
              "album artists": {"first": "The Police",
                                "second": "Rainbow",
                                "third": "Led Zeppelin"
                               }
             }"""
import json
data = json.loads(jsonstr)
print(type(data))


# In[7]:

jsonstr = """{"song": "Roxanne",
              "artist": "The Police",
              "album": "The Very Best of 70s"
              "album artists": {"first": "The Police", "second": "Rainbow", "third": "Led Zeppelin"}}"""
import json
data = json.loads(jsonstr)
print(type(data))


# In[13]:

json_string = """{"organisation": "Python Software Foundation",
                 "officers": [
                            {"first_name": "Guido", "last_name":"Rossum", "position":"president"},
                            {"first_name": "Diana", "last_name":"Clarke", "position":"chair"},
                            {"first_name": "Naomi", "last_name":"Ceder", "position":"vice chair"},
                            {"first_name": "Van", "last_name":"Lindberg", "position":"vice chair"},
                            {"first_name": "Ewa", "last_name":"Jodlowska", "position":"director of operations"}
                            ],
                "type": "non-profit",
                "country": "USA",
                "founded": 2001,
                "members": 244,
                "budget": 750000,
                "url": "www.python.org/psf/"}"""
import json
data = json.loads(json_string)
print(type(data))
from pprint import pprint as pp
pp(data)
for key in data:
    print(key, end = ' ')
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii = False, indent = 4)



# In[14]:

import json
import urllib.request
user = "lzgod"
url = 'https://api.github.com/users/lzgod/repos' 
response = urllib.request.urlopen(url)  
text = response.read().decode('utf-8')  
data = json.loads(text)
print(len(data))  
for i in data:
    print(i["name"])


# In[ ]:



