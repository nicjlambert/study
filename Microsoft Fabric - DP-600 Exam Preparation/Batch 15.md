_Microsoft Fabric is an end-to-end data analytics SaaS solution. It brings many workloads in the analytics area, including Data Integration, Warehousing, Engineering, Business Intelligence, Data Science, and Real-time Analytics._

# Plan, Manage, and Implement a Solution

## Batch 15

### Question 1

Which of the following is true when applying Sensitivity labels in Power BI Desktop

1. You must have a Power BI Pro or Premium Per User license <- **ANS**
2. Sensitivity labels must be enabled for your organisation  <- **ANS**
3. You do not need to be signed in
4. You must belong to a security group that has permissions to apply sensitivity labels  <- **ANS**

[Reading #1](https://learn.microsoft.com/en-us/fabric/get-started/apply-sensitivity-labels)
[Reading #2](https://learn.microsoft.com/en-us/power-bi/enterprise/service-security-sensitivity-label-overview)

### Question 2

Which of the following is true about a Power BI Project (.pbit) file?

1. They are highly optimised Power BI files offering better optimisation and performance than .pbix files
2. They are highly secure and encrypted files offering greater security than .pbix files
3. They are individual plain text files in easy to understand folder structures in an XML format
4. They are individual plain text files in easy to understand folder structures in an JSON format  <- **ANS**

[Reading](https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-overview)

### Question 3

You would like to limit who can create a workspace to three people in your organisation. What is the best way to acheive this?

1. Give each of the users a password and have them enter the password when creating a workspace
2. Enter the email addresses of the three users in the Workspace Settings of the Admin portal
3. Put the three users in a security group and enter that security group in the Workspace Settings of the Admin portal  <- **ANS**
4. It is not possible to limit who can create workspaces. Anyone in an organisation can create a workspace.
5. Both #2 and #3

### Question 4

You are building a warehouse in Fabric for your company.

You plan to modify the schema for one of the tables in the warehouse. How can you effectively assess the potential impact of this change on downstream dependencies?

1. Implement data versioning in the warehouse and analyse historical reports to compare results before and after the schema change
2. Use the impact analysis feature within Fabric that traces data lineage and highlights all dependent objects <- **ANS**
3. Schedule test deployments of the modified schema and manually observe the behavior of dependent reports in seperate environments
4. Manually review all Power BI reports using the log data to identify affected visuals and calculations

[Reading](https://learn.microsoft.com/en-us/fabric/governance/lineage)

### Question 5

A single workspace can contain how many semantic models and how many reports per semantic model?

1. 100 and 100
2. 250 and 250
3. 500 and 500
4. 1,000 and 1,000 <- **ANS**

[Reading](https://learn.microsoft.com/en-us/power-bi/collaborate-share/service-new-workspaces)
