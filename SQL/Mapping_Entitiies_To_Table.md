# Mapping Entities to Tables

Welcome to Mapping Entities to Tables. After watching this video, you will be able to define entity relationship diagram ERD, and relational database. Identify the key components of ERD, outline the steps involved in mapping entities to tables, describe the best practices for relational database design.

---

## ERD Definition
An ERD is a graphical representation of the entities and the relationships between them in a database. It is a modeling technique used in database design to represent the structure of a database system visually.

---

## Primary Components of ERD
The primary components of an ER diagram include entities, attributes, and relationships.

---

### Entities
Entities represent real world objects, concepts or things that store and manage data. Rectangles in an ER diagram depict these entities. In this example, book represents an entity.

---

### Attributes
Attributes represent the characteristics associated with an entity. Ovals inside the entity rectangle depict these attributes. In the given example, ISBN, title, author, and published year are all attributes.

---

### Relationships
Relationships illustrate how entities interrelate. Let's introduce another entity in the example, say author. A relationship could be that an author writes a book represented by a line connecting the author and book rectangles in the ER diagram.

---

## Relational Database
The relational database model provides a well defined framework for managing and manipulating structured data. In a relational database you organize data elements in a table. Relationships between the tables depend on common fields.

---

## Mapping ERD to Tables
To design a relational database, begin with an ERD and then map the ERD to the tables in a database.

---

### Step 1: Convert Entity to Table
The illustration utilizes an ERD for the book entity as an example. The entity book becomes a table with the same name book. This step provides the structure for the rows and columns. However, the table is still empty. It doesn't contain actual data.

---

### Step 2: Convert Attributes to Columns
The next step involves translating attributes into the table. When translated to a table, the attributes of an entity become columns in that table. For example, if book had attributes, ISBN, title, and author, these become columns in the book table.

---

### Step 3: Add Data Values
The final step is to add data values to the table's columns. You can add the relevant data as shown in the table. The step completes transforming a conceptual entity into a tangible table with specific data.

---

### Applying Steps to Other Entities
You will follow similar steps for other entities. For example, transform the entity author into the table and translate the attributes into columns. Adding data values into the columns completes the table.

---

## Best Practices for Relational Database Design
The best practices involve primary key designation, data validation, default values, using views, concurrency control.

---

### Primary Key Designation
A primary key is an exclusive identifier allocated to each entry in a table. Designate a primary key for the book table, such as book ID, to identify each book in the database uniquely.

---

### Data Validation
Data validation, implement data validation mechanisms to ensure the accuracy and consistency of the data entered into the database. The step may involve checks for data, types, ranges, and formats. For example, ensure that the published year attribute for the book entity only accepts numerical values within a specified range.

---

### Default Values
Default values. Consider assigning default values to certain columns to streamline data entry and enhance the records. For example, set a default value of "Unknown" for the author column in the book table to handle cases where the author's information is not available.

---

### Use of Views
Use of views, utilize views to present a customized and simplified data perspective, especially for complex queries or reporting purposes. For example, create a view that combines information from the book and author tables to present a comprehensive list of books and their authors without showing the underlying complexity.

---

### Concurrency Control
Concurrency control, implement concurrency control mechanisms to manage multiple users access and modifications to the database concurrently. This step helps prevent data inconsistency and conflicts. For example, include a "Last modified" timestamp in the book table.

---

## Summary
In this video, you learned that an ERD is a graphical representation of the entities and the relationships between them in a database. ERD components include entities, attributes, and relationships. Relational databases organize data into tables with relationships based on common fields. Entities become tables with the same name and attributes become columns within those tables. Adhering to best practices in relational database design is crucial for ensuring the efficiency and maintainability of the database system.