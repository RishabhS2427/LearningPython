# Data Movement Utilities

Welcome to data movement utilities. After watching this video, you will be able to identify reasons for moving data in and out of databases. Compare methods for data movement, including backup, restore, import, and export. Identify various file formats for importing and exporting data, evaluating their suitability. Recognize the efficiency of data movement operations using different database utilities.

---

## Introduction
Data engineers and database administrators often need to move data into and out of an existing database.

---

## Reasons for Data Movement
There are multiple reasons for this action. These include:

- populating the database and its objects like tables  
- creating a duplicate database for development and testing needs  
- creating a snapshot of the state of the database for disaster recovery  
- generating a new table using data from external sources or files  
- adding data into one or more existing tables  

---

## Methods for Data Movement
Most databases support different ways to move data in and out of the database using multiple file formats.

Each database has its tools and utilities for data movement, but for this lesson we will classify them into three categories:

- backup and restore  
- import and export  
- load  

---

## Backup and Restore

One method for moving data between databases is to perform backup and restore.

- The backup operation creates a file or a set of files that encapsulates all the database objects and their data.  
- The restore operation creates an exact copy of the original database from the backup files.  

### What Backup Preserves
Backup and restore operations preserve all objects in the database, including:

- schemas  
- tables  
- views  
- user defined data types  
- functions  
- stored procedures  
- table constraints  
- triggers  
- security settings  
- relationships between objects  
- the data in all the tables  

### Usage
- Backups are essential to preserve copies of the production database for disaster recovery purposes.  
- You can also perform backup and restore operations to create additional database copies for development and test purposes.  

---

## Import and Export

- The important operation reads data from a file and performs a series of insert statements against the target table.  
- The export operation retrieves data from the designated table and stores it in a chosen file.  

### Interfaces for Import and Export
Users can perform import and export operations using multiple interfaces:

- command line utility  
- management APIs  
- graphical or web administration tools  
- third-party tools  

---

## File Formats

Most databases support multiple file formats for importing and exporting data.

### DEL
- delimited ASCII allows data exchange among various database and file managers  
- utilizing special character delimiters to separate column values  
- comma separated variable files being a well-known example  

### ASC
- nondelimited ASCII imports data from applications generating flat text files  
- with aligned columns  

### PC/IXF
- the PC version of the integration exchange format IXF  
- represents the preferred method for data exchange within the database manager  
- presents a structured description of a database table  
- containing an external representation of the internal table  

### JSON
- with the popularity of JSON and rest web services  
- some databases and third-party tools support importing and exporting data to and from JSON files  

---

## Examples of Import and Export

### DB2 Command Line
- the command line import and export utilities allows you to type the file names, formats, table names, and message files  
- the export utility in DB2 allows you to specify an SQL query and export a subset of the data  

### DB2 Cloud Console
- includes a visual interface that allows you to export the results of any table or query  
- save it as a CSV file  

#### Steps
- select the table  
- click view data  
- select the export button  
- click export to CSV  
- specify a name and location  

---

## Load Utility

As an alternative to the import utility, some databases provide load utilities.

- The load utility outperforms the import utility by directly formatting pages into the database  
- rather than running SQL insert statements  

### Characteristics
- does not perform referential or table constraint checking  
- may bypass database logging  
- helps with higher performance  

### Usage
- import may work well for smaller tables  
- load utilities are preferred for large volumes of data  

### Activation
- from the command line  
- through API in an application  
- using visual database management tools  

---

## Summary
In this video, you learned that:

- data movement is essential for the initial population of databases and tables  
- backup and restore utilities actively create and recover copies of entire databases  
- the import utility facilitates data insertion into a specific table from various formats  
- the export utility allows preserving data from a specific table in various formats like CSV  
- load utilities provide high performance data insertion into specified tables  