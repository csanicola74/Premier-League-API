import requests
import pandas as pd


endpoint = 'https://api.premierleague.com/v1/matches'
params = {'competitionId': '2022/23'}


response = requests.get(endpoint, params=params)


data = response.json()
