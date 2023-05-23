
import pandas as pd
url = f"https://api. Premier League.com/data/v1/teams/{team_id}/matchdays/{day_number}/results"
data = requests.get(url)


data = requests.get(url)
df = pd.DataFrame(data.json())
df.describe()


df.to_csv(" Premier League Data.csv", index=False)
