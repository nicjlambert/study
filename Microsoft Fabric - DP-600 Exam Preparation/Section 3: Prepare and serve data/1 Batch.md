_Microsoft Fabric is an end-to-end data analytics SaaS solution. It brings many workloads in the analytics area, including Data Integration, Warehousing, Engineering, Business Intelligence, Data Science, and Real-time Analytics._

# Prepare and serve data

## Batch 1

### Question 1

Your company needs to migrate sales data from an on-premises SQL Server database to a Fabric data warehouse. The data will be used for various reports and almost no transformation during the migration is needed.

Which of the following methods is the efficient and cost-effective for this data migration?

* Use Data Factory with a Copy activity <-- **ANS**
* Develop a custom Azure Function to extract data from SQL Server and stage it in a lakehouse before loading it into the warehouse
* Use Dataflows Gen2 to move the data to the warehouse
* Use Spark notebooks and write Spark code to read the SQL Server data and write it to the data warehouse.

### Question 2

[Reading](https://www.sqlshack.com/implementing-slowly-changing-dimensions-scds-in-data-warehouses)

### Question 2

You are working with a Microsoft Fabric data warehouse that employs Type 1 slowly changing dimensions (SCDs). A user requests a report that tracks historical changes to customer addresses. However, the current implementation only overwrites existing records with updates, potentially losing historical data. Which of the following approaches would be most appropriate to handle this issue?

Select one.

* Implement a Type 2 SCD for the customer dimension to store historical values.  <-- **ANS**
* Add a new 'Address History' dimension table to capture prior addresses.
* Create a separate fact table specifically for historical address data.
* Enable change tracking on the customer dimension table to track historical values.
* Modify the ETL process to append new records for each address change.

### Question 3

Which of the following statements about converting data types using PySpark in Microsoft Fabric are false? (Select 2)

* PySpark allows converting string data types to integer data types using built-in functions.
* In PySpark, Boolean values can be directly converted to numeric values (0 and 1) without any additional processing.
* PySpark supports the conversion of date strings to date objects using built-in functions.
* PySpark is incapable of handling null values during data type conversion and will result in errors if not handled properly. <-- **ANS**
* Converting data types in PySpark requires external libraries as it cannot be done using the native framework. <-- **ANS**

### Question 4

You are working with a Microsoft Fabric data warehouse that employs Type 2 slowly changing dimensions (SCDs). You need to implement a Type 2 SCD for the customer dimension to track historical changes in customer addresses. Which of the following steps would be essential to carry out this implementation?

* Add a 'Valid From' and 'Valid To' date column to the customer dimension table.
* Create a new surrogate key column to uniquely identify each version of a customer record.
* Modify the ETL process to insert new records with updated address information, rather than overwriting existing records.
* Populate the 'Valid To' date of the previous record with the date of the change when a new record is inserted.
* All of the above <-- **ANS**

[Reading](https://www.sqlshack.com/implementing-slowly-changing-dimensions-scds-in-data-warehouses)

### Question 5

You have a Fabric data warehouse containing customer transaction data. Teams analyze customer purchasing behavior across various product categories. Currently, this analysis requires complex calculations of average order value and purchase frequency for each category.

How can you optimize query performance and code reusability for these reports using views, functions, or stored procedures?

* Use materialized views for each product category, pre-computing and storing the calculated values for faster retrieval.
* Develop a stored procedure that accepts the product category as input and returns the calculated values.
* Create individual views for each product category containing the calculated average order value and purchase frequency.
* Implement user-defined functions (UDFs) within the data warehouse to encapsulate the calculations for average order value and purchase frequency.  <-- **ANS**

[Reading #1](https://www.c-sharpcorner.com/article/stored-procedures-vs-user-defined-functions-and-choosing-which-one-to-use)
[Reading #2](https://www.mssqltips.com/sqlservertip/7437/sql-stored-procedures-views-functions-examples)
