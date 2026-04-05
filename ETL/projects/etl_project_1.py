# Code for ETL operations on Country-GDP data
# Importing the required libraries

import pandas as pd
import sqlite3 as sql
import numpy as np
from bs4 import BeautifulSoup
from datetime import datetime
import requests

# Initilze all the known entities
url = 'https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'

table_attributes = ["Country", "GDP_USD_millions"]
table_name = "Countries_by_GDP"
csv_path = "./output/Countries_by_GDP.csv"
db_name = "World_Economics.db"


def extract(url, table_attribs):
    ''' This function extracts the required
    information from the website and saves it to a dataframe. The
    function returns the dataframe for further processing. '''
    page = requests.get(url).text
    data = BeautifulSoup(page, 'html.parser')
    df = pd.DataFrame(columns=table_attribs)
    table = data.find_all('tbody')
    # print(table)
    rows = table[2].find_all('tr')
    print(rows)
    for row in rows:
        col = row.find_all('td')
        if len(col) != 0:
            if col[0].find('a') is not None and '—' not in col[2]:
                dict_data = {"Country" : col[0].get_text(strip=True),
                             "GDP_USD_millions": col[2].get_text(strip=True),
                             }
                df1 = pd.DataFrame(dict_data, index=[0])
                df = pd.concat([df,df1], ignore_index=True)
    print(df)
    return df



def transform(df):
    ''' This function converts the GDP information from Currency
    format to float value, transforms the information of GDP from
    USD (Millions) to USD (Billions) rounding to 2 decimal places.
    The function returns the transformed dataframe.'''

    gdp_list = df["GDP_USD_millions"].tolist()
    print(f"gdp_list: {gdp_list}")
    gdp_list = [np.round(float("".join(x.split(",")))/1000,2) for x in gdp_list]
    print(f"after transform gdp_list: {gdp_list}")
    df["GDP_USD_millions"] = gdp_list
    df = df.rename(columns = {"GDP_USD_millions": "GDP_USD_billions"})
    print(df)
    # gdp_list = [np.round(x/1000, 2) for x in gdp_list]
    return df


def load_to_csv(df, csv_path):
    ''' This function saves the final dataframe as a `CSV` file
    in the provided path. Function returns nothing.'''
    df.to_csv(csv_path, index=False)


def load_to_db(df, sql_connection, table_name):
    ''' This function saves the final dataframe as a database table
    with the provided name. Function returns nothing.'''
    df.to_sql(table_name,sql_connection, if_exists='replace', index=False)

def run_query(query_statement, sql_connection):
    ''' This function runs the stated query on the database table and
    prints the output on the terminal. Function returns nothing. '''
    print(query_statement)
    query_data = pd.read_sql_query(query_statement, sql_connection)
    print(query_data)
    print(f"Data in json{query_data.to_json(orient='records')}")

# def log_progress(message):
#     ''' This function logs the mentioned message at a given stage of the code execution to a log file. Function returns nothing'''
#
#
# ''' Here, you define the required entities and call the relevant
# functions in the correct order to complete the project. Note that this
# portion is not inside any function.'''



# extraction process
print("ETL PROCESS START")
print("DATA EXTRACTION START")
df_extracted = extract(url, table_attributes)
print("DATA EXTRACTION SUCCESS")
print("DATA TRANSFORMATION START")
# Transform process
df = transform(df_extracted)
print("DATA TRANSFORMATION SUCCESS")
print("DATA LOAD IN CSV START")
# load into csv
load_to_csv(df_extracted, csv_path)

print("DATA LOAD IN DB START")
sql_connection = sql.connect(db_name)
load_to_db(df, sql_connection, table_name)

statement_1 = f"SELECT * FROM {table_name} WHERE GDP_USD_billions >=100"
run_query(statement_1, sql_connection)

sql_connection.close()


