# Distributed Architecture and Clustered Databases

Welcome to Distributed Architecture and Clustered Databases. After watching this video, you will be able to describe common types of database architecture along with their benefits, describe some techniques for managing data and optimizing performance.

---

## Introduction
In our exploration of database architectures, we've primarily focused on single-server configurations. However, for critical or large-scale workloads where high availability or scalability is important, relational database management systems, RDBMSs, offer distributed architectures.

These distributed database architectures involve clusters of machines interconnected through a network, distributing data processing and storage tasks. The approach brings about notable benefits including enhanced scalability, fault tolerance, and overall performance improvements.

---

## Types of Database Architecture
The common types of database architecture include shared disk architecture, shared nothing architecture, and combination and specialized architectures.

---

### Shared Disk Architecture
Shared disk architecture involves multiple database servers processing workloads in parallel. Each server establishes a connection to shared storage and communications with other servers using high-speed interconnection.

The shared disk architecture also facilitates the effective distribution of workloads, ensuring scalability as the demand for processing power grows.

In the event of a server failure, a mechanism is in place to reroute clients seamlessly to other servers, maintaining high availability and minimizing service disruptions.

---

### Shared Nothing Architecture
Let's now learn about shared nothing architecture which utilizes either replication or partitioning techniques.

The approach allows for the effective distribution of client workloads across multiple nodes, promoting parallel processing and efficient resource utilization.

One of the key advantages lies in enhanced fault tolerance achieved by rerouting clients to alternative nodes in the event of a server failure.

---

### Combination and Specialized Architectures
Certain distributed database architectures employ a combination of shared disk, shared nothing, replication or partitioning techniques.

Additionally, they integrate specialized hardware components to achieve specific goals related to availability and scalability.

---

## Techniques for Managing Data and Optimizing Performance
Now that you know different types of database architectures, let's explore some techniques for managing data and optimizing performance.

Some of the common techniques include database replication, database partitioning and sharding.

---

### Database Replication
Database replication is a technique that involves copying changes from one database server to one or more replicas.

This process distributes the client workload across servers, leading to improved performance.

When the replica resides in the same location, we call it a high availability, HA, replica.

If the primary database server experiences a failure due to software or hardware issues, the system redirects clients to HA replica.

To mitigate broader disasters, organizations establish replicas in geographically distributed locations.

This guarantees that during instances of complete data center outages, be it due to power loss, fire, earthquake or flood, clients can be rerouted to disaster recovery replicas.

---

### Database Partitioning and Sharding
An alternative strategy involves partitioning tables with substantial data into logical segments, each containing a subset of the overall data, e.g., sales records for different quarters.

This technique, known as sharding, places these partitions on separate nodes in a cluster.

Each shard possesses its compute resources, processing, memory, and storage to operate on its specific subset of data.

When a client issues a query, it is processed in parallel across multiple nodes or shards, and the results from different nodes are synthesized and returned to the client.

As data or query workloads increase, additional shards and nodes can be seamlessly added to the database cluster, facilitating increased parallel processing and improved overall performance.

Database partitioning and sharding are particularly prevalent in handling data warehousing and business intelligence workloads that involve extensive volumes of data.

---

## Summary
In this video, you learned that RDBMSs offer distributed architectures for critical or large-scale workloads.

- Shared disk allows parallel processing with mechanisms for high availability during server failures.  
- Shared nothing employs replication or partitioning for optimized performance.  
- Database replication involves copying changes from one database server to one or more replicas.  
- Sharding involves placing partitions on separate nodes, facilitating increased parallel processing and improved overall performance.  