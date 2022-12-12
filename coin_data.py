import os
import requests

def get_coin_data(id='british-pound-sterling'):
    coin_url_template = 'https://api.coincap.io/v2/rates/{id}'
    
    coin_url = coin_url_template.format(id=id)
    resp = requests.get(coin_url)
    
    if resp.ok:
        return resp.json()
    else:
        return resp.reason

def retrieve_coin_data(id):
    coin = get_coin_data(id)['data']
    info = ['symbol', 'currencySymbol', 'type', 'rateUsd']
    info_dict = dict((i, coin[i]) for i in info if i in coin)
    
    return info_dict

if __name__ == '__main__':
    data = retrieve_coin_data('british-pound-sterling')