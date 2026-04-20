::page{title=""}

# Hands-on Lab: Views in PostgreSQL

<img src="
https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/images/IBM_logo.png"
width="300">

**Estimated time needed:** 15 minutes

##

In this lab, you will learn how to create, execute, and materialize views in the PostgreSQL database service using the pgAdmin graphical user interface (GUI) tool. Materialized views behave differently compared to regular views. The result set is materialized or saved for future use in the materialized views. You can not insert, update, or delete rows like in regular views. Materialized views store the results of a database query as a separate table-like object so that someone can access the results later without having to re-run the query. As a result, materialized views can improve database performance compared to regular views.

## Software used in this lab

In this lab, you will use the <a target="_blank" href="https://www.postgresql.org/">PostgreSQL Database</a>. PostgreSQL is a relational database management system (RDBMS) designed to store, manipulate, and retrieve data efficiently.

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Views%20in%20PostgreSQL/images/postgresql.png" width="130" height="100">
<p>

To complete this lab, you will utilize the PostgreSQL relational database service available as part of IBM Skills Network Labs (SN Labs) Cloud IDE. SN Labs is a virtual lab environment used in this course.

## Database used in this lab

You will use the eBooks database in the lab.

The following ERD diagram shows the schema of the complete eBooks database used in this lab:

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/datasets/eBooks/eBooks_schema_complete.png" width="630" height="500">

## Objectives

After completing this lab, you will be able to use pgAdmin with PostgreSQL to:

- Restore a database schema and data
- Create and execute a view
- Create and execute a materialized view

## Lab structure

In this exercise, you will go through three tasks to learn how to create and execute views and materialized views in the PostgreSQL database service using the pgAdmin graphical user interface (GUI) tool.

## Task A: Restore a database schema and data

To get started with this lab, you will first download the relevant **eBooks** database dump file, then launch PostgreSQL and pgAdmin using the Cloud IDE. You can do this by following these steps:

1. Download the following **eBooks** PostgreSQL dump file (containing the eBooks database schema and data) to your local computer.

    - [eBooks_pgsql_dump.tar](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/datasets/eBooks/eBooks_pgsql_dump.tar)

2. Click the Skills Network extension button on the left side of the window.

3. Open the **DATABASES**  menu and click **PostgreSQL**.

4. Click **Create**. PostgreSQL may take a few moments to start.

     ![postgres start pic.png](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/4zLhpz5CI5tmSl-DH7NRXQ/postgres%20start%20pic.png)

5. Next, open the pgAdmin Graphical User Interface by clicking **pgAdmin** in the Cloud IDE interface.

     ![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/ZnZiQafAH3ZwT4V6Wz7fYw/pgadmin%20.png)

6. Once the pgAdmin GUI opens, click **Servers** tab on the left side of the page. You will be prompted to enter a password.

    ![pgAdmin_2](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Create%20Tables%20and%20Load%20Data%20in%20PostgreSQL%20using%20pgAdmin/images/pgAdmin_2.png)

7. To retrieve your password, click **PostgreSQL** tab near the top of the interface and select **Connection Information** tab.


     ![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/priMDdmsl6kx9EFaQ2kHGA/pgadmin-pass1.png)
	
8. Scroll down and click the Copy icon on the left of your password to copy the session password onto your clipboard.
	
	 ![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/EfhCH4BlDAZOTsvjRhHw3Q/pgadmin-pass2.png)

9. Navigate back to the **pgAdmin** tab and paste your password, then click **OK**.

10. You will then be able to access the pgAdmin GUI tool.

    ![pgAdmin GUI tool](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Views%20in%20PostgreSQL/images/1.5.png)

11. In the tree view, expand **Servers** > **postgres** > **Databases**. Enter your PostgreSQL service session password if prompted during the process. Right-click on **Databases** and go to **Create > Database**. Type **eBooks** as the  database name and click **Save**.

    ![Servers** > postgres > **Databases](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Views%20in%20PostgreSQL/images/1.6.1.png)

    <p>

    ![Create > Database](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Views%20in%20PostgreSQL/images/1.6.2.png)

12. In the tree-view, expand **eBooks**. Right-click **eBooks** and select **Restore**.

    ![tree-view](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Views%20in%20PostgreSQL/images/1.7.png)

