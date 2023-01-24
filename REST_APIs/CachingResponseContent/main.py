import requests
# it's not found in the permanent cache
res = requests.get('https://api.datamuse.com/words?rel_rhy=happy', params='datamuse_cache.txt')
print(res.text[:100])
# this time it will be found in the temporary cache
res = requests.get("https://api.datamuse.com/words?rel_rhy=happy", params="datamuse_cache.txt")
# This one is in the permanent cache.
res = requests.get("https://api.datamuse.com/words?rel_rhy=funny", params="datamuse_cache.txt")