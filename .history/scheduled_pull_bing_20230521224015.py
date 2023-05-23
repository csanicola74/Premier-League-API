# Import libraries
import requests
import pandas as pd
import openpyxl
import schedule
import time

# Define constants
API_KEY = "your_api_key_here"
API_URL = "https://api.premierleague.com/football/data/competition/1/table"
FILE_NAME = "premier_league_table.xlsx"
SHEET_NAME = "weekly_data"

# Define a function that pulls data from API and writes to spreadsheet
def pull_and_write_data():
    # Make a request to API with API key
    headers = {"X-Auth-Token": API_KEY}
    response = requests.get(API_URL, headers=headers)
    # Check if response is successful
    if response.status_code == 200:
        # Parse JSON data into a dictionary
        data = response.json()
        # Create a DataFrame from dictionary
        df = pd.DataFrame(data["standings"][0]["table"])
        # Write DataFrame data to Excel file
        df.to_excel(FILE_NAME, sheet_name=SHEET_NAME, index=False)
        print("Data written successfully.")
    else:
        print("Request failed.")

# Schedule function to run once every week on Monday at 10:00 AM
schedule.every().monday.at("10:00").do(pull_and_write_data)

# Keep running until interrupted
while True:
    # Run pending scheduled tasks
    schedule.run_pending()
    # Wait for one second
    time.sleep(1)