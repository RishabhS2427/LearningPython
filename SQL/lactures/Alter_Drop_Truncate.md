# ALTER, DROP, and TRUNCATE Tables

Welcome to ALTER, DROP, and TRUNCATE Tables. After watching this video, you will be able to describe the ALTER TABLE, DROP TABLE, and TRUNCATE statements, explain the syntax, use the statements in queries.

---

## ALTER TABLE Statement
You use the ALTER TABLE statements to add or remove columns from table, to modify the data type of columns, to add or remove keys, and to add or remove constraints.

### Syntax
You start with ALTER TABLE followed by the name of the table that you want to alter.

Differently to the create table statement though you do not use parentheses to enclose the parameters for the ALTER TABLE statement.

Each row in the ALTER TABLE statement specifies one change that you want to make to the table.

---

### Add Column
For example, to add a telephone_number column to the author table in the library database to store the author's telephone number, use the following statement.

ALTER TALE author ADD COLUMN telephone_number BIGINT.

In this example, the data type for the column is BIGINT, which can hold a number up to 19 digits long.

---

### Modify Column Data Type
You also use the ALTER TABLE statement to modify the data type of a column.

To do this, use the ALTER COLUMN clause specifying the new datatype for the column.

For example, using a numeric datatype for telephone number means that you cannot include parentheses, plus signs, or dashes as part of the number.

You can change the column to use the CHAR datatype to overcome this.

This code shows how to alter the author table.

ALTER TABLE author ALTER COLUMN telephone_number SET DATA TYPE CHAR(20).

---

### Important Note
Altering the data type of a column containing existing data can cause problems, though, if the existing data is not compatible with the new data type.

For example, changing a column from the CHAR character type to a numeric datatype will not work if the column already contains nonnumeric data.

If you try to do this, you will see an error message in the notification log and the statement will not run.

---

### Drop Column
If your spec changes and you no longer need this extra column, you can again use the ALTER TABLE statement, this time with the DROP COLUMN clause to remove the column as shown.

ALTER TABLE author DROP COLUMN telephone_number.

---

## DROP TABLE Statement
Similar to using DROP COLUMN to delete a column from a table, you use the DROP TABLE statement to delete a table from a database.

When you delete a table that holds data, the data will be automatically removed along with the table by default.

### Syntax
DROP TABLE table_name.

So you use this statement DROP TABLE author to remove the table from the database.

---

## TRUNCATE TABLE Statement
Sometimes you might want to just delete the data in a table rather than deleting the table itself.

While you can use the DELETE statement without a WHERE clause to do this, it is generally quicker and more efficient to truncate the table.

Instead, you use the TRUNCATE TABLE statement to delete all of the rows in a table.

### Syntax
TRUNCATE TABLE table_name IMMEDIATE.

IMMEDIATE indicates an immediate processing of the statement and emphasizes that the action cannot be reversed.

So, to truncate the author table, you use this statement TRUNCATE TABLE author IMMEDIATE.

---

## Summary
In this video, you learn that:

- The ALTER TABLE statement changes the structure of an existing table for example, to add, modify, or drop columns.  
- The DROP TABLE statement deletes an existing table.  
- The TRUNCATE TABLE statement deletes all rows of data in a table.  