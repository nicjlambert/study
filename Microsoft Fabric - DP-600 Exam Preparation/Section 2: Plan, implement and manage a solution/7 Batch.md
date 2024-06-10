_Microsoft Fabric is an end-to-end data analytics SaaS solution. It brings many workloads in the analytics area, including Data Integration, Warehousing, Engineering, Business Intelligence, Data Science, and Real-time Analytics._

# Plan, Manage, and Implement a Solution

## Batch 7

### Question 1

Which of the following types of queries does `Query Insights` track?

1. User queries <-- **ANS**
2. Internal queries
3. Any query executed that includes the `WITH_QUERY_INSIGHTS` operator included in the query statement
4. None unless Query Insights is turned on in the Admin portal

[Reading](https://learn.microsoft.com/en-us/fabric/data-warehouse/query-insights)

### Question 2

Dataflows that use a Gateway and use a data destination feature are limited to how much time before a timeout occurs?

1. 30 mins
2. 60 mins <-- **ANS**
3. 90 mins
4. 120 mins

[Reading](https://learn.microsoft.com/en-us/fabric/data-factory/gateway-considerations-output-destinations)

### Question 3

Wich of the following is not a valid place to apply sensitivity lables in Power BI?

1. Dataflows
2. Reports
3. Dashboards
4. Dataflows
5. Excel file exported from Power BI
6. All of these are valid <-- **ANS**

[Reading #1](https://learn.microsoft.com/en-us/fabric/get-started/apply-sensitivity-labels)
[Reading #2](https://learn.microsoft.com/en-us/power-bi/enterprise/service-security-sensitivity-label-overview)

### Question 4

What period of time does `Query Insights` allow you to view queries against a SQL endpoint?

1. 30 days <-- **ANS**
2. 90 days
3. 60 days
4. Unlimited

[Reading](https://learn.microsoft.com/en-us/fabric/data-warehouse/query-insights)

### Question 5

You are tasked with configuring a new Micrsoft Fabric workspace for a team of analysts. Which of the following settings would you prioritise to ensure secure and efficient collaboration? (Choose Two)

1. Enabling Azure Active Directory (Azure AD) integration for authentication and authorisation <-- **ANS**
2. Establishing workspace permissions to control access to content and resources <-- **ANS**
3. Setting up deployment pipelines to automate the delivery of content to production environments
4. Configuring usage quotas to manage resource consumption and costs
5. Integrating with external data sources to provide access to relevant datasets

It is critical to establish Azure AD integration (1.) is crucial for secure authentication and authorizatrion of users, ensuring only authorized individuals can access the workspace and its contents.

Workspace permissions (.2) provide granular control over who can view, edit, and publish content, protecting sensitive information and preventing unauthorised changes.

The other options are not directly related to security and collaboration, although they are important.