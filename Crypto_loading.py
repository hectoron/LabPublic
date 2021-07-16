#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import requests


# In[53]:


def Get_Crypto_Data(df):
    URL = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false"
    response = requests.get(URL)
    data = response.json()
    df = pd.DataFrame.from_dict(data, orient='columns')
    df = df.drop(columns=['image'
        , 'fully_diluted_valuation'
        , 'fully_diluted_valuation'
        , 'total_volume'
        , 'high_24h'
        , 'low_24h'
        , 'price_change_24h'
        , 'price_change_percentage_24h'
        , 'market_cap_change_24h'
        , 'market_cap_change_percentage_24h'
        , 'circulating_supply'
        , 'total_supply'
        , 'max_supply'
        , 'ath'
        , 'ath_change_percentage'
        , 'ath_date'
        , 'atl'
        , 'atl_change_percentage'
        , 'atl_date'
        , 'roi'
        , 'last_updated'])
    return df


# In[59]:


def get_output_schema():
    return pd.DataFrame({
        'id': prep_string(),
        'symbol': prep_string(),
        'name': prep_string(),
        'current_price': prep_decimal(),
        'market_cap': prep_int(),
        'market_cap_rank': prep_int(),
    })
