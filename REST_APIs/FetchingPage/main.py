import requests

kval_pairs = {'rel_rhy': 'funny'}
page = requests.get('https://api.datamuse.com/words', params=kval_pairs)
print(page.text[:150])
print(page.url)

d = {'q': 'violins and guitars', 'tbm': 'isch'}
results = requests.get('https://google.com/search', params=d)
print(results.url)
print(results.text)
