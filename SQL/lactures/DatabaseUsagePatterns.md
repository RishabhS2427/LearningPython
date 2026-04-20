# Database Usage Patterns

Welcome to Database Usage Patterns. After watching this video, you will be able to identify the major categories of database users and their use cases for accessing the database. Explain the interfaces and tools used by different types of database users.

---

## Introduction
Different job roles use different tools to access databases. Three primary classes of database users include data engineers and database administrators, data scientists and business analysts, application developers.

---

## Data Engineers and Database Administrators (DBAs)
The first key users of databases include data engineers and database administrators DBAs. Their main activities involve engaging with databases for administrative purposes, which include the establishment and supervision of database objects. Implementation of access controls, and the monitoring and enhancement of performance.

Their primary focus is on creating a solid foundation for storing and managing data efficiently.

---

### Tools and Mechanisms Used

Data engineers and database administrators employ the following mechanisms for performing their tasks:

- Graphical user interfaces (GUIs) or web-based management tools  
- Command-line interfaces and utilities  
- Application programming interfaces (APIs)  

---

### Graphical User Interfaces (GUIs)
GUIs or web-based management tools serve as common means for interacting with databases. Databases typically offer graphical tools, web-based interfaces, particularly for cloud databases and mobile applications.

If vendor-provided tools lack sufficient functionality or user friendliness, users may turn to third-party or specialized alternatives.

For example, Oracle SQL Developer is a graphical tool provided by Oracle for database management.

---

### Command-Line Interfaces
Command-line interfaces and utilities continue to play a crucial role despite the prevalence of GUI tools. Proficiency in command-line usage remains valuable for certain tasks.

While using these tools, users can issue database commands directly or utilize interactive shells for efficient command line interactions.

#### Examples
- Command-line interfaces may involve issuing straightforward database commands directly from the terminal, such as, db2 create database sample mysqldump sakila > sakila.sql.  
- Alternatively, interactive command-line shells like sqlplus for Oracle or db2 clp can be utilized as demonstrated by db2, db2 > connect to sample.  

Furthermore, SQL scripts and batch files executed from the shell provide additional means of interacting with databases.

---

### APIs
Databases often incorporate programmatic interfaces or APIs designed for administrative tasks accessible from applications and tools created by data engineers or third parties.

Users commonly employ APIs in situations requiring automated or programmatic access for tasks like creating and managing database objects, setting access controls, and monitoring performance.

---

## Data Scientists and Business Analysts
Other key users include data scientists and business analysts. These users engage with databases for data analysis, insight derivation, and data-driven predictions.

Their typical data access patterns involve reading from existing data sources, occasionally necessitating the creation and population of database objects, especially in their sandbox environments.

---

### Tools Used in Data Science and BI
Frequently employed tools for tasks in data science and machine learning encompass Jupyter, R Studio, Zepplin, SAS, and SPSS.

Reporting, dashboarding and business intelligence tasks utilize tools such as Microsoft Excel, Microsoft PowerBI, Microsoft Tableau, and Microstrategy.

Both data science and business intelligence tools interact with relational databases through SQL interfaces and APIs, often abstracting away the direct use of SQL.

Additionally, users may opt for SQL query tools for ad-hoc querying, commonly provided by databases, or available as third-party solutions compatible with various database systems.

---

## Application Developers
The last users we will discuss are application developers. They seldom access databases directly. They create applications that can require both read and write access to databases.

Developers use programming languages such as C++, C#, Java, JavaScript, .NET, PHP, Perl, Python, and Ruby to write applications.

---

### Database Interaction
The programming languages communicate with the database through SQL interfaces and APIs like ODBC and JDBC. Some databases, especially cloud-based ones, also include REST APIs for accessing data.

Although programming applications using these lower-level APIs is feasible, it is worth noting that this was the conventional approach for developing applications in the past.

---

### ORM Frameworks
Nowadays, most programmers opt for object relational mapping (ORM) frameworks when working with databases.

ORM frameworks are tools in software development that facilitate the interaction between a relational database and an object-oriented programming language. They are user friendly and can conceal the intricacies of the underlying relational database and SQL.

#### Examples of ORM Frameworks
- ActiveRecord in Ruby applications  
- Django in Python  
- Entity Framework in .Net  
- Hibernate in Java  
- Sequelize in JavaScript  

---

## Summary
In this video, you learned that databases cater to various user roles, including data engineers and DBAs, data scientists and analysts, application developers.

- Data engineers. DBAs manage databases using GUIs, command-line interfaces, and APIs for administrative tasks.  
- Data scientists analysts leverage tools like Jupyter, R Studio, and SQL interfaces for analysis, while BI tools like PowerBI, and Tableau abstract SQL interactions.  
- Application developers use programming languages and ORM frameworks for application development.  