# Db2

Welcome to Db2, after watching this video, you will be able to describe Db2. Its histories and features list various Db2 products and deployment options. Describe Db2 on cloud and its plans. Explain how you can work with Db2 on cloud, describe Db2 high availability options, and describe Db2 scalability with partitioning.

---

## Introduction to Db2
Database 2, or Db2, was first released by IBM in 1983 and was an early example of a relational database management system.

This first release ran on IBM mainframe computers, but over the years, different versions were developed to run on many other platforms, including OS2, Unix, Linux, and Windows.

After some time, the product was rewritten to use the same codebase across the multiple operating systems so that you can easily port applications accessing Db2 data from one operating system to another.

After many iterations of the offering across many platforms and with enhanced functionality, today, Db2 is a whole suite of database management products.

---

## Db2 Products
Including Db2 database, Db2 warehouse, Db2 on cloud, Db2 warehouse on cloud, Db2 big SQL, and Db2 for z OS.

---

## Evaluation Options
There are many ways to evaluate these products.

- You can use Db2 database community license for free with a 100-gigabyte data limit.  
- You can download a free docker image of Db2 database.  
- You can also use the free lite plan of Db2 on cloud for development and evaluation purposes on IBM Cloud.  
- Db2 Warehouse Enterprise Edition and Db2 Big SQL are available in no-cost trial editions.  
- You can use Db2 warehouse on cloud for free up to 1GB of data.  

---

## Features of Db2
The Db2 products all use AI-powered functionality to simplify the management and querying of your data, both on-premises and in cloud environments.

- You can use machine learning algorithms to improve the efficiency and performance of queries.  
- The column store feature to improve performance and reduce overheads for analytic workloads by directing queries to specific columns rather than processing an entire data table.  
- The data skipping feature to reduce overheads by automatically avoiding processing data that is not required in a particular query.  

The common SQL engine across all the Db2 family means that you can write a query once and be sure it will work with other products in the family. This simplifies migration of applications between products and platforms.

The support for all data types, relational, structured, and unstructured, means you can access all of your corporate data to make better business decisions.

The Db2 replication functionality enables you to implement high availability and disaster recovery solutions.

---

## Scalability
Db2 provides scalability in a number of ways.

- For short peaks, you can extend on-premises storage and power levels onto hosted cloud deployments.  
- You can independently scale power and storage in a managed cloud deployment to only use and pay for extra resources when you need them.  
- In Db2 warehouse, you can use the database partitioning feature to transparently split data across partitions and servers to maximize the compute power available and enable massively parallel processing.  

---

## Db2 Family Overview
The Db2 family provides you with a range of data management products to work with data on-premises or in the cloud.

### Db2 Database
Db2 database is a powerful enterprise-ready on-premises RDBMS optimized for OLTP. It is supported on Linux, Unix, and Windows and provides performance, high availability, scalability, and resilience.

### Db2 Warehouse
Db2 Warehouse is an on-premises data warehouse that provides advanced data analytics, massively parallel processing, and machine learning.

### Db2 on Cloud
Db2 on Cloud is a fully managed cloud-based SQL database which provides similar features to Db2 database performance, high availability, scalability, and resilience.

### Db2 Warehouse on Cloud
Db2 warehouse on Cloud is a fully managed elastic cloud-based data warehouse that provides similar features to the on-premises Db2 warehouse.

You can deploy both of the cloud-based products on IBM Cloud and Amazon Web Services.

### Db2 Big SQL
Db2 Big SQL is an SQL on-Hadoop engine that provides massively parallel processing and advanced query querying functionality.

You can use it to query a range of data sources, including Hadoop HDFS and web HDFS, RDBMS, NoSQL, and other object stores.

You can integrate it with Cloudera data platform or use a service on IBM Cloud Pak for data.

### Db2 for ZOS
Db2 for ZOS, an enterprise data server for IBM Z. It provides a mission-critical data solution with integration for analytics, mobile, and cloud that supports thousands of customers and millions of users.

---

## Cloud Pak for Data
Cloud pack four data is a fully integrated data and AI platform that you can use to work with and manage all of your data.

It runs on Red Hat OpenShift in a container, so you can deploy it on any private, public, or hybrid cloud.

Using Cloud Pak four data, you can:

- Connect to Db2 or any other data source wherever it may be stored.  
- Use the Watson Knowledge catalog to organize your data.  
- Work with a range of analytics services to gain insight on your data.  
- Use Watson and other services to infuse AI into your systems.  

---

## Db2 on Cloud Plans
Db2 on Cloud is a great way to get started with Db2. It offers three plans for lite, standard, and enterprise.

### Lite Plan
The lite plan is free and time unlimited, meaning that you can use it in your projects without worrying about a time-limited trial period coming to an end.

The plan is limited to 200 megabytes of data and 15 simultaneous connections.

### Standard Plan
The standard plan provides flexible scaling of compute capability and storage as well as built-in three-node high availability clustering.

### Enterprise Plan
The enterprise plan provides you with a dedicated database instance. Again, with flexible scaling of compute capability and storage and built-in three-node high availability clustering.

You can deploy Db2 on Cloud on the IBM Cloud platform or on Amazon Web services.

---

## Working with Db2 on Cloud
Once running, you can access your Db2 on cloud databases by using:

- The CLPPlus command line interface  
- The Db2 on cloud GUI console  
- Standard APIs such as ODBC, JDBC, and rest  

You can also easily load data from Excel, CSV, and text files from Amazon S3 object storage using the GUI console, and you can programmatically load data from IBM cloud object storage.

---

## High Availability and Disaster Recovery (HADR)
Db2 provides high availability, disaster recovery, or HADR functionality to support high availability systems.

HADR replicates changes made at a primary database to multiple standby servers.

If the primary database fails for any reason, hardware, software, or network issues, you can automatically promote one of the standby databases to be the primary database.

Redirect client applications to this new primary database, and continue to replicate to the other standby servers in the group.

When the original primary database comes back online, it can either take the place of a standby server or be promoted back to the primary position.

---

## Partitioning and Scaling in Db2 Warehouse
Db2 warehouse offers massively parallel processing and data analytics for BI workloads.

At times, you may need to scale the storage capabilities of your system to meet peak demand or to reduce costs when demand is low.

Data in Db2 warehouse is stored in data nodes.

To scale up your storage capacity, you just need to add a node to your deployment. The partitions and their workloads are then automatically rebalanced across the new node setup.

Similarly, to scale down, you just remove a node to return to your original state.

---

## Summary
In this video, you learned that Db2 is a family of products that you can use to work with and manage your data in whatever way you need.

- You can deploy Db2 across many platforms, both on premises and in the cloud.  
- Cloud Pak for data includes Db2 and many IBM tools for data.  
- Db2 on cloud is a fully managed cloud-based SQL database that can run on IBM Cloud or AWS.  
- Db2 provides high availability, disaster recovery, and scalability functionality.  