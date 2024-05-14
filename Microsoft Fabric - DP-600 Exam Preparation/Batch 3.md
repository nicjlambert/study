_Microsoft Fabric is an end-to-end data analytics SaaS solution. It brings many workloads in the analytics area, including Data Integration, Warehousing, Engineering, Business Intelligence, Data Science, and Real-time Analytics._

# Plan, Manage, and Implement a Solution

## Batch 3


### Question 1

You want to allow users to use Excel to view and interact with on-premises Power BI datasets. However, some users are saying that they are not able to do so. Which of the following could be reasons why?

'Allow XMLA endpoints' and 'Analyze in Excel' with on-premises datasets is probably disabled at the tenant level.


[Reading](https://learn.microsoft.com/en-us/power-bi/enterprise/service-premium-connect-tools)

### Question 2

Which of the following is/are true regarding XMLA endpoints?

'XMLA endpoints' support open-platform connectivity from Microsoft and third-party client applications and tools. By default, 'read-only' connectiviety is enabled. And 'read-write' connectivity can be enabled but isn't by default.

[Reading](https://learn.microsoft.com/en-us/power-bi/enterprise/service-premium-connect-tools)

### Question 3

You share a Lakehouse with another user. Which of the following is true about permissions the user will receive?

By default, sharing a Lakehouse grants users read permission to the Lakehouse, the associated SQL endpoint, and the default semantic model. In addition to these default permissions, you can grant:

1. ReadData permission on SQL endpoint to access data without SQL policy.
2. ReadAll permission on the lakehouse to access all data using Apache Spark.
3. Build permission on the default semantic model to allow building Power BI reports on top of the semantic model.


[Reading #1](https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-sharing)	
[Reading #2](https://learn.microsoft.com/en-us/fabric/get-started/share-items)

### Question 4

You are Fabric administrator, and you want to purchase a Fabric capacity that allows you to execute light Fabric workloads and also allow up to 20 users to view Power BI reports in the most cost effective way. You decide to purchase an F 64 capacity. Does this meet the goal of minimizing cost?

No, it would be cheaper to purchase an F2, F4 or F8 etc and purchase 20 Power BI Pro licenses at ~$10 per month.

[Reading](https://learn.microsoft.com/en-us/fabric/enterprise/licenses)

### Question 5

Where can sensitivity labels be applied?

They can be applied in Power BI Desktop or Power BI Service (not Purview or the Micrsoft 365 Portal)

[Reading #1](https://learn.microsoft.com/en-us/fabric/get-started/apply-sensitivity-labels)
[Reading #2](https://learn.microsoft.com/en-us/power-bi/enterprise/service-security-sensitivity-label-overview)
