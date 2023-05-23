import requests
import pandas as pd


url = "https://premierleague-api.com/matches?season=2020&matchday=8"
headers = {"Authorization": "Bearer YOUR_API_KEY"}
response = requests.get(url, headers=headers)
data = response.json()


matches = pd.DataFrame(data)
