# In this lab you'll learn
# how to:
# 1. Create a database using Python
# 2. Load the data from a CSV file as a table to the database
# 3. Run basic "queries" on the database to access the information.

import pandas as pd
import  sqlite3
conn = sqlite3.connect('./output/STAFF.db')
table_name = 'INSTRACTOR'
attribute_list = ['ID', 'FNAME', 'LNAME','CITY','CCODE']
file_path = "./input/INSTRUCTOR.csv"
file_path_2 = "./input/Departments.csv"
df = pd.read_csv(file_path, names = attribute_list)
df.to_sql(table_name , conn, if_exists = 'replace', index = False)
print('Table is ready')
query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)
query_statement = f"SELECT FNAME FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)
print(query_output.to_json(orient='records'))

query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

data_dict = {
 'ID' : [2000],
    'FNAME' : ['Rishabh'],
    'LNAME' : ['Shrivastava'],
    'CITY' : ['JABALPUR'],
    'CCODE' : ['JB']
}
data_appand = pd.DataFrame(data_dict)
data_appand.to_sql(table_name,conn, if_exists = 'append', index = False)
print("Data appended Successfully")


table_name_2 = 'Departments'
attribute_list_2 = ['DEPT_ID', 'DEP_NAME', 'MANAGER_ID', 'LOC_ID']

df2 = pd.read_csv(file_path_2, names = attribute_list_2) # convert csv into dataframe
df2.to_sql(table_name_2,conn , if_exists='replace', index=True) # convert dataframe into SQL
print("Dept table is ready")

data_dict_2 = {
    'DEPT_ID' : [9],
    'DEP_NAME' : 'Quality Assurance',
    'MANAGER_ID' : [30010],
    'LOC_ID' : 'L0010',
}
data_append_2 = pd.DataFrame(data_dict_2)

data_append_2.to_sql(table_name_2, conn, if_exists = 'append', index = False)
print("Data appended Successfully")

statement_1 = f"SELECT * FROM {table_name_2}"
query_output = pd.read_sql(statement_1, conn)
print(statement_1)
print(query_output)

statement_2 = f"SELECT count(*) FROM {table_name_2}"
query_output = pd.read_sql(statement_2, conn)
print(statement_2)
print(query_output)


conn.close()