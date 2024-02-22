import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


json_data = {
    'code': 'ok',
    'start': '2022-01-01',
    'end': '2023-01-01',
    'assets': ["BTC", "ETH", "BNB"]
}


def fetch_binance_data(asset, start, end):
    api_url = 'https://api.binance.com/api/v3/klines'

    # Convertir les temps en millisecondes
    start = int(start.timestamp() * 1000)
    end = int(end.timestamp() * 1000)

    params = {
        'symbol': asset,
        'interval': '1h',
        'startTime': start,
        'endTime': end,
        'limit': 100000
    }

    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data, columns=['Open Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close Time',
                                         'Quote Asset Volume', 'Number of Trades', 'Taker Buy Base Asset Volume',
                                         'Taker Buy Quote Asset Volume', 'ignore'])
        df['Open Time'] = pd.to_datetime(df['Open Time'], unit='ms')
        df['Close Time'] = pd.to_datetime(df['Close Time'], unit='ms')
        df.drop(['ignore'], axis=1, inplace=True)
        return df
    else:
        print("Erreur lors de la récupération des données:", response.status_code)
        return None


def load_all_data(assets, start, end):
    data = dict()
    for asset in assets:
        data[asset] = fetch_binance_data(asset=f"{asset}USDT", start=start, end=end)
    return data


if __name__ == "__main__":
    start_date = pd.Timestamp(json_data["start"])
    end_date = pd.Timestamp(json_data["end"])
    assets = json_data["assets"]
    dict_data = load_all_data(assets=assets, start=start_date, end=end_date)
    print(dict_data)


