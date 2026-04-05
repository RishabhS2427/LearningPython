# https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films

import pandas as pd
import requests
import sqlite3 as sql
from bs4 import BeautifulSoup

from ETL.etl_practice import target_file

url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'
db_name = 'Movies.db'
table_name = 'Top_50'
target_file_1 = "top_25_movies.csv"
csv_path = 'top_50_films.csv'
df = pd.DataFrame(columns=["Average Rank", "Film", "Year"])
count = 0
html_page = requests.get(url).text
data = BeautifulSoup(html_page,'html.parser')
tables= data.find_all('tbody')
rows = tables[0].find_all('tr')
print(f"rows {rows}")

for item in rows:  # skip header row
    cols = item.find_all('td')

    if len(cols) >= 3:
        data_dict = {
            "Average Rank": cols[0].get_text(strip=True),
            "Film": cols[1].get_text(strip=True),
            "Year": cols[2].get_text(strip=True),
            "Rotten Tomatoes' Top 100": cols[3].get_text(strip=True)
        }

        df = pd.concat([df, pd.DataFrame([data_dict])], ignore_index=True)
        count += 1

    if count >= 25:
        break

df["Year"] = pd.to_numeric(df["Year"], errors='coerce')
df = df[df["Year"] >= 2000]
df.to_csv(target_file_1)

print(df)
df.to_csv(csv_path)
conn = sql.connect(db_name)
df.to_sql(table_name, conn, if_exists='replace', index=False)
conn.close()

