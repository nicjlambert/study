_Microsoft Fabric is an end-to-end data analytics SaaS solution. It brings many workloads in the analytics area, including Data Integration, Warehousing, Engineering, Business Intelligence, Data Science, and Real-time Analytics._

# Plan, Manage, and Implement a Solution

## Batch 4

### Question 1

True or false: with reserved capacity pricing you will never pay more than the agreed upon price?

True: When you attempt to exceed capacity limits, you are throttled. With reserved capacicty priocing you'll never pay more than you agreed to.

[Reading](https://learn.microsoft.com/en-us/power-bi/enterprise/service-premium-capacity-manage)

### Question 2

In a large organisation, a Power BI developer uses the Lineage View to assess the impact of proposed changes in a data source that feeds multiple reports and dashboards. What key aspect would the Lineage View primarily help to identify in this scenario?

The specific reports and dashboards that will be affected by the change in the data source.

[Reading](https://learn.microsoft.com/en-us/fabric/governance/lineage)

### Question 3

When using XLMA endpoints for semantic model write operations, it is recommended to enable Large Model support for models over this size:

1. 250MB
2. 500MB
3. 1GB **<- ANS**
4. 5GB
5. 10GB

Workspaces use the `XML for Analysis (XMLA)` protocol for communications between client applications and the engine that manages your Power BI workspaces and semantic models.

[Reading](https://learn.microsoft.com/en-us/power-bi/enterprise/service-premium-connect-tools)

### Question 4

Which of the following are primary reasons for applying a sensitivity label to an item in Power BI?

1. To let users know the item may contain sensitive data
2. To ensure only authorised people can access the data **<- ANS**
3. To prevent reports and queries from accessing the data
4. To track user accounts and groups used in Microsoft Fabric permission settings

[Reading #1](https://learn.microsoft.com/en-us/fabric/get-started/apply-sensitivity-labels)
[Reading #2](https://learn.microsoft.com/en-us/power-bi/enterprise/service-security-sensitivity-label-overview)

### Question 5

Which of the following true:

1. Shared recipients only have access to the data warehouse shared with them and not any other items within the same workspace as the warehouse **<- ANS**
2. Read all data using SQL permission gives the user granuar access to items in a data warehouse
3. Shared recipients of a data warehouse are also able to re-share the data warehouse
4. If a report is built on top of a data warehouse and is shared with another recipient, the shared recipient will always be able to acces the report

[Reading](https://learn.microsoft.com/en-us/fabric/data-warehouse/share-warehouse-manage-permissions)
