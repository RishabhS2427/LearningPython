# MySQL

Welcome to MySQL. After watching this video, you will be able to describe MySQL and its historical background, describe the key attributes of working with MySQL, describe some MySQL storage engines, identify clustering options provided by MySQL.

---

## Introduction to MySQL
MySQL is an object relational database management system that plays a pivotal role in modern web development.

MySQL stands out for its reliability, scalability, and ease of use. With diverse flavors and additions, it caters to different needs, even offering a clustered version designed to handle demanding workloads effectively.

This versatility has contributed to MySQL's widespread adoption as an adaptable database solution across various applications and industries.

---

## History of MySQL
Let us learn about the history of MySQL.

A Swedish company, MySQL AB, initially developed MySQL, naming it after My, the daughter of co-founder Monte Widenius.

Sun Microsystems later acquired MySQL AB, and subsequently Oracle Corporation acquired Sun Microsystems.

The MySQL logo features a dolphin named Sakila, selected from suggestions in a name the dolphin contest.

MySQL gained popularity in the late 1990s and early 2000s because it played a crucial role in the Linux operating system, Apache Web Server, MySQL database, and PHP scripting language, LAMP stack.

The stack was the foundation for building many of the era's popular websites.

---

## Licensing
MySQL has dual licensing, offering the open source GNU GPL and a commercial license for applications and solutions that embed MySQL.

The open source nature of GNU GPL has led to the emergence of various forks, with Maria DB being a prominent example led by some original MySQL developers.

---

## Working with MySQL
Let us now explore aspects of working with SQL.

MySQL is compatible with numerous Unix versions, Microsoft Windows, and Linux.

Writing client applications for MySQL is feasible with a wide range of modern programming languages.

MySQL employs standard SQL syntax and introduces extensions for added functionality.

For example, use of load data statement which swiftly imports rows from a text file into a database table.

MySQL works primarily with relational data, but also supports JSON.

---

## Storage Engines
Like many other relational database management systems, RDBMS, MySQL supports multiple storage engines.

The storage engine is the component that handles the SQL operations on a table and defines what feature that table can use.

You base your choice of engine for a particular table on the expected workload and the table's requirement.

---

### InnoDB Engine
The default MySQL storage engine is InnoDB, which supports transactions to ensure the consistency of your data, row-level locking to improve multi-user performance, clustered indexes on primary keys to increase the performance of regularly executed queries, and foreign key constraints to maintain data integrity.

The engine provides a balance of high performance and reliability.

---

### MyISAM Engine
MySQL also supports the MyISAM engine, which is good for workloads with mainly read operations and few updates, such as data warehouse or web applications.

It uses table-level locking, which inhibits performance in a read-write environment.

---

### NDB Engine
Another commonly used engine is the NDB Engine, which supports multiple instances of MySQL servers running in a cluster.

This is primarily used for applications that require high levels of availability and redundancy.

---

## High Availability and Scalability
MySQL supports high availability and scalability.

You can use replication to create a copy of your data on one or more replicas.

Changes in the source database are then simultaneously executed at the replicas.

Multiple copies of the same data mean that you can share certain read loads for your data across the replica set improving scalability.

Additionally, replication boosts availability. If the source database experiences a failure, you can perform a failover to use one of the replicas instead.

---

## Clustering
Let us now learn about clustering.

Clustering is the practice of connecting multiple independent computing resources to work together as a unified system.

MySQL provides two clustering options; InnoDB Storage engine with group replication, MySQL Cluster Edition with NDB Storage engine.

---

### InnoDB with Group Replication
The first option uses the InnoDB storage engine with group replication and enables you to work with one read-write primary server and multiple secondary servers.

You can then use MySQL router to load balance client applications across the multiple server instances.

In the event of unplanned downtime of any of the servers, MySQL router will reconnect client applications to an available server.

---

### MySQL Cluster Edition (NDB)
Alternatively, the MySQL cluster edition uses the NDB storage engine to provide a highly available and scalable solution.

Multiple MySQL server nodes access a set of data nodes usually stored in memory.

Running multiple data nodes provides redundancy and hence increased availability in the event of failure, and running multiple server nodes provides scalability.

---

## Summary
In this video, you learned that MySQL is a reliable, scalable, and widely adopted database system.

- MySQL is compatible with UNIX, Windows, and Linux, supporting various programming languages.  
- MySQL has dual licensing, offering GNU GPL for open source and a commercial license for embedded applications.  
- MySQL works with relational and JSON data supporting multiple storage engines.  
- MySQL provides two clustering options, InnoDB with group replication, and MySQL Cluster Edition with NDB storage engine.  