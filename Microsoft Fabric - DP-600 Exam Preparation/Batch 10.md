_Microsoft Fabric is an end-to-end data analytics SaaS solution. It brings many workloads in the analytics area, including Data Integration, Warehousing, Engineering, Business Intelligence, Data Science, and Real-time Analytics._

# Plan, Manage, and Implement a Solution

## Batch 10

### Question 1

How can a single point of failure be avoided when using a data gateway?

1. Implement a data gateway cluster <-- **ANS**
2. Increase the gatewat's processing power?
3. Use a virtual private network (VPN)
4. Schedule regular backups

[Reading](https://learn.microsoft.com/en-us/fabric/data-factory/how-to-access-on-premises-data)

### Question 2

Which of the following roles can access a workspace's lineage view?

1. Administrator <-- **ANS**
2. Contributor <-- **ANS**
3. Member <-- **ANS**
4. Viewer <-- **ANS**
5. 1, 2 and 3 only

Any user with a role in a workspace can access that workspace's lineage view. However, users with the Viewer role won't see data sources.

[Reading](https://learn.microsoft.com/en-us/fabric/governance/lineage)

### Question 3

Which of the following semantic model properties are copied from one pipeline stage to another when a deployment is done.

1. Role assignments
2. Refresh schedules
3. Credentials
4. Endorsements
5. None of these <-- **ANS**
6. All of these

[Reading](https://learn.microsoft.com/en-us/fabric/cicd/deployment-pipelines/understand-the-deployment-process)

### Question 4

When a workspace is deleted, it can be restored up to a certain number of days. This is known as the retention period. Where can this be changed?

1. Microsoft 365 Portal
2. Microsoft Fabric Admin Portal <-- **ANS**
3. Workspace Setting Panel
4. PowerShell Only

During the retention period, a `Microsoft Fabric administrator` can restore the workspace.

[Reading](https://learn.microsoft.com/en-us/fabric/admin/portal-workspaces)

### Question 5

You want to allow an analyst to see a workspace's lineage view along with all the data sources. You assign the analyst a Viewer role in the workspace. Will this accomplish your goal.

No. Veiwer role means you cannot see the data sources in lineage view.

[Reading](https://learn.microsoft.com/en-us/fabric/governance/lineage)