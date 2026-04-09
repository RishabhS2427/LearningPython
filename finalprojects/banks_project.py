
#
# Final project overview
# Estimated effort: 5 mins
# In this project, you will put all the skills acquired throughout the course and your knowledge of basic Python to test. You will work on real-world data and perform the operations of Extraction, Transformation, and Loading as required. Throughout the project, you will note some outputs you need to answer questions on the graded quiz. You will also take snapshots, which you will upload in the AI-Graded or Peer-Graded Assignment, depending on the option you selected.
#
# Project Scenario
# A multi-national firm has hired you as a data engineer. Your job is to access and process data as per requirements.
#
# Your boss asked you to compile the list of the top 10 largest banks in the world ranked by market capitalization in billion USD. Further, you need to transform the data and store it in USD, GBP, EUR, and INR per the exchange rate information made available to you as a CSV file. You should save the processed information table locally in a CSV format and as a database table. Managers from different countries will query the database table to extract the list and note the market capitalization value in their own currency.
#
# Directions
# 1) Write a function to extract the tabular information from the given URL under the heading By Market Capitalization, and save it to a data frame.
#
# 2) Write a function to transform the data frame by adding columns for Market Capitalization in GBP, EUR, and INR, rounded to 2 decimal places, based on the exchange rate information shared as a CSV file.
#
# 3) Write a function to load the transformed data frame to an output CSV file.
#
# 4) Write a function to load the transformed data frame to an SQL database server as a table.
#
# 5) Write a function to run queries on the database table.
#
# 6) Run the following queries on the database table: a. Extract the information for the London office, that is Name and MC_GBP_Billion b. Extract the information for the Berlin office, that is Name and MC_EUR_Billion c. Extract the information for New Delhi office, that is Name and MC_INR_Billion
#
# 7) Write a function to log the progress of the code.
#
# 8) While executing the data initialization commands and function calls, maintain appropriate log entries.


import pandas as pd
import requests
import sqlite3 as sql
from bs4 import BeautifulSoup
from datetime import datetime as dt

from pandas.core.interchange.dataframe_protocol import DataFrame

url = "https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks"
table_attributes = ["Name", "MC_USD_Billion"]
table_attributes_final = ["Name", "MC_USD_Billion", "MC_GBP_Billion", "MC_EUR_Billion", "MC_INR_Billion"]
outputCSVPath = "./output/Largest_banks_data.csv"
db_name ="./output/Banks.db"
table_name_bank_largest = "Largest_banks"
inputCSVPath = "./input/exchange_rate.csv"
def log_progress(message):
    time_format = "%Y-%m-%d %H:%M:%S"
    now = dt.now().strftime(time_format)
    with open("./output/code_log.txt", "a") as log:
        log.write(now + ": " + message + "\n")
    print(now,message) # print logs into terminal reference purpose

def extract (url):
    html_page = requests.get(url).text
    html_parser = BeautifulSoup(html_page, 'html.parser')
    tables = html_parser.find_all('tbody')
    rows = tables[0].find_all('tr')
    data_list = []
    for row in rows:
        col = row.find_all('td')
        if len(col)!=0 :
            data_dict = {
                "Bank name": col[1].text.strip(),
                "Market cap US$ Billion": col[2].text.strip()
            }
            data_list.append(data_dict)
    df = pd.DataFrame(data_list)
    print("Data Frame",df)
    return df

def transform (df, table_attributes_final, df_exchange):
    # Name
    df[table_attributes_final[0]] = df['Bank name']
    # Market cap US$ Billion
    df['Market cap US$ Billion'] = pd.to_numeric(df['Market cap US$ Billion'])
    df[table_attributes_final[1]] = df['Market cap US$ Billion']
    # Market Capitalization in GBP
    df[table_attributes_final[2]] = (df['Market cap US$ Billion'] * df_exchange['GBP']).round(2)
    # 'Market Capitalization in EUR'
    df[table_attributes_final[3]] = (df['Market cap US$ Billion'] * df_exchange['EUR']).round(2)
    #'Market Capitalization in INR'
    df[table_attributes_final[4]] = ((df['Market cap US$ Billion']) * df_exchange['INR']).round(2)
    print(df)
    return df
def from_csv(input_file):
    df = pd.read_csv(input_file)
    df = df.set_index('Currency').to_dict()['Rate']
    print(df)
    return df

def load_to_csv(df,output_path):
    df.to_csv(output_path, index = False)

def load_to_db(df,sql_connection, table_name):
    df.to_sql(table_name, sql_connection, index = False)

def run_query(query,sql_connection):
    print(query)
    query_data = pd.read_sql_query(query,sql_connection)
    print(query_data)

log_progress("ETL Process Started")
log_progress("Extraction data from website Started")
extracted_df = extract(url)
log_progress("Extraction data from website ended")
log_progress("Extraction data from csv for exchanging data")
df_exchange = from_csv(inputCSVPath)
log_progress("Transformation of data Started")
transform_df = transform(extracted_df, table_attributes_final, df_exchange)
log_progress("Transformation of data ended")
log_progress("Loading data into csv Started.")
load_to_csv(transform_df, outputCSVPath)
log_progress("Loading data into csv successfully.")
log_progress("Loading data into local database started.")
sql_connection = sql.connect(db_name)
load_to_db(transform_df, sql_connection, table_name_bank_largest)
log_progress("Loading data into local database successfully.")
statement1 = f"SELECT * FROM {table_name_bank_largest}"
run_query(statement1, sql_connection)
statement2 = f"SELECT AVG(MC_GBP_Billion) FROM {table_name_bank_largest}"
run_query(statement2, sql_connection)
statement3 = f"SELECT Name from {table_name_bank_largest} LIMIT 5"
run_query(statement3, sql_connection)
sql_connection.close()
log_progress("ETL Process Completed.")
