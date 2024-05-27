_Microsoft Fabric is an end-to-end data analytics SaaS solution. It brings many workloads in the analytics area, including Data Integration, Warehousing, Engineering, Business Intelligence, Data Science, and Real-time Analytics._

# Plan, Manage, and Implement a Solution

## Batch 11

### Question 1

You are deploying content from one pipeline stage to another. Which of the following items can be copied to the target stage?

1. Dataflows <-- **ANS**
2. Datamarts <-- **ANS**
3. Lakehouses <-- **ANS**
4. Template App workspaces
5. Streaming dataflows

[Reading](https://learn.microsoft.com/en-us/fabric/cicd/deployment-pipelines/understand-the-deployment-process)

### Question 2

A user, in an organization that has a P1 capacity, does not have a Power BI Pro license or a Power BI Premium Per User License but wants to access the workspace.
Which of the following options would be best to grant the user the ability to do this?

1. Place workspace in a P1 capacity or higher
2. Place workspace in a P2 capacity or higher
3. Place workspace in a P3 capacity and the user must be in a Viewer role <-- **ANS**
4. The user must purchase a Pro or PPU license

[Reading](https://learn.microsoft.com/en-us/power-bi/collaborate-share/service-new-workspaces)

### Question 3

You want to share a lakehouse with a user who wants to use Apache Spark to access the data. You give the user `ReadData` permission on the endpoint. Will this accomplish your goal?

No. grant `ReadAll` permission on the lakehouse to access all data using Apache Spark.

[Reading](https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-sharing)

### Question 4

Which of the following is true with regards to Git integrations?

1. A workspace can only connect to one branch and folder at a time <-- **ANS**
2. A workspace can be connected to mutliple branches and folders at a time
3. A workspace can be connected to multiple branches and one folder at a time
4. A workspace can be connected to one branch and multiple folders at a time

[Reading](https://learn.microsoft.com/en-us/fabric/cicd/git-integration/git-get-started?tabs=commit-to-git)

### Question 5

You're designing a Fabric environment for an organisation with departments. They require unified data analytics across the organisation while ensuring each department can customise reports with their branding and preferred visuals.

Which approach would best enable custom Power BI report themes while maintaining consistency across the organisation?

1. Develop a single master theme in Fabric and enforce it across all departments and reports
2. Design a base theme in Fabric with customisable elements for each department <-- **ANS**
3. Implement Power BI theme json files for individual departments
4. Create individual themes for each department and allow full customisation