_Microsoft Fabric is an end-to-end data analytics SaaS solution. It brings many workloads in the analytics area, including Data Integration, Warehousing, Engineering, Business Intelligence, Data Science, and Real-time Analytics._

# Plan, Manage, and Implement a Solution

## Batch 1


### Question 1

You need to modify your Fabric capacity. Which of the following would you use to do this?

You use Azure Portal to modify your Fabric capacity. Settings that you can configure when managing your organization's capacity settings:

* Create new capacities
* Pause/Resume capacities
* Delete capacities
* Manage capacity permissions
* Change the size of the capacity

The size of the capacity determines the amount of computation power available.

**OneLake** ---sits below--> **Workspace** ---resides in a---> **Capacity** ---resides in a---> **Tenant**

[Reading](https://learn.microsoft.com/en-us/fabric/admin/service-admin-portal-capacity-settings)


### Question 2

Which of the following is the most accurate definition of a Microsoft Fabric capacity?

Capacity refers to compute resources (storage is a separate resource and billed seperately). Fabric **capacity is a compute resource** reserved for exclusive use be a single tenant.

When you purchase Fabric Capacity is the same thing as a Power BI capacity e.g. when you buy a F64 you also have a P1.

[Reading](https://learn.microsoft.com/en-us/fabric/admin/service-admin-portal-capacity-settings)


### Question 3

You have been asked to create a new Power BI report theme. What file options do you have to create this theme?

All Power BI theme files are stored in JSON format

[Reading](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-report-themes)


### Question 4

 You are attempting to use a Gateway to read on-premises data in a Dataflows Gen2 process. The table refresh shows as succeding but the write to destination step is failing. What is the likely cause of this? 2 are correct?

The protocol for Gateway to read on premises data uses **TCP** protocol (and on port **1433** for SQL Server port).

[Reading](https://learn.microsoft.com/en-us/fabric/data-factory/gateway-considerations-output-destinations) 


### Question 5

If someone commits a change to a Git connected branch, how are users are notified in the workspace?

Via a notification in the workspace.

[Reading](https://learn.microsoft.com/en-us/fabric/cicd/git-integration/git-get-started?tabs=commit-to-git)
