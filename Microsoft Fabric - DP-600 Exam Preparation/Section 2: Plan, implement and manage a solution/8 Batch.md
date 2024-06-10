_Microsoft Fabric is an end-to-end data analytics SaaS solution. It brings many workloads in the analytics area, including Data Integration, Warehousing, Engineering, Business Intelligence, Data Science, and Real-time Analytics._

# Plan, Manage, and Implement a Solution

## Batch 8

### Question 1

You want to give a co-worker permissions to create, update and delete a workspace. So you put your co-worker in an Admin role. Will this accomplish your goal?

No. The ability to create a workspace is not dependent upon a workspace role. The person must be in a security group that is assigned to the `Create Workspaces` activity in `Tenant Settings` in the `Admin Portal`.

[Reading](https://learn.microsoft.com/en-us/fabric/get-started/roles-workspaces	)

### Question 2

You want to connect (or disconnect) a workspace tied to a capacity to an Azure repository for source control. Which of the following roles are able to do this?

1. Capacity admin
2. Power BI admin <- **ANS**
3. Workspace admin <- **ANS**
4. Any user with Contributor permissions

Only a workspace admin can connect a workspace to an Azure Repo, but once connected, anyone with permission can work in the workspace.

[Reading](https://learn.microsoft.com/en-us/fabric/cicd/git-integration/git-get-started?tabs=commit-to-git)

### Question 3

When a `Sensitivity Label` is applied to data in Power BI, when does the actual encryption of data occur?

1. When the data is viewed in Power BI report in the Power BI service
2. When the data is viewed in Power BI desktop
3. When data is queried via a DAX expression
4. When the data leaves the service such as when exporting to Excel <- **ANS**

The only time encryption occurs is when the data leaves the service.

[Reading #1](https://learn.microsoft.com/en-us/fabric/get-started/apply-sensitivity-labels)
[Reading #2](https://learn.microsoft.com/en-us/power-bi/enterprise/service-security-sensitivity-label-overview)

### Question 4

Your company is migrating Power BI reporting to Fabric and needs to ensure access controls for individual users.

Which of the following approaches best accomplishes this?

1. Utilise Azure Active Directory (AAD) groups and map them to Fabric workspace roles <- **ANS**
2. Develop a custom Power BI extension for managing user access within Fabric
3. Migrate user accounts directly from the existing platform to Fabric, including access settings
4. Manually recreate user permissions for each report within Fabric workspaces

### Question 5

Which of the following are false about a Power BI Project (PBIP) file?

1. They can be created from the Power BI Desktop
2. They can be created from the Power BI Service <- **ANS**
3. Any text editor can modify the contents of a PBIP file
4. Sensitivity labels are supported in PBIP files <- **ANS**
5. A .pbix file can be saved as a PBIP and a PBIP file can be saved as a .pbix

[Reading](https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-overview)
