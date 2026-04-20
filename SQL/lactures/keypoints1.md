## Key points

* DDL (Data Definition Language) statements, such as CREATE, ALTER, and DROP, are used for defining, modifying, and deleting objects in a database, like tables and their attributes.

* When creating tables, key considerations involve selecting a schema, defining columns with names, datatypes, and optional values like primary key constraints, and referencing an Entity Relationship Diagram (ERD).

* Methods for creating tables include using visual interfaces like the Db2 on Cloud console, SQL statements, and administrative APIs.

* Post-creation actions may include generating SQL code, modifying table structure, exploring dependencies, and dropping the table if necessary.

* Data manipulation involves DML (Data Manipulation Language) statements for working with data within tables, such as inserting, updating, deleting, or querying records.

* Data movement tasks include populating databases initially, adding or appending data, making copies for development tests or disaster recovery, and ensuring scalability.

* Utilities like BACKUP and RESTORE are used to create and recover copies of entire databases, including tables, views, constraints, and their data.

* The IMPORT utility facilitates inserting data into tables from different formats like DEL/CSV, ASC, and IXF, while the EXPORT utility saves table data into various formats like CSV.

* LOAD utilities enable high-performance insertion of large volumes of data into specified tables, offering quicker and more efficient data loading compared to multiple INSERT statements.

* Loading data can be done from various sources, including delimited text files and Cloud Object Storage, and can be managed through user-friendly interfaces like the Load Data utility in the Db2 Web Console.MySQL, renowned for its scalability and reliability, is an open-source RDBMS available in various forms, including a
  free community edition, commercial version, and cloud deployment.

* Key administration tools for MySQL management include MySQL CLI, MySQL Workbench, and phpMyAdmin.

* MySQL CLI enables interaction with the MySQL server and data via commands, while MySQL Workbench integrates SQL
  development, administration, and design tasks.

* phpMyAdmin, a web-based GUI, is popular among web hosting providers and individual website owners for MySQL
  management.

* Database and table creation in MySQL can be accomplished through command line interfaces, graphical user interfaces,
  or API calls.

* phpMyAdmin offers an intuitive interface for creating databases, tables, and columns, allowing for easy addition and
  modification of post-table creation.

* Backup and restore functionality, available both via command line and phpMyAdmin, facilitates database population.

* For small data inserts, phpMyAdmin provides a convenient manual insertion method.

* Import and export functionalities, accessible through the command line and phpMyAdmin, aid in table population and
  data saving to files.

* Primary keys in MySQL are established by defining a primary index on one or more columns, and autoincrement can be
  used to generate sequential numeric data in a column.

* When creating foreign keys, actions like ON DELETE and ON UPDATE can be defined.

* By default, columns in MySQL tables within phpMyAdmin are set to NOT NULL.

* Columns can be configured to accept only unique values in MySQL setups.