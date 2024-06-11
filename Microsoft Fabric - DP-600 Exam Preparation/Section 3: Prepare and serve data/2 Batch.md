_Microsoft Fabric is an end-to-end data analytics SaaS solution. It brings many workloads in the analytics area, including Data Integration, Warehousing, Engineering, Business Intelligence, Data Science, and Real-time Analytics._

# Prepare and serve data

## Batch 2

### Question 1

Which of the following is the fastest and most efficient way of ingesting data into a warehouse?

* T-SQL Copy statement <-- **ANS**
* Dataflows Gen2
* Dataflows Gen1
* Data pipelines

[Reading](https://learn.microsoft.com/en-us/fabric/data-warehouse/ingest-data-copy)

### Question 2

You are developing a Power BI report for a large retail company. The source data model includes a large fact table with many millions of rows and several dimension tables. You want to build a semantic model.

Which of the following scenarios justifies using DAX Studio and Tabular Editor 2 for semantic model design and development in the best way? Choose one.

* You want to define relationships between dimension tables and the fact table using Relationship Editor.
* You need to create calculated columns and measures to enrich the data model with new insights.
* You want to import data from various sources and create a data model from scratch.
* You need to configure data partitioning and test aggregation strategies and DAX measures during development. <-- **ANS**

### Question 3

In the context of using Microsoft Fabric notebooks for data analytics, which of the following is the most effective method for identifying and resolving data loading bottlenecks? Select one.

* Increase the memory allocation for each notebook instance.
* Consolidate all data processing tasks into a single notebook to streamline data management.
* Implement cross workspace “save as” feature for better data management.
* Redesign the SQL queries to optimize performance and make sure V-Order is implemented in the tables. <-- **ANS**

[Reading](https://learn.microsoft.com/en-us/fabric/data-engineering/delta-optimization-and-v-order?tabs=sparksql)

### Question 4

You are managing a data warehouse in Microsoft Fabric and notice performance degradation due to a large number of small Parquet files. Which of the following strategies would be most effective in addressing this issue?

1. Utilize the OPTIMIZE statement to consolidate small files into larger ones, reducing file count and metadata overhead.
2. Adjust the spark.microsoft.delta.optimizeWrite.binSize configuration property to increase the target file size for new writes, proactively preventing excessive small files.
3. Consider partitioning the table to organize data into logical segments, allowing for more targeted optimization and potentially reducing the number of files scanned for queries.
4. Enable V-Order optimization to improve Parquet file layout and compression, potentially reducing file sizes and improving query performance.
5. All the above <-- **ANS**

[Reading](https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-and-delta-tables)
[Reading](https://www.linkedin.com/posts/jasonpresley_delta-lake-table-optimization-and-v-order-activity-7067541783500492801-ZqFh)
[Reading](https://www.red-gate.com/simple-talk/blogs/microsoft-fabric-checking-and-fixing-tables-v-order-optimization/)
[Reading](https://www.red-gate.com/simple-talk/blogs/microsoft-fabric-and-the-delta-tables-secrets/)
[Reading](https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-and-delta-tables)
[Reading](https://www.linkedin.com/posts/jasonpresley_delta-lake-table-optimization-and-v-order-activity-7067541783500492801-ZqFh)

### Question 5

Which of the following workspace roles can create a table clone? Choose all that apply.

1. Admin <-- **ANS**
2. Member <-- **ANS**
3. Contributor <-- **ANS**
4. Viewer