import urllib.request
import os
import re
import urllib.parse

def get_url(url):
    try:
        page = urllib.request.urlopen(url)
        text = page.read().decode('utf-8')
        return text
    except:
        print("Error at", url)

def meta(text):
    author = ''
    title = ''
    date = ''
    year = ''
    month = ''
    source = ''
    r = re.search("<strong>Автор:</strong> <a>(.*?)</a>", text)
    if r:
        author = r.group(1)
        
    r = re.search("<header><a>(.*?)</a></header>", text)
    if r:
        title = r.group(1)
    
    r = re.search("<time>(.*?)</time>", text)
    if r:
        date = r.group(1)
        date = re.sub('-', '.', date)
        year = date.split(".")[2]
        month = date.split(".")[1]
    
    r = re.search("action= '(.*?)'", text)
    if r:
        source = r.group(1)
    
    return author, title, date, year, month, source

def plain(text, meta):
    plain_text = []    
    text = text.split('\n')
    for line in text:
        r = re.search('<p.*?>(.+?)</p>', line)
        if r:
            plain_text.append(r.group(1))
            
    plain_text = '\n'.join(plain_text)
    plain_text = re.sub('<br />', '\n', plain_text)
    plain_text = re.sub('<.*?>', '', plain_text)
    
    path = "." + os.sep + "paper" + os.sep + "plain" + os.sep + meta[3] + os.sep + meta[4]
    if not os.path.exists(path):
        os.makedirs(path)
    file = "%s\\%s.txt" % (path, str(len(os.listdir(path))+1))
    with open(file, 'w', encoding='utf-8') as t:
        t.write(plain_text)
    
    row = '%s\t%s\t%s\t%s\tпублицистика\tNone\tнейтральный\t\
    n-возраст\tn-уровень\tрайонная\t%s\tАвангард\t\
    %s\tгазета\tРоссия\tВавожский район\tru'
    with open ('metadata.csv', 'a', encoding='utf-8') as t:
        t.write(row %(file, meta[0], meta[1], meta[2], meta[5], meta[3]) + '\n')    
    return plain_text

def stem(meta):
    inp = os.path.join('.', 'paper', 'plain', meta[3], meta[4])
    name = len(os.listdir(inp))
    out = os.path.join('.', 'paper', 'mystem-plain', meta[3], meta[4])
    if not os.path.exists(out):
        os.makedirs(out)
    os.system('mystem.exe -cgid --eng-gr ' + inp + os.sep + str(name) + '.txt' + ' '  + out + os.sep + str(name) + '.txt')          
    out = os.path.join('.', 'paper', 'mystem-xml', meta[3],meta[4])
    if not os.path.exists(out):
        os.makedirs(out)
    os.system('mystem.exe -cgid --eng-gr ' + inp + os.sep + str(name) + '.txt' + ' '  + out + os.sep + str(name) + '.xml')

def ft(plain_text, meta):    
    path = os.path.join('.', 'paper', 'plain', meta[3], meta[4])
    file = "%s\\%s.txt" % (path, str(len(os.listdir(path))))    
    with open(file, 'w', encoding='utf-8') as t:
        t.write('@au %s\n@ti %s\n@da %s\n@topic %s\n@url %s\n\n%s' %(meta[0], meta[1], meta[2], None, meta[5], plain_text))

def main():
    common_url = 'http://moyaokruga.ru/avangard-vavozh/Articles.aspx?articleId='

    row = 'path\tauthor\theader\tcreated\tsphere\
    \ttopic\tstyle\taudience_age\taudience_level\
    \taudience_size\tsource\tpublication\tpubl_year\
    \tmedium\tcountry\tregion\tlanguage'
    with open ('metadata.csv', 'w', encoding='utf-8') as t:
        t.write(row + '\n')
    
    for i in range(205071, 205571):
        page_url = common_url + str(i)  
        page_url = urllib.parse.urlsplit(page_url)
        page_url = list(page_url)
        page_url[2] = urllib.parse.quote(page_url[2])
        page_url = urllib.parse.urlunsplit(page_url)
        
        text = get_url(page_url)
        met = meta(text)
        plain_text = plain(text, met)
        stem(met)
        ft(plain_text, met)
    print("over")

if __name__ == "__main__":
    main()
