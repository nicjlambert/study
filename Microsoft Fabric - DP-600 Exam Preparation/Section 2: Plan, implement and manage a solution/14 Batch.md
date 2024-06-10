_Microsoft Fabric is an end-to-end data analytics SaaS solution. It brings many workloads in the analytics area, including Data Integration, Warehousing, Engineering, Business Intelligence, Data Science, and Real-time Analytics._

# Plan, Manage, and Implement a Solution

## Batch 14

### Question 1

When a workspace is deleted, it can be restored up to a certain number of days. This is known as the retention period. What is the default and maximum retention period?

1. 0, 30
2. 7, 30
3. 7, 45
4. 14, 120
5. 7, 90 <-- **ANS**

The retention period for collaborative workspaces is configurable. The default retention period is seven days. However, Fabric administrators can change the length of the retention period by turning on the Define workspace retention period setting in the admin portal and specifying the desired retention period (from 7 to 90 days).

[Reading](https://learn.microsoft.com/en-us/fabric/admin/portal-workspaces)

### Question 2

Which protocol is used to communicate between client applications and the engine that manages semantic models?

1. HTTPS
2. TDS
3. XMLA <-- **ANS**
4. None of these

Workspaces use the XML for Analysis (XMLA) protocol for communications between client applications and the engine that manages your Power BI workspaces and semantic models.

[Reading](https://learn.microsoft.com/en-us/power-bi/enterprise/service-premium-connect-tools)

### Question 3

Which of these semantic models cannot be accessed using XLMA endpoints:

1. Models located in a Fabric workspace
2. Models located in My Workspace  <-- **ANS**
3. Models using DirectQuery
4. Direct Lake Models
5. Models in an Excel workbook  <-- **ANS**

[Reading](https://learn.microsoft.com/en-us/power-bi/enterprise/service-premium-connect-tools)

### Question 4

You are attempting to set up single sign on to an Oracle environment but are not able to do so. What might cause this?

1. Microsoft Fabric does not support SSO to Oracle
2. The Oracle administrator has this feature disabled
3. Oracle SSO is disabled in the Fabric Admin portal <-- **ANS**
4. When connecting to Oracle in Fabric you must specify authenticating via SSO

[Reading](https://learn.microsoft.com/en-us/fabric/admin/tenant-settings-index)

### Question 5

Which of the following applications are not able to use XMLA endpoints

1. Microsoft Excel
2. SQL Server Profiler
3. SQL Server Management Server
4. PowerShell
5. All of these can use XMLA endpoints <-- **ANS**

[Reading](https://learn.microsoft.com/en-us/power-bi/enterprise/service-premium-connect-tools)