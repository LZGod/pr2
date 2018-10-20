def Download(name, page):
    #url = 'https://api.github.com/users/%s/repos?page=%d&per_page=100&access_token=%s' % (user_name, page, token)
    url = 'https://api.github.com/users/%s/repos?page=%d&per_page=100' % (name, page)#сюда нужно вставить свой токен, а то не будет доступа 
    response = urllib.request.urlopen(url)
    text = response.read().decode('utf-8')
    data = json.loads(text)  
    return data

def DownloadFolls(name):
    token = '8f64f0e6e3b8024ae8a27d9161834ac69769bff7'
    url = 'https://api.github.com/users/%s?access_token=%s' % (name, token)
    response = urllib.request.urlopen(url)
    text = response.read().decode('utf-8')
    data = json.loads(text)  
    return data['followers']

def Form(name, num):
    if (num % 10) == 1 and num != 11:
        return name + 'и'
    return name + 'ях'

def Pun(key, mean):
    out = key + ':'
    out = out.ljust(45, ' ')
    out = '  ' + out
    print(out, mean)

def UserData(name):
    n = 1
    langs = {}
    flag = False
    while True:
        data = Download(name, n)
        if len(data) == 0:
            break
        if not flag:
            print('Список его репозиториев:')
            flag = True
        for rep in data:
            Pun(rep['name'], rep['description'])
            lang = rep['language']
            if lang in langs:
                langs[lang] += 1
            else:
                langs[lang] = 1
        n += 1
        
    if not flag:
        print('У этого пользователя нет репозиториев')
        return
    
    langs.pop(None)
    print()
    print('Пользователь', name, 'пишет на', ', '.join([s for s in langs]))
    s = ', '.join(['язык %s используется в %s '%(lang, langs[lang]) + Form('репозитори', langs[lang]) for lang in langs])
    s = s[0].upper() + s[1:]
    print(s)

def UserInfo(name):
    n = 1
    langs = {}
    flag = False
    count_reps = 0
    while True:
        data = Download(name, n)
        if len(data) == 0:
            break
        if not flag:
            flag = True
        for rep in data:
            lang = rep['language']
            if lang in langs:
                langs[lang] += 1
            else:
                langs[lang] = 1
        count_reps += len(data)
        n += 1
    if not flag:
        return (0, ())
    return (count_reps, langs)

def CommInfo(names_list):
    max_reps = ('', 0)
    max_folls = ('', 0)
    pop_lang = ('', 0)
    langs = {}
    for name in names_list:
        count_folls = DownloadFolls(name)
        count_reps, langs = UserInfo(name)
        for lang in langs:
            if lang in langs:
                langs[lang] += langs[lang]
            else:
                langs[lang] = langs[lang]
        if count_folls > max_folls[1]:
            max_folls = (name, count_folls)
        if count_reps > max_reps[1]:
            max_reps = (name, count_reps)
    for lang in langs:
        if langs[lang] > pop_lang[1]:
            pop_lang = (lang, langs[lang])
    print()
    print('Из списка', ', '.join([name for name in names_list]), 'больше всего репозиториев у пользователя', max_reps[0])
    print('Самый популярный язык среди пользователей из списка', ', '.join([name for name in names_list]), '--', pop_lang[0])
    print('Больше всего подписчиков у пользователя', max_folls[0])

def main(names_list):
    flag = False
    print('Введите имя Github пользователя')
    while not flag:
        name = input()
        if not name in names_list:
            print('Вы ввели что-то не то. Повторите попытку ввода.')
        else:
            flag = True
    print('Вы выбрали пользователя', name)
    UserData(name)
    CommInfo(names_list)

import urllib.request
import json
NAMES_LIST = ['elmiram', 'maryszmary', 'lizaku', 'nevmenandr', 'ancatmara', 'roctbb', 'akutuzov', 'agricolamz', 'lehkost', 'kylepjohnson', 'mikekestemont', 'demidovakatya', 'shwars', 'JelteF', 'timgraham', 'arogozhnikov', 'jasny', 'bcongdon', 'whyisjake', 'gvanrossum']
main(NAMES_LIST)

