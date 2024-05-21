_Microsoft Fabric is an end-to-end data analytics SaaS solution. It brings many workloads in the analytics area, including Data Integration, Warehousing, Engineering, Business Intelligence, Data Science, and Real-time Analytics._

# Plan, Manage, and Implement a Solution

## Batch 6

### Question 1

You want to grant a user read-only access to a workspace. Which workspace role would be best for this purpose?

1. Admin
2. Contributor
3. Viewer <-- **ANS**
4. Member
5. Read-only

[Reading](https://learn.microsoft.com/en-us/power-bi/collaborate-share/service-new-workspaces)

### Question 2

Your organisation has a central dataset that needs to be accessed and analysed by multiple teams.
You've created a robust semantic model in Power BI Desktop that accurately reflects the data structure and relationships.
Which of the following methods would be the most appropriate for sharing this semantic model with other users, ensuring
they can create their own reports and dashboards while maintaining a single source of truth?

1. Distribute copies of the Power BI Desktop file (`.pbix`) to each user
2. Publish the model to the Power BI Service as a shared dataset <- **ANS**
3. Export the model as a template file (`.pbit`) and share it with other users
4. Create live connections to the underlying data source in separate Power BI Desktop files
5. Embed the model directly into a SharePoint site for collaborative access.

[Reading](https://learn.microsoft.com/en-us/power-bi/connect-data/service-datasets-share)

### Question 3

You have users telling you that they are unable to export report data to Excel. What factor(s) might cause this?

1. Power BI Desktop does not allow exporting to Excel
2. This feature is turned off at the tenant level <- **ANS**
3. When the report was created the export to Excel feature was turned off <- **ANS**
4. Users are attempting to export to Excel from a Matrix visual which does not support this operation

[Reading](https://learn.microsoft.com/en-us/fabric/admin/about-tenant-settings)

### Question 4

Which of the following roles would allow you to perform the duties of a Fabric Administrator?

1. Global Administrator <- **ANS**
2. Power Platform Administrator <- **ANS**
3. License Administrator
4. Fabric Administrator <- **ANS**
5. User Administrator

To be a Microsoft Fabric admin for your organization, you must be in one of the following roles:

* Global administrator
* Power Platform administrator
* Fabric administrator

[Reading](https://learn.microsoft.com/en-us/fabric/admin/roles)

### Question 5

Microsoft recommends enabling `large model support` for semantic models when enabling `XMLA` read-write capability.
Why is this?

1. Large model support will not function correctly without XMLA read-write capability
2. Models over 50GB will generally operate faster
3. Models over 1GB will generally operate much faster <- **ANS**
4. When using a Fabric capacity XMLA read-write capabilities is required. But it is not required for a Power BI capacity

When using the XMLA endpoint for semantic model management with write operations, it's recommended you enable the semantic model for large models.
This reduces the overhead of write operations, which can make them considerably faster. For semantic models over 1 GB (after compression), the difference can be significant.

[Reading](https://learn.microsoft.com/en-us/power-bi/enterprise/service-premium-connect-tools)
