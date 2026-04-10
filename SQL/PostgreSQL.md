# PostgreSQL

Welcome to PostgreSQL. After watching this video, you will be able to describe PostgreSQL, explain how you can work with PostgreSQL, and describe replication functionality in PostgreSqL.

---

## Introduction and History
PostgreSQL originates from the POSTGRES project at the University of California more than 30 years ago.

POSTGRES was used for many research and production applications across a range of industries, including financial services, aviation, and medicine.

In 1994, the open source Postgres95 was released, which included an SQL language interpreter. This was soon renamed PostgreSQL, and is today generally pronounced as simply Postgres.

---

## Usage and Extensions
You can use it as part of the LAPP, Linux, Apache, PostgreSQL, and PHP stack for web applications and websites.

And you can also use independently developed extensions for additional functionality such as PostGIS for geographic and spatial data handling.

---

## Definition
PostgreSQL is a free open source object-relational database management system.

The open source part means that you can use, modify, and distribute the Postgres source code to meet your business requirements.

The object part describes that like object-oriented programming languages, it supports inheritance and overloading. You can use these techniques to simplify your design and reuse database objects.

---

## Compatibility and Features
Postgres is compatible with most of today's commonly used operating systems, and its low maintenance threshold make it easy to implement in an organization.

It supports many programming languages, enabling you to integrate it with your web applications, and supports ANSI-SQL standards.

---

## Database Capabilities
When using Postgres, you can use all the standard relational database constructs such as keys, transactions, views, functions, and stored procedures.

And you can also use some of the NoSQL functionality such as JSON for structured data and HSTORE for non-hierarchical data.

---

## Replication

### Two Node Synchronous Replication
Postgres supports replication for high availability.

It supports two node synchronous replication. This stores a copy of your data on a second server and applies each change you make to Node 1 at Node 2.

You can then share read loads across the two servers.

And if Node 1 fails, you can enable Node 2 to service all clients until Node 1 is running again.

---

### Multi-Node Asynchronous Replication
It also supports multi-node asynchronous replication for high availability and scalability.

Here, one master node distributes its changes to multiple read-only replicas for scalability purposes.

And again, if the read-write node fails, you can quickly replace it with one of the read-only replicas.

---

### Multi-Master Replication
For even greater flexibility for scaling applications, you can use commercial additions such as EDB PostgreSQL replication server, which provide multi-master read/write replication.

This enables you to run multiple read/write databases that all replicate changes with each other.

If one fails, users can easily be redirected to another instance until it is available again.

---

## Scalability Techniques

### Partitioning
Other technologies that have been added to PostgreSQL in recent releases to enhance scalability and working with larger data sets include partitioning, which enables you to split a large table into multiple smaller sections or partitions to improve query performance.

### Sharding
And sharding, which enables you to store horizontal partitions across multiple remote servers.

---

## Summary
In this video, you learned that PostgreSQL is an open source, object-relational database.

- It supports a range of languages for client application development.  
- It supports relational, structured, and non-structured data.  
- And it supports replication and partitioning for high availability and scalability.  