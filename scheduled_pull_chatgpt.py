import requests
import pandas as pd


def retrieve_premier_league_data():
    # Make a request to the Premier League API and retrieve the data
    response = requests.get("https://api.example.com/premier-league")

    if response.status_code == 200:
        # Process the API response and extract the relevant data
        data = response.json()

        # Create a pandas DataFrame with the data
        df = pd.DataFrame(data)

        return df
    else:
        print("Failed to retrieve data from the Premier League API.")
        return None


def generate_spreadsheet():
    # Retrieve Premier League data
    premier_league_data = retrieve_premier_league_data()

    if premier_league_data is not None:
        # Create a spreadsheet using pandas
        spreadsheet = pd.ExcelWriter(
            'premier_league_data.xlsx', engine='xlsxwriter')
        premier_league_data.to_excel(
            spreadsheet, sheet_name='Premier League Data', index=False)

        # Save the spreadsheet
        spreadsheet.save()
        print("Spreadsheet generated successfully.")
    else:
        print("Spreadsheet generation failed.")


# Call the generate_spreadsheet function to generate the spreadsheet
generate_spreadsheet()


# CRON JOB
# chmod +x generate_premier_league_spreadsheet.py
# python generate_premier_league_spreadsheet.py
# crontab -e
# 0 22 * * * /path/to/python /path/to/generate_premier_league_spreadsheet.py
