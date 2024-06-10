_Microsoft Fabric is an end-to-end data analytics SaaS solution. It brings many workloads in the analytics area, including Data Integration, Warehousing, Engineering, Business Intelligence, Data Science, and Real-time Analytics._

# Plan, Manage, and Implement a Solution

## Batch 5

### Question 1

You have purchased a P1 / F64 on a reserved basis. The capacity needs to run at least 18 hours per day. You want to protect yourself (avoid being throttled) in the event of over utilising capacity. Which of the following options would be the most cost effective and practical?

Utilise autoscaling with a preset cost limit.

[Reading](https://learn.microsoft.com/en-us/power-bi/enterprise/service-premium-auto-scale)

### Question 2

While examining a workspace, you notice the workspace has a state of 'Ophaned'. What does this mean?

1. The workspace has been deleted but not physically removed yet
2. The workspace has been deleted and physically removed but it remains visible for seven days
3. The workspace is not available
4. The workspace has no admin user **<-ANS** (A workspace with no admin user. You need to assign an admin)

[Reading](https://learn.microsoft.com/en-us/fabric/admin/portal-workspaces)

### Question 3

You want to see a downstream item for a particular object in a workspace, whether or not the downstram object is in the same workspace or not. Which of the following will allow you to see this?

1. Impact analysis view  **<-ANS** (lineage view doesn't show downstream items in different workspaces)
2. Lineage view 
3. Downstream analysis view
4. All of these

[Reading](https://learn.microsoft.com/en-us/fabric/governance/lineage)

### Question 4

When using a `Gateway` which protocol must be used?

1. TCPIP
2. UDP
3. TCP **<-ANS**
4. TDS

[Reading](https://learn.microsoft.com/en-us/fabric/data-factory/gateway-considerations-output-destinations)

### Question 5

Which of the following statements about managing users in Fabric is correct?

1. Managing users is done directly in Microsoft Fabric Admin portal
2. Managing users is done directly in Microsoft 365 portal **<-ANS**
3. Both 1 and 2 are correct
4. Neither 1 or 2 are correct

[Reading](https://learn.microsoft.com/en-us/fabric/admin/service-admin-portal-users)
