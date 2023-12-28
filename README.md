# Backtesting API Project

API pour Backtesting de Stratégies de Trading Algorithmique.


## Objectif du Projet
Le but de ce projet est de développer une API permettant aux utilisateurs de soumettre leurs propres stratégies de trading algorithmique pour backtesting. Le système doit être capable d’exécuter ces stratégies sur des données de marché historiques et de fournir des analyses de performance sur la période spécifiée.


## Fonctionnalités Clés

### 1. Soumission de Fonctions de Trading :
• L'utilisateur soumet une stratégie de trading que notre système va évaluer par backtesting sur des données de marché historiques. La fonction de trading prend la forme d'un script python et de plusieurs inputs afin de mesurer la performance de la stratégie.
• Le système contrôle les fonctions soumises pour garantir leur exécution sûre et conforme lors du backtesting.

### 2. Backtesting :
• L'analyse de la performance par backtesting est réalisé à partir de données de marché historiques des actifs de l'univers d'investissement. Nous utilisons les barres de prix OHLCV afin de calculer les différents indicateurs demandés par l'utilisateur.
• La réponse de l'API fournit des statistiques et des analyses de performance pour la stratégie testée.

### 3. Stockage et Exécution Programmée :
• L'API permet également de planifier des backtests à des intervalles spécifiés par l’utilisateur avec la même stratégie de trading. Ceci permet d'éviter de requêter plusieurs fois l'API avec la même fonction de trading.


## Utilisation

Les focntionnalités de backtesting de stratégie de trading algorithmique sont utilisable directement via une requête POST à l'API développée. Cette API prend en entrée plusieurs paramètres afin de renvoyer les indicateurs de performances souhaités à l'utilisateur.

Les paramètres d'entrée de l'API sont collectés par un dictionnaire json puis inséré dans la requête de l'API comme suit :

```python
params = {"code": "fonction_de_trading", "indicateurs": ["sharp_ratio"], "start": "01-01-2022", "end": "31-12-2022", "actifs": ["AAPL", "GOOGL"], "packages": ["numpy"], "reuse": False, "interval": 0}
response = requests.post(url, data=params)
```

Les arguments pris en compte sont les suivants :
- code : script python qui applique la stratégie de trading. La stratégie de trading doit prendre en entrée des données historiques d'actifs et renvoyer la position sur la prochaine période. Les données historiques peuvent être consultées en appelant une fonction externe "load_data(asset, start, end)" et qui renvoie un dataframe avec une ligne par jour de trading et les variables suivantes :
    - Open Time (t): The start time of the candlestick.
    - Open (o): The opening price of the candlestick.
    - High (h): The highest price during the candlestick's time period.
    - Low (l): The lowest price during the candlestick's time period.
    - Close (c): The closing price of the candlestick.
    - Volume (v): The total traded base asset volume during the candlestick's time period.
    - Close Time (T): The closing time of the candlestick.
    - Quote Asset Volume (q): The total traded quote asset volume during the candlestick's time period.
    - Number of Trades (n): The number of trades that occurred during the candlestick's time period.
    - Taker Buy Base Asset Volume (V): The total traded base asset volume attributed to taker buys during the candlestick's time period.
    - Taker Buy Quote Asset Volume (Q): The total traded quote asset volume attributed to taker buys during the candlestick's time period.
- indicateurs : liste d'indicateurs parmis les suivants : return (rendement moyen), vol (volatilité du portefeuille), sharp_ratio (ratio de sharp de l'investissement) et beta (sensibilité de la valeur de l'actif aux variations du marché)
- start : début de la période de backtesting au format "dd-mm-aaaa"
- end : fin de la période de backtesting au format "dd-mm-aaaa"
- actifs (univers d'investissement) : actifs à tester parmis la liste suivante : "AAPL", "MSFT", "AMZN", "NVDA", "GOOGL", "TSLA", "META", "GOOG", "BRK.B" et "UNH"
- packages : liste de packages (pip) requis pour exécuter la fonction de trading dans un environnement virtuel possédant uniquement python 3.10
- reuse : True ou False pour indiquer si l'utilisateur veut planifier d'autres backtests dans le futur
- interval : int, nombre de mois d'intervalle entre chaque backtest à partir de la date de requête

### Exemple d'utilisation

```python 
import requests

# URL de l'API
url = "https://exemple.com/api/endpoint"

# Code Python que vous souhaitez envoyer
script_code = """
print("Hello, world!")
"""

# Paramètres de la requête POST
payload = {
    'code': script_code
}

# Envoi de la requête POST
response = requests.post(url, data=payload)

# Lecture de la réponse JSON
json_data = response.json()
```



