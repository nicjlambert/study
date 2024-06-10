_Microsoft Fabric is an end-to-end data analytics SaaS solution. It brings many workloads in the analytics area, including Data Integration, Warehousing, Engineering, Business Intelligence, Data Science, and Real-time Analytics._

# Plan, Manage, and Implement a Solution

## Batch 12

### Question 1

Which of the following is the most effective approach for configuring a Microsoft Fabric workspace for a Power BI project?

1. Set up the workspace with default settings and allow all team members to have admin privileges
2. Create an App Workspace, add team members with member or admin roles based on their responsibilities, and implement item-level access controls <-- **ANS**
3. Use a single workspace for all projects and datasets to simplify management and access
4. Disable sharing options and external access to ensure data securiity, regardless of the project requirements

### Question 2

You are creating a deployment pipeline. The following activties must be performed. Put them in the correct order.

1. Make the pipeline stage public (3)
2. Assign a workspace (2)
3. Deploy to an empty stage (4)
4. Create a deployment pipeline (1)
5. Create deployment rules (6)
6. Deploy content from one stage to another (5)

Prerequisites
Step 1 - Create a deployment pipeline
Step 2 - Assign a workspace
Step 3 - Make a stage public (optional)
Step 4 - Deploy to an empty stage
Step 5 - Deploy content from one stage to another
Step 6 - Create deployment rules (optional)

[Reading](https://learn.microsoft.com/en-us/fabric/cicd/deployment-pipelines/get-started-with-deployment-pipelines?tabs=from-fabric)

### Question 3

You are attempting to find a way around the 48 refresh limit per day that the Power BI service imposes. Which of the following would allow you to accomplish this?

1. Upgrade to a Power BI P2 / F128 capacity where this limit has been removed
2. Write a DAX method to do this. Refreshes done within a DAX mthod are not subject to this limit
3. Create PowerShell code that performs the refresh using XLMA endpoints. The refresh limit is no applicable in this situation <-- **ANS**
4. There is no way to accomplish this

[Reading](https://learn.microsoft.com/en-us/power-bi/enterprise/service-premium-connect-tools)

### Question 4

Microsoft Fabric supports capacity bursting and smoothing. What is the purpose of this?

1. To allow you to consume extra compute resources (capacity) beyond what you have purchased, for pay-as-you-go payment plans <-- **ANS**
2. To allow you to consume extra compute resources (capacity) beyond what you have purchased, for reserved pricing plans
3. To allow you to consume extra compute resources (capacity) beyond what you have purchased. Microsoft will then invoice you for the excess capacity used, for pay-as-you-go payment plans
4. To allow you to consume extra compute resources (capacity) beyond what you have purchased. Microsoft will then invoice you for the excess capacity used, for reserved payment plans.

Bursting and smoothing only applies to pay-as-you-go. With resvered pricing plans you'll never pay more than you agreed to.

[Reading](https://blog.fabric.microsoft.com/en-us/blog/fabric-capacities-everything-you-need-to-know-about-whats-new-and-whats-coming/)

### Question 5

You purchase an F2 capacity on a pay-as-you-go basis. What happens if you consume more than 2 capacity units during a Fabric operation?

1. Your request will be rejected
2. Your request will be throttled
3. Your request will succeed, and the excess capacity units consumed will be ignored if it only happens once per 1 hour period
4. Your request will succeed, and the excess capacity units consumed will be applied to a point in the future when you have excess capacity.  <-- **ANS**

[Reading](https://learn.microsoft.com/en-us/fabric/data-warehouse/compute-capacity-smoothing-throttling)