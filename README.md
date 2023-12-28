# Backtesting API Project

API pour Backtesting de Stratégies de Trading Algorithmique.


## Objectif du Projet
Le but de ce projet est de développer une API permettant aux utilisateurs de soumettre leurs propres stratégies de trading algorithmique pour backtesting. Le système doit être capable d’exécuter ces stratégies sur des données de marché historiques et de fournir des analyses de performance.


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
params = {"code": "fonction_de_trading", "indicateurs": ["avg_return", "sharp_ratio"], "start": "dd-mm-aaaa", "end": "dd-mm-aaaa", etc...}
response = requests.post(url, data=params)
```

Tous les arguments pris en compte sont les suivants :
- code :  prend les données historique et renvoie la position sur la prochaine période uniquement. Nous on évalue ses perfs avec le backtesting et on renvoie les indicateurs demandés
- indicateurs : liste d'indicateurs parmis les suivants avg_return, sharp_ratio, beta, 
- start : début de la période de backtesting
- end : fin de la période de backtesting
- actifs (univers d'investissement) : actifs à tester
- packages : packages requis pour exécuter la fonction de trading dans un environnement virtuel possédant uniquement python 3.9



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



