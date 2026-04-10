::page{title="Hands-on Lab: Create Tables and Load Data in Datasette"}


<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/images/IDSN-logo.png" width="300"><br>

##

**Estimated time needed:** 20 minutes

In this lab, you will learn how to create tables and load data in Datasette.

## Objectives

After completing this lab, you will be able to:

* Create and load data into a table from a CSV file
* Create and load data into a table from a SQL script file

## Prerequisites


In this lab, you will use <a href="https://github.com/simonw/datasette?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2022-01-01" target="_blank">Datasette, </a>an open-source multi-tool for exploring and publishing data.

## Datasets

 PETSHOP and BookShop are the two data sets you will use in this lab.

*   PETSHOP:

      <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Create%20Tables%20and%20Load%20Data%20in%20Db2/images/PETSHOP_table.png">

*   BookShop:

      <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Create%20Tables%20and%20Load%20Data%20in%20Db2/images/BookShop_table.png">




::page{title="Exercise 1: Load a CSV file and create a table using the Datasette tool"}


In this exercise, you will learn how to load a CSV file and create a table using the Datasette tool.

1. First, select **Open tool**, then click the  **Navigation Pane** at the right-end corner, and then select **Add DataSets**.

   ![Add a Dataset](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/Datasetteoptionallabs/Week2/images/Fig1.PNG)


2. You will then be redirected to a page where you need to enter the full URL of the CSV data set in the text box.

    * Right-click the link [PETSHOP.csv](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/datasets/PET_Tables/PETSHOP.csv) and copy the link address. Enter the copied URL in the text box and select the **create** button.



   ![CSV file](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/Datasetteoptionallabs/Week2/images/Fig2.PNG)

3.  The data loaded from the CSV file will create the PETSHOP table. By default, a **SELECT** query related to the table will appear on the **text area** section of the following webpage. Click **Submit Query** to view the results.

    ![Select query](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/Datasetteoptionallabs/Week2/images/Fig3.PNG)

4.  Next, modify the **SELECT** query as follows:

     ```
     select count(*) from PETSHOP
     ```

   Once you have completed this step, you should see all five rows of the PETSHOP table.

   ![PETSHOP DATABASE](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/Datasetteoptionallabs/Week2/images/Fig4.PNG)

5.  You have successfully created and loaded the **PETSHOP** table.

::page{title="Exercise 2: Create and load data in the table using an SQL script file "}


In this exercise, you will learn how to create and load data into a table by running a script containing the CREATE and INSERT SQL commands.

1.  Download the script file to your computer:

    *   [BookShop-CREATE-INSERT.sql](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/Datasetteoptionallabs/Week2/data/BookShop-CREATE-INSERT.sql)

</br>
2.  Open the script file using a notepad or any text editor.

* Copy the contents of the script file and paste it in the datasette text area
- Select Submit query


    ![Submit query](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/Datasetteoptionallabs/Week2/images/Fig5.PNG)

3. Next, click the **home** link at the top of the page.
</br>

   ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/Datasetteoptionallabs/Week2/images/Fig6.PNG)

4. This step will redirect you to a page displaying **Databases and Tables**.

   * Select the **BookShop** table under the **PetShop** database.

   ![Petshop database](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/Datasetteoptionallabs/Week2/images/Fig7.PNG)

5. You will be able to view the **columns** and **data** of the **Bookshop** table.

   ![Bookshop database](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/Datasetteoptionallabs/Week2/images/Fig8.PNG)

</br>

<h3> Congratulations! You have completed this lab and are ready for the next topic. </h3>

</br>

<!--
## Author(s)
* [Sandip Saha Joy](https://www.linkedin.com/in/sandipsahajoy/)

* [Lakshmi Holla](https://www.linkedin.com/in/lakshmi-holla-b39062149/)
<footer>

<!--## Changelog

| Date       | Version | Changed by      | Change Description          |
| ---------- | ------- | --------------- | --------------------------- |
| 30-01-2024 | 1.3     | Mary Stenberg   | QA pass with edits          |
| 14-06-2022 | 1.2     | Lakshmi Holla | Converted intial version to DataSette |
| 29-07-2021 | 1.1     | Lakshmi Holla   | Modified  as per new DB2 UI |
| 16-03-2020 | 1.0     | Sandip Saha Joy | Created initial version     |
IBM Corporation 2023. All rights reserved.
-->


## <h3 align="center"> &#169; IBM Corporation. All rights reserved. <h3/>
