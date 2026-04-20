# Creating Databases and Loading Data into PostgreSQL

Welcome to creating databases and loading data into PostgreSQL. After watching this video, you will be able to identify the steps involved in creating databases and tables on the command line and using pgAdmin. Describe the steps for backing up and restoring databases. Describe how to import and export data from tables.

---

## Introduction
As with many RDBMSs, you can create databases and tables and load data into PostgreSQL using a command-line interface, a graphical user interface, or API calls.

In this video, you will see how to perform these tasks using the PSQL command-line interface and the pgAdmin user interface.

You will see how to create the database, then the table, and how to define and edit the columns in that table.

Next, you will see how to load data into your database.

---

## Using PSQL Command-Line Interface

You can use PSQL to issue commands to create and interact with database objects and data.

### Creating Database and Table
- Use the Create Database command to create the database  
- Use Create Table for tables by specifying column names and data types  

### View Table Structure
- You can use the \d command to show the structure of the newly created table  

---

## Loading Data using PSQL

After creating the database, it is likely that you will want to load data into it.

- On the command line, you can use PSQL to restore a database that was previously backed up using pg_dump  
- Specify the target database name and the name of the dump file  

This command will recreate the tables, any other database objects, and the data present at the time of the creation of the dump file.

---

## Using pgAdmin

Alternatively, you can use pgAdmin to create the same database.

pgAdmin is a web-based visual tool that you can use to work with PostgreSQL.

---

### Create Database in pgAdmin
- Navigate to the tree view in the left panel  
- Right-click on Databases  
- Click Create  
- Click Database  
- Enter the name of the new database  
- Click Save  

---

### Restore Database in pgAdmin
- Select the database you want to restore to in the tree view  
- Click Restore  
- Enter the location of your dump file in the restore box  

This step executes the SQL statements contained in that file to recreate the database objects and data in the current database.

---

### Create Table in pgAdmin
- In the tree view, right-click on Tables  
- Select Create  
- Click Table  
- On the general page, enter the name of your table, in this case, Employee_details  
- Navigate to the columns tab  
- Enter the details of your columns  
- Continue saving  

Next, you will see your table and columns in the tables section of the tree view panel.

---

## Import Data using pgAdmin

From here, you can use the Import/Export function to load data into your new table.

- In the Import/Export data box, choose to import  
- Specify the location and name of the data file  

If you are loading data from a CSV file, it is not necessary to specify the delimiter, as it is the default option for CSV files.

---

### View and Edit Data
- You can use the view and edit data option to review the loaded data  

This executes an SQL query to display the data in the selected table.

---

## Export Data using pgAdmin

- Utilize the Import/Export function to export the current data in your database to a CSV file for external use  

CSV is the default format, allowing you to simply specify the file name and click OK.

---

## Backup using pg_dump

If you want to back up the entire database, you can use the pg_dump utility.

- Specify the database name and the name of the dump file  

By default, pg_dump creates an SQL file containing a script that describes all objects and data in the database.

- You can customize the command to send to a compressed file  
- By default, pg_dump backs up the entire schema and the data in the database  

---

## Summary
In this video, you learned that:

- you can use various tools to create PostgreSQL objects, including the PSQL command-line utility and pgAdmin  
- you can use pg_dump to back up databases and PSQL to restore them  
- you can use the pgAdmin Import/Export tool to load data and export data from tables  