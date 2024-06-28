C: Report for pharmaplus services outage on 25 october 2023 form 10:30 pm to 3:30am

Issue Summary
On the 25th october 2023 we encountered a critical issue which resulted in the order processing system of our online pharmacy to become unresponsive. This incident caused a complete halt in the service to process and update new and existing orders respectively. This resulted in a significant down time for the platform which lasted for approximately 5 hours from 10:30 pm to 3:30 am. This was caused by a flow in a new bulk order processing feature that caused excessive database locking.
Timeline
9:56:35 pm
The issue was detected at at 9:56 by one of our server monitoring systems and an alert was sent to the system administrator
10:00pm
At 10:00 pm the system admin :
.  Analyzed the system and application logs during the time period when the incident occurred
. Server Health: Monitored CPU, memory, and network usage of the service
.Code Review: Reviewed the recent code updates and deployments 
.Database: checked the overall health and performance of the database
The system admin resolved this issue by  

Root cause
Database Locking: A new feature  for bulk order processing created a flaw that caused excessive data locking which led to a high number of concurrent transactions for locks resulting  in timeout errors and failure to process order error.
Insufficient Testing: The new feature was not thoroughly tested under realistic load conditions which lead to deployment of bugged code.

The Problem was fixed by 
 .Rollback: The problematic deployment was rolled back to restore the order processing system to its original state.
Increased monitoring and alerts were implemented on the database server health, and server performance to quickly detect similar issues in the future.

Corrective and preventive measures

. Refactor and optimize the bulk order processing query to reduce locks and improve performance.
. Implement load testing procedures for new features so as to identify performance problems that could occur in case of an incredibly lard order.
. Enhance the code review process to include performance and scalability considerations for all features before deployment.

