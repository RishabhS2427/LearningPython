# Database Architecture

Welcome to Database Architecture. After watching this video, you will be able to; describe some common deployment topologies, recognize the advantages of deploying databases in Cloud.

---

## Deployment Topology Definition
The deployment topology is the arrangement or configuration of the hardware, software, and network components in a system or application deployment. The choice of deployment topology depends on factors such as scalability, performance, reliability, and the nature of the application.

---

## Common Deployment Topologies
Here are some common deployment topologies.

- Single-tier architecture  
- Client-server architecture, or two-tier database architecture  
- Three-tier architecture  
- Cloud-based deployment  

---

## Single-Tier Architecture
A single-tier architecture deploys all components of an application, including the user interface, application logic, and data storage on a single server or machine. In this configuration, the application's entire stack operates within the same environment.

---

## Client-Server Architecture (Two-Tier Architecture)
Let's now discuss client-server architecture, also referred to as a two-tier architecture. The architecture represents a deployment topology that divides the application into two distinct layers.

- A client layer, responsible for the user interface  
- A server layer, managing the application logic and data storage  

In this scenario, a remote server hosts the database and users usually access it from client systems, commonly through a web page or local application.

In two-tier database set up, the database server and application function are in distinct tiers. The client tier application establishes a connection to the database server through a database interface such as an API or framework.

Depending on the programming language used to write the application, this interface communicates with the database server through a database client or API installed on the client system.

---

## Database Server Layers
The server's database management system software, DBMS, comprises several layers, broadly categorized as:

- Data access layer  
- Database engine layer  
- Database storage layer  

Communication between the database interface and server occurs through a database client or API installed on the client system.

The data access layer server provides interfaces for various client types encompassing standard APIs like JDBC and ODBC, command line processor, CLP interfaces, and vendor-specific or proprietary interfaces.

Additionally, the database server incorporates an engine responsible for compiling queries, retrieving and processing data, and delivering the result set.

---

## Three-Tier Architecture
In scenarios involving multiple users, the introduction of a middle tier or application server layer often occurs between the application client and the remote database server, forming a three-tier architecture commonly deployed in production environments.

Most production environments usually restrict access to database servers, except administrators.

### Reasons for Restricted Access
- A primary concern is security. Database servers contain sensitive data. Limiting access to authorized personnel is important to protect against unauthorized data access or modification.  
- The next concern is performance optimization. Database servers are often critical components of applications, so it is important to avoid overloading them with unnecessary traffic.  
- Lastly, maintainability is crucial, and administrators, with their training and experience, are entrusted with making changes to the database schema or data to avoid disrupting the application.  

### Structure of Three-Tier Architecture
In a three-tier database architecture, the application presentation layer and business logic layer exist in different tiers.

- The presentation layer serves as the user interface, accessible through various platforms like desktop applications, web browsers, or mobile apps.  
- The client application interacts with an application server via the network.  
- The application server encapsulates both the application and business logic, establishing communication with the database server through a database API or driver.  

For instance, in an Internet banking app scenario, the client application, such as a mobile phone, connects to a banking application server, which further communicates with the bank's database servers storing users account data.

---

## Cloud-Based Deployment
Let's now learn about Cloud topology. Using the Cloud to deploy databases is becoming increasingly popular.

In a cloud deployment, the database resides within a cloud environment, offering the many advantages inherent to cloud-based services. Therefore, it eliminates the need to download or install database software locally and ongoing maintenance of supporting infrastructure.

Cloud-based databases are easily accessible to users from anywhere at any time, and with only an internet connection required.

Client applications and users interact with the database through an application server layer or interface situated within the cloud environment.

The flexibility of cloud deployments make them suitable for a wide range of purposes, including development, testing, and full-scale production environments.

---

## Summary
In this video, you learned that deployment topology involves organizing hardware, software, and network components.

- A single-tier architecture deploys all components of an application on a single server or machine.  
- In a two-tier database setup, the database server and application operate in separate tiers.  
- In a three-tier database architecture, the application presentation layer and business logic layer exist in different tiers.  
- Users with an internet connection can access cloud-based databases from anywhere.  