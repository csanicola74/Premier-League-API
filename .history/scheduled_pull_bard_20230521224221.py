import requests
import pandas as pd


def get_premier_league_data():
    """Gets the latest data from the Premier League API."""
    url = "https://api.premierleague.com/v1/competitions/2021-2022/matches"
    response = requests.get(url)
    data = response.json()
    return data


def write_premier_league_data_to_spreadsheet(data):
    """Writes the data from the Premier League API to a spreadsheet."""
    df = pd.DataFrame(data)
    df.to_excel("premier_league_data.xlsx")


def main():
    """The main function."""
    data = get_premier_league_data()
    write_premier_league_data_to_spreadsheet(data)


if __name__ == "__main__":
    main()


# then cron job
