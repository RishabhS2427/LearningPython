# Views

Welcome to Views. After watching this video, you will be able to describe views, create and use a view, explain how materialized views differ from regular views, create and use a materialized view.

---

## Definition of Views
A view is an alternative method of presenting information sourced from one or more tables or additional views.

You can interact with views in the same way as you interact with tables. Inserting, updating, and deleting data as required.

---

## Advantages of Views
Views are a useful way of:

- limiting access to sensitive data  
- simplifying data retrieval  
- reducing access to underlying tables  

For example, you could create a view to include the name and email columns from these two tables.

Users can then easily access this data without needing to know that it is stored in two different tables and without being given access to the sensitive salary information.

---

## Creating Views in pgAdmin
In pgAdmin, you create views within a schema.

### Steps
- In the tree view on the left-hand side, right-click "Views"  
- Click "Create"  
- Click "View"  
- This opens the Create View box  
- First need to name the view  
- On the Code page, enter the SQL code that defines the view  
- Click "Save"  

You'll then see your view in the view's folder and you can expand the view to display the columns included in it.

---

## Using Views
To run the view:

- Right-click the view name  
- Click "View/Edit Data"  
- Click "All rows"  

You'll then see all the rows included in the view.

---

## Materialized Views
PostgreSQL also supports another type of view, a materialized view.

When you refresh a materialized view for the first time, the result set is materialized or saved for future use.

### Characteristics
- you can only query the data  
- cannot update or delete it  
- enhances performance for future querying  
- result set is readily available  
- often stored in memory  

---

## Creating Materialized Views

Creating a materialized view is a similar process to creating a regular view.

### Steps
- Start in the materialized views folder in the view tree  
- Enter the name for the view on the definition page  
- Enter the code to define the view  
- Click "Save"  

This example includes just the employee ID and salary columns from the employee_details table to anonymize the salary information.

The materialized view is added to the folder.

---

## Using Materialized Views
Because the view stores the data:

- before using it, you need to refresh it with the current rows  
- then you can use the view to access the data it holds  
- you can refresh the data in the view at any time to update it with the data in the underlying tables  

---

## Summary
In this video, you learned that:

- views are another way of data presentation from one or more tables  
- you can use views to restrict access to sensitive data and for easier data retrieval  
- materialized views store the result set for quicker access  
- you cannot insert, update, or delete rows using a materialized view  