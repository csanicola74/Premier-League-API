import requests
import pandas as pd


endpoint = 'https://api.premierleague.com/v1/matches'
params = {'competitionId': '2022/23'}


response = requests.get(endpoint, params=params)


data = response.json()


df = pd.DataFrame(data['matches'])
df.columns = ['match_id', 'competition',
              'team_id', 'team_name', 'round', 'match_date']
df['match_date'] = pd.to_datetime(df['match_date'])


# Save the spreadsheet: Use the pandas.DataFrame.to_excel method to save the DataFrame as an Excel file.
