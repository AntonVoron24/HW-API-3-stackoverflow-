import requests
import datetime as DT


todate = DT.datetime.fromisoformat(str(DT.datetime.today())).timestamp()
fromdate = DT.datetime.fromisoformat(str(DT.date.today() - DT.timedelta(days=2))).timestamp()
params = {
    'fromdate': round(int(fromdate), 0),
    'todate': round(int(todate), 0),
    'order': 'desc',
    'sort': 'activity',
    'tagged': 'python',
    'site': 'stackoverflow',
    'pagesize': 100,
    'page': 1
}

url = f'https://api.stackexchange.com/2.3/questions?'
resp = requests.get(url, params=params).json()

try:
    while resp['has_more']:
        resp = requests.get(url, params=params).json()
        for question in resp['items']:
            print(question['title'], question['link'])
        params['page'] += 1
except KeyError:
    print('Готово')
