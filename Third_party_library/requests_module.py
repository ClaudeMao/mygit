import requests

r = requests.get('https://www.pornhub.com')
print(r.status_code)
print(r.encoding)

b = requests.get('https://search.bilibili.com/all', params={'keyword': 'GUILTY CROWN'})
print(b.url)
print(r.encoding)
print(b.status_code)