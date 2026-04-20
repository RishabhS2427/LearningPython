# Creating Tables

Welcome to creating tables. After watching this video, you will be able to, identify key considerations for creating tables, outline the steps to create a table in Db2 on Cloud, describe the process of modifying a table structure after its creation.

---

## Introduction
Creating a table in a relational database requires careful consideration and information gathering.

---

## Key Considerations for Creating Tables
Here are a few key considerations.

- Firstly, choose the location for table creation. Considering the presence of schemas in many relational databases, schemas offer a means to organize database objects logically.  
- Next, collect all necessary details for table creation, including a name for the table and names and data types for each column.  
- You should also consider whether a column can contain duplicate values or if a column will allow null values.  
- Utilize the Entity Relationship Diagram, ERD, created during database design as a helpful reference.  
- Lastly, confirm that you have a complete set of information needed for table creation to avoid issues later in the process.  

---

## Methods for Creating Tables
There are several methods for creating tables in a relational database.

### Common Methods
- Using visual interface or UI tools  
- Using SQL statements  
- Using APIs  

---

### Visual Interface (UI Tools)
Many relational databases provide a visual interface or UI tools that allow users to create and modify tables using a graphical representation.

It is often suitable for small scale or occasional tasks and is user-friendly for those not familiar with SQL.

A few examples include Db2 on Cloud console, MySQL phpMyAdmin, and PostgreSQL PGAdmin.

---

### SQL Statements
Another common method involves using SQL statements, specifically the CREATE TABLE statement.

Include the statement in a script file to help you automate the creation process when you are creating multiple tables.

---

### APIs
Some databases also provide administrative application programming interfaces, APIs, that allow for programmatic creation and management of tables.

These APIs help interact with the database at a higher level, providing more control and automation options, for example, MongoDB with pymongo (Python Driver).

---

## Db2 on Cloud Table Creation
The Db2 on Cloud console is the user interface provided by IBM to interact with and manage Db2 databases in the Cloud.

Creating a table using the Db2 on the Cloud console involves a step by step process.

### Key Steps
- Choosing a schema  
- Creating a new table  
- Configuring table columns and data types  

---

### Step 1: Choose Schema
The first step is to select a schema to hold the table. The default schema in Db2 is often the username.

In the provided example, the username is schema name. Each user will have a unique username in their Db2 database.

You can create new schemas to hold your tables, views, and other database objects.

---

### Step 2: Create Table
After choosing the schema, proceed to create a new table.

Provide a name for the table, for instance, the example names it employee details.

The fully qualified name for this table considering the selected schema, schema name, would be schema name.employee details.

---

### Step 3: Configure Columns
By default, the new table has a single column. You can rename this column to suit your needs.

Set the data type for the column by choosing from the available options.

Use the add column option to continue adding columns until you define the entire table structure.

Specify data types, decide on null value acceptance, and provide length and scale as needed.

Lastly, click the create button to finalize the table creation.

---

## Modifying Table Structure
You can also alter a table structure after its creation, which involves modifying the existing table.

### Post-Creation Actions
- You can drop or delete the table.  
- You can also generate SQL code to perform actions such as select, insert, update, and delete.  
- Next, you can modify the table by adding new columns, setting constraints, or altering its structure.  
- Lastly, you can explore the database objects that the table relies on.  

---

## Summary
In this video, you learn that, in creating tables, key considerations involve choosing the location, collecting details, and referencing the ERD.

- Methods for creating tables include using visual interfaces, SQL statements, and administrative APIs.  
- The Db2 on Cloud console is an example of a visual interface for managing Db2 databases.  
- Steps for creating a table in Db2 include selecting a schema, creating the table, and configuring columns.  
- Post-creation actions include dropping the table, generating SQL code, modifying the structure, and exploring dependencies.  