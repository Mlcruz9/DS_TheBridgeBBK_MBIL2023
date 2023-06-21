import hashlib
import requests
import datetime
import pandas as pd
from variables import *

def hash_params(timestamp,priv_key,pub_key):
    """ Marvel API requires server side API calls to include
    md5 hash of timestamp + public key + private key """

    hash_md5 = hashlib.md5()
    hash_md5.update(f'{timestamp}{priv_key}{pub_key}'.encode('utf-8'))
    hashed_params = hash_md5.hexdigest()

    return hashed_params


def create_df(offset, inicial):

    params = {'ts': timestamp,
            'apikey': pub_key, 
            'hash': hash_params(timestamp,priv_key,pub_key),
            'offset': offset,
            'nameStartsWith': inicial,
            'limit': 100};

    url = 'http://gateway.marvel.com/v1/public/characters'

    res = requests.get(url,params=params)

    data = res.json()

    id = []
    name = []
    url = []

    for i in range(len(data['data']['results'])):

        id.append(data['data']['results'][i]['id'])
        name.append(data['data']['results'][i]['name'])
        url.append(data['data']['results'][i]['thumbnail']['path'] + '.' + data['data']['results'][i]['thumbnail']['extension'])

    df = pd.DataFrame({'id': id, 'name': name, 'url': url})

    return df