import requests
import json

page = requests.get('https://api.datamuse.com/words?rel_rhy=funny')
print(type(page))
print(page.text)
print(page.url)
print('------------')
x = page.json()
print(type(x))
print('--------First item in the list---------')
print(x[0])
print('--------The whole list, pretty printed----------')
print(json.dumps(x, indent=2))
