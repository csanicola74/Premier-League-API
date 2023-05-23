To generate a spreadsheet that pulls data from an API in Python, you can use the requests library to make HTTP requests to the API, and the pandas library to manipulate and store the data in a spreadsheet format. Here is an example of how you can do this:

Install the required libraries: You can install the requests and pandas libraries using pip, by running the following commands in your terminal:
pip install requests
pip install pandas
Import the libraries: In your Python script, import the requests and pandas libraries:
import requests
import pandas as pd
Define the API endpoint and parameters: Define the API endpoint, which is the URL of the API, and the parameters, which are the data you want to retrieve. For example:
endpoint = 'https://api.premierleague.com/v1/matches'
params = {'competitionId': '2022/23'}
Here, we are retrieving data for the 2022/23 competition.

Make the request: Use the requests.get function to make a GET request to the API endpoint with the specified parameters:
response = requests.get(endpoint, params=params)
Get the data: Get the data from the response using the .json() method, and store it in a variable. For example:
data = response.json()
Create the spreadsheet: Use the pandas.DataFrame constructor to create a DataFrame from the data, and specify the column names and data types. For example:
df = pd.DataFrame(data['matches'])
df.columns = ['match_id', 'competition', 'team_id', 'team_name', 'round', 'match_date']
df['match_date'] = pd.to_datetime(df['match_date'])
Here, we are creating a DataFrame with columns for match ID, competition, team ID, team name, round, and match date. We are also converting the match date column to a datetime type.

Save the spreadsheet: Use the pandas.DataFrame.to_excel method to save the DataFrame as an Excel file.