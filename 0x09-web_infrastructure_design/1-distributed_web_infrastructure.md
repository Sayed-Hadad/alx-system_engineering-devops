# 1. Distributed Web Infrastructure

![Distributed Web Infrastructure](images\1-distributed_web_infrastructure.png)

## Title Explanation:

- **For every additional element, why are you adding it?**
  Additional elements like load balancers, multiple servers, and database clusters are added to improve performance, reliability, and scalability. Load balancers distribute incoming traffic among multiple servers to prevent overloading and ensure high availability. Database clusters provide redundancy and fault tolerance, allowing for uninterrupted access to data even if one node fails.

- **What distribution algorithm your load balancer is configured with and how it works?**
  The load balancer is configured with a round-robin distribution algorithm, which evenly distributes incoming requests among the available servers in a sequential manner. This ensures that each server receives a fair share of traffic and prevents any single server from becoming overwhelmed.

- **Is your load balancer enabling an Active-Active or Active-Passive setup, explain the difference between both?**
  The load balancer enables an Active-Active setup, where all servers actively handle incoming requests simultaneously. In contrast, an Active-Passive setup involves one server actively serving traffic while the others remain on standby, only becoming active if the primary server fails. Active-Active setups typically offer better resource utilization and scalability.

- **How a database Primary-Replica (Master-Slave) cluster works?**
  In a Primary-Replica cluster, also known as a Master-Slave setup, the primary node (master) accepts write operations and replicates data changes to the replica nodes (slaves). The replica nodes synchronize their data with the primary node, ensuring consistency across the cluster. If the primary node fails, one of the replica nodes can be promoted to become the new primary node, maintaining database availability.

- **What is the difference between the Primary node and the Replica node in regard to the application?**
  The primary node handles write operations and serves as the authoritative source of data, while replica nodes primarily handle read operations and serve as backups. In regard to the application, the primary node is responsible for processing user requests that involve data modifications (e.g., insert, update, delete), while replica nodes serve read-only requests to retrieve data.

## Title: Issues with Distributed Web Infrastructure:

- **Where are SPOF?**
  Single points of failure can still exist, such as in the load balancer or the primary node of the database cluster. If any of these components fail, it can disrupt service availability.

- **Security issues (no firewall, no HTTPS):**
  Without proper security measures like firewalls and HTTPS encryption, the infrastructure is vulnerable to attacks such as DDoS, data breaches, and man-in-the-middle attacks, compromising data integrity and user privacy.

- **No monitoring:**
  Lack of monitoring tools and practices makes it challenging to identify and address performance issues, security threats, and system failures in real-time, leading to potential downtime and service disruptions.