13. Follow the instructions below to restore and proceed to Task B:

    - On the **General** tab, click **Select file** by the **Filename** box.

        ![General tab](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/b-xbFvgUwclATKK8I5grog/1-8-1.png)

    - Ensure that you upload the files to this path: /var/lib/pgadmin/. To do this, you can either manually navigate to the path (or) copy /var/lib/pgadmin/, replace /home/ with it, and press Enter. You should then see some default files in that path, as shown below.

		![General tab](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/ewH2MCoByP4XxV7MVsHmNA/default-files.png)

    - Click on the three dots, then select **Upload**.

        ![Upload file](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/xnZ4AHriciZG7a522bEUlQ/1-8-2.png)

    - Double-click on the drop files area and load the **eBooks_pgsql_dump.tar** you downloaded earlier on your local computer.

        ![Drop files area](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/a2VVrYt0CSJe-i8jJ-Y6_g/1-8-3.png)

    - When the upload is complete, close the drop files area by clicking **X**.

        ![Drop files area](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/Jp9EWspBTSsZXKPZtKuuHQ/1-8-4.png)

    - Ensure **Format** is set to **All Files**, select the uploaded **eBooks_pgsql_dump.tar** file from the list, and then click **Select**.

        ![Format](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/mbW6cKrapGgNjtOjgStrmw/1-8-5.png)

    - In the General tab, ensure the filename path matches the one shown below. If you see a different path that includes "None," modify it accordingly.

        ![Restore options](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/q93FepMgL0EsosgO0cM0Qg/1-8-6.png)

    - Now switch to the **Options** tab. Under **Disable**, toggle on the **Triggers** option, and then click Restore.

        ![ Restore*](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/7EhYMgQUhnvOeiuOrD7-2Q/1-8-7.png)

## Task B: Create and execute a view

1. In the tree-view, expand **eBooks > Schemas > public**. Right-click **Views** and go to **Create > View**.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Views%20in%20PostgreSQL/images/2.1.png)

2. On the **General** tab, type **publisher_and_rating_view** as the name of the view. Then, switch to the **Code** tab.

    ![General tab](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Views%20in%20PostgreSQL/images/2.2.png)

3. On the **Code** tab, copy and paste the following code. Then click **Save**.

    ```
    SELECT books.title, books.rating, publishers.name
    FROM books INNER JOIN publishers ON books.publisher_id = publishers.publisher_id
    ```



    ![Code tab](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Views%20in%20PostgreSQL/images/2.3.png)

4. In the tree view, expand **Views**. Right-click **publisher_and_rating_view** and go to **View/Edit Data > All Rows**.

    ![PgAdmin](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Views%20in%20PostgreSQL/images/2.4.png)

5. You will access the view you created. This action allows you to access and view the tables in your database.

    ![tables in database](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Views%20in%20PostgreSQL/images/2.5.png)

## Task C: Create and execute a materialized view

1. In the tree view, expand **eBooks > Schemas > public**. Right-click **Materialized Views** and go to **Create > Materialized View**.

    ![eBooks > Schemas > public](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Views%20in%20PostgreSQL/images/3.1.png)

2. On the **General** tab, type **publisher_and_rating_materialized_view** as name of the view. Then switch to the **Code** tab.

    ![General tab](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/KJxPhJHOtP3fIBRawlKxIA/3-2.png)

3. On the **code** tab, copy and paste the following code. Then click **Save**.

    ```
    SELECT books.title, books.rating, publishers.name
    FROM books INNER JOIN publishers ON books.publisher_id = publishers.publisher_id
    ```



    ![Definition tab](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/eHpb35GPfVHUuzaaoNjqZg/3-3.png)

4. In the tree-view, expand **Materialized Views**. Right-click **publisher_and_rating_materialized_view** and go to **Refresh View > With data**.

    ![Materialized Views](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Views%20in%20PostgreSQL/images/3.4.png)

5. Right-click **publisher_and_rating_materialized_view** again and go to **View/Edit Data > All Rows**.

    ![publisher_and_rating_materialized_view](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Views%20in%20PostgreSQL/images/3.5.png)

6. You will access the materialized view you created.

    ![your materialized view](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Views%20in%20PostgreSQL/images/3.6.png)

At first glance, it does not look too different from the regular view you created earlier in this lab. From the user perspective, it is essentially the same: you see the results of a query displayed in a table-like format. The difference is that this materialized view is cached in the database so someone can reaccess the data in the future without re-running the database query.

## Conclusion
Congratulations! You have completed this lab and learned how to restore a database schema and data, create and execute a view, and create and execute a materialized view.

<br>

#### Author: [Sandip Saha Joy](https://www.linkedin.com/in/sandipsahajoy/)

#### Other Contributors: [David Pasternak](https://www.linkedin.com/in/david-pasternak-6b84a2208/)

<footer>

<img align="left" src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/images/MicrosoftTeams-image.png" alt="">

</footer>

<br>



<center><h3> © IBM Corporation. All rights reserved. <h3/></center>

<!--
	## Changelog

| Date | Version | Changed by | Change Description |
|------|--------|--------|---------|
| 2021-03-25 | 1.0 | Sandip Saha Joy | Created initial version |
| 2021-10-18 | 1.1 | David Pasternak | Updated instructions |
| 2024-01-30 | 1.2 | Mary Stenberg   | QA review           |
| 2024-09-02 | 1.4 |Anita Verma | Updated lab instructions and screenshots |

--!>