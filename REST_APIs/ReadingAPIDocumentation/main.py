import requests


def get_rhymes(word):
    base_url = 'https://api.datamuse.com/words'
    params_diction = {'rel_rhy': word, 'max': '3'}
    resp = requests.get(base_url, params=params_diction)

    word_ds = resp.json()
    return [d['word'] for d in word_ds]
    # return resp.json()


print(get_rhymes('funny'))
print(get_rhymes('dash'))
print(get_rhymes('jack'))

