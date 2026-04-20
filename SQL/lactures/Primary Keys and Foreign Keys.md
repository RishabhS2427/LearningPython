# Primary Keys and Foreign Keys

Welcome to Primary Keys and Foreign Keys. After watching this video, you will be able to, describe primary and foreign keys, outline the steps to create primary and foreign keys.

---

## Primary Key

You can use the primary key to uniquely identify every row in a table.

In some tables, the choice of the primary key is easy because it is a naturally occurring unique attribute of an entity.

For example, the book_id of a book or the employee_id number of a staff member.

If your table doesn't have an existing unique attribute, you can add a column to the table to serve as the primary key.

Or if a combination of the two attributes uniquely identifies each row, you can create a primary key across the two columns.

For example, where employees have a unique identifier within their work site, you can use the combination of their site_id and employee_id.

Note that each table can only have one primary key.

---

## Creating Primary Key

You can create a primary key when you create the table by using the PRIMARY KEY clause and the CREATE TABLE statement.

In the parentheses for the PRIMARY KEY clause, state the name of the column or columns that will be the primary key.

Alternatively, you can create a primary key on the existing table by using the ADD PRIMARY KEY clause of the ALTER TABLE statement.

Again, in the parentheses state the name of the column or columns, that will be the primary key.

---

## Relationship using Keys

You use primary and foreign keys to define the relationships between your tables.

---

## Foreign Key

A foreign key is a table column that holds information identical to the primary key in another table.

For example, the copy table might list all books that the library owns.

Therefore, the book_id of a copy of an individual book must exist in the book table as a valid book.

When the library owns multiple copies of a popular book, the book_id of that particular book will appear multiple times in the copy table.

You can also specify that whenever you add a row to the copy table, the book_id you use must already exist in the book table.

---

## Creating Foreign Key

Similar to primary keys, you can create a foreign key when you create the table by using the CONSTRAINT name FOREIGN KEY clause of the create table statement.

In the parentheses for the FOREIGN KEY clause state the name of the column or columns that will be the foreign key and then reference the table and primary key column that the foreign key links to.

---

## Rule Clause

You can also use the rule clause to define what action to take if a row in the parent table, the table with the primary key, is updated or deleted.

For updates and deletes, you can specify to take no action, in which case the update or delete option on the parent table may fail.

For deletions, you can also specify to cascade the delete, that is to delete the related child row in the dependent table or to set the values in the foreign key column of the child table to null.

---

## Additional Note

Alternatively, you can create a primary key on an existing table by using the ADD PRIMARY KEY clause of the alter table statement.

Again, in the parentheses state the name of the column or columns, that will be the primary key.

Note to use a comma to separate the column names when using multiple columns for a primary key.

---

## Summary

In this video, you learned that you can use primary keys to enforce the uniqueness of rows in a table.

Foreign keys are columns in a table which contain the same information as the primary key in another table.

You can use primary and foreign keys to create relationships between tables.

<video width="340" height="240" controls>
  <source src="[PrimaryKeysandForeignKeys.mp4](videos/PrimaryKeysandForeignKeys.mp4)" type="video/mp4">
</video>
