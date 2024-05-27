_Microsoft Fabric is an end-to-end data analytics SaaS solution. It brings many workloads in the analytics area, including Data Integration, Warehousing, Engineering, Business Intelligence, Data Science, and Real-time Analytics._

# Plan, Manage, and Implement a Solution

## Batch 9

### Question 1

Which of the following are valid deployment permissions?

1. Tenant admin
2. Pipeline admin <-- **ANS**
3. Workspace viewer  <-- **ANS**
4. Workspace contributor <-- **ANS**
5. Workspace admin <-- **ANS**

[Reading](https://learn.microsoft.com/en-us/fabric/cicd/deployment-pipelines/understand-the-deployment-process)

### Question 2

Which of the following are valid ways of applying a report theme in Power BI?

1. Select from the available list of themes in Power BI Desktop
2. Use the theme gallery in Power BI Desktop
3. Customise a theme using the customise theme dialog
4. Import a custom theme json file

All of them.

[Reading](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-report-themes)

### Question 3

Which of the following is not included in a Power BI temple (.pbit) file?

1. Report pages, visuals and other elements
2. Data model definition
3. Queries and query parameters
4. All report data <-- **ANS**
5. Sampling of data <-- **ANS**

[Reading](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-templates)

### Question 4

True of false, sensitivity labels are always copied from one pipeline stage to another when a deployment is done.

`FALSE` certain conditions must be met.

Sensitivity labels are copied only when one of the following conditions is met. If these conditions aren't met, sensitivity labels are not copied during deployment.

* A new item is deployed, or an existing item is deployed to an empty stage.

* The source item has a label with protection and the target item doesn't. In this case, a pop-up window asks for consent to override the target sensitivity label.

[Reading](https://learn.microsoft.com/en-us/fabric/cicd/deployment-pipelines/understand-the-deployment-process)

### Question 5

You want to set up a data gateway to allow a single user to access data behind a firewall that is needed for a Power App. You set up an On-Premises data (personal mode) gateway. Will this satisfy the requirement?

No. Only Power BI is support with personal mode.

[Reading](https://learn.microsoft.com/en-us/data-integration/gateway/service-gateway-onprem)
