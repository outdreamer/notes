# terms
	- software/data/platform/infrastructure as service/code/config

AWS security

    - Use AWS identity and access management to control access to your AWS resources
    - Restrict access by allowing only trusted hosts or networks to access ports on your instance
    - Review the rules in your security groups regularly
    - Only open up permissions that you require
    - Disable password-based login, for example, launched from your AMI
    - use Shielf, WAF, Route53, CloudFront, ELB, and VPC to protect against DDos

AWS limits
	- 100 buckets in each of your AWS accounts
	- VPC 
		- enables hybrid cloud (site-to-site VPN)
		- cant establish a Peering connection to a VPC in a different region
		- can connect your VPC with a VPC owned by another AWS account
		- EC2 instance inside your VPC can connect with the EC2 instance belonging to other VPCs
		- 200 subnets per VPC
		- 20 EC2 Instances in a vpc
		- maximum VPC size is 65,536 instances
		- 5 VPC Elastic IP addresses are allowed for each AWS account
		- cannot ping the router or default gateway that connects your subnets
		- EBS snapshots need to be in same region as VPC 
		- no peering connections to VPCs in different regions
		- database servers should be launched into a private subnet if one is available in that VPC
		- link on-premise to cloud by establishing a VPN connection between your company & Amazon VPC.
	- EBS can be attached to any running instance that is in the same Availability Zone
	- can switch from EBS to instance based storage at specific times
	- NAT gateways are limited in bandwidth to 45 gbps
	- Internet gateway is needed to use VPC (virtual private cloud peering) connections
		- IG is horizontally scaled, redundant & highly available, usually without Bandwidth constraints
	- route table:
		- route the network packets
		- one route table would be available in each subnet
		- multiple subnets can be attached

	- Connection Draining in ELB pulls all the traffic from that particular failed instance and re-route the traffic to other healthy instances

	- When a DB instance is deleted, RDS deletes automated backups & retains user & manually created DB snapshots
	- Elastic IP address stays with the instance as long as the user doesn’t manually detach it (just like private ip), vs a public IP which is removed on stop/termination
	- cannot connect an EBS volume to multiple instances (but an instance can have multiple volumes)
	- select provisioned IOPS storage over standard RDS storage to perform batch-related workloads
	- terminating an instance permanently deletes the attached EBS volumes 
	- AWS services that are not region-specific: IAM, Route 53, WAF, CloudFront
	- When your instances are spread across regions you need to create key pair in each region

	- common errors

		- exceed your limit of Elastic IP addresses

		- VPC is not resolving the server through DNS: enable DNS hostname resolution

        - ec2 connection issues:
            Connection timed out
            User key not recognized by the server
           	Host key not found, permission denied
            An unprotected private key file
            Server refused our key
            No supported authentication method available
            Error using RDP Client

# tasks

	- keep your standby RDS service in a different Availability Zone to avoid failure

	- manage access with IAM:
	    Create & manage IAM users/groups
	    Manage user security credentials
	    Create & manage policies to grant access to AWS services/resources

	- use WAF: control the traffic flow to your applications, create custom rules that block common attack patterns (using allow/prevent/count all requests for a policy) 

	- automate EC2 backup using EBS: create snapshots of EBS volumes on S3, assign a retention period of the snapshot, remove snapshots older than retention period

	- auto-delete old snapshots: use AWS Ops Automator to create/copy/delete EBS snapshots automatically

	- transfer vast amounts of data
		- AWS Snowball is a data transport solution for moving high volumes of data into/out of an AWS region
		- AWS Snowball Edge adds additional computing functions
		- snowmobile: is an exabyte-scale migration service that allows you to transfer data up to 100 PB.

	- add an existing instance to a new Auto Scaling group
		- EC2 -> instance -> Actions -> Instance Settings -> Attach to Auto Scaling Group

    - auto-scaling advantages:
        - fault tolerance
        - availability
        - cost management
    
    - Lifecycle hooks are used for autoscaling to put a wait time to insert logic to a scale in/out event

	- provide secure communication between sites using the AWS VPN CloudHub, if you have multiple VPN connections

    - Vertical scaling of EC2 instance:
        1. Spin up a new larger instance than the one you are currently running
        2. Stop new instance and detach its root volume, and discard
        3. Then stop your live instance and detach its root volume
        4. Note the unique device ID & attach the associated root volume to the new server
        5. Start new server again

	- recover/login to an EC2 instance with missing key
	    Verify that EC2Config service is running
	    Stop original instance
	    Detach instance root volume
	    Attach the volume to a temporary instance
	    Modify the configuration file
	    Re-attach volume to original instance
	    Restart original instance

	- configure CloudWatch to recover an EC2 instance
		- Create an Alarm in CloudWatch
	    - go to Define Alarm -> Actions tab
	    - Choose Recover this instance option

	- grant access to a s3 bucket by attaching a policy to the IAM user or adjusting s3 bucket access policy

	- find config state at a certain time: config (configuration items)

	- use VPC to allocate various private & public IP addresses to make them communicate with the internet and other instances

	- build VPC with components: 
		- Subnet
		- Route (and Route table)
		- Gateways:
			- Internet (or Egress-only)
			- NAT (NAT gateway, or an Ec2 configured as a nat)
			- Virtual Private 
			- Customer
		- Connections:
			- HW VPN 
			- EndPoints
			- Peering Connections
		- Endpoint: S3

		- attributes
			- CIDR Block: allowed private ip range
			- DNS Support / Hostnames:  
				- allow DNS hostnames to be automatically assigned to the EC2 instances in the VPC
				- provides a name to reach our EC2 instances, rather than just an IP address
			- if your VPC needs to connect to the internet, add InternetGatway & GatewayAttachment
			- subnet
				- cidr block 
				- availability zone
			- Routing tables define which destinations subnet traffic can be routed to
				- subnets are only "public" or "private" based on associated routing tables
				- route table attributes:
					- vpc id
				- route attributes:
					- gateway id
					- route table id
      				- DestinationCidrBlock: 0.0.0.0/0
      				- NatGatewayId: (for a private subnet route)

      		- now you can launch an EC2 instance with a public IP address in one of these subnets, and it will be reachable from the public internet
		
		- use a NAT gateway: to prevent public internet from reaching instances in private subnets, & allow instances to make outbound connections like downloads without public IP addresses
			- the nat has public IP address & is associated with a public subnet, so private instances in private subnets can use the nat to initiate outbound connections, but the NAT will not allow a party on the public internet to use the NAT to connect to our private instances
			- associate nat gateway with a public subnets and a fixed public ip address (allocation id)
		- associate subnets with route tables using SubnetRouteTableAssociation resource

# comparisons

	- security group vs. ACL
		- Security Group: defines traffic allowed TO or FROM EC2 instance
		- NACL: controls traffic TO or FROM a Subnets

	- RDS vs. dynamo
		- rds is meant for structured data only
		- DynamoDB is meant for unstructured data which is a NoSQL service

	- vertical vs. horizontal scaling
		- Vertical scaling lets you vertically scale up your master database with one click
		- horizontal scaling is good for replicas. These are read-only replicas, done through Amazon Aurora.

	- NAT Gateways & Instances have:
		- the same:
			- function
			- high availability 
			- cost-dependence on count & usage duration/amount
		- they differ in that:
			- NAT gateways are managed by AWS, have better performance, & limited bandwidth
			- NAT instances can have assigned security groups, configurable size/load, variable bandwidth by instance, and cost is dependent on instance type

	- S3 vs. EBS
		- s3 uses a fast object store with redundancy across data centers using public/private key
		- ebs is a very fast filesystem store that can only be used with ec2 and only has redundancy within a data center

	- regions vs. availability zones
		- AWS regions (us-east-1) are geographical areas
		- availability zones (us-east-1a) are areas inside the regions - isolated zones that can replicate themselves as required
			- linked thru low-latency links

	- data warehouse vs. lake

		- data warehouse: database optimized for relational data from transactional systems & LOB apps, with data structure/schema defined in advance for fast SQL queries

			- supports data: Relational from transactional systems, operational db's, & line of business apps 	
			- schema design time: Designed prior to the DW implementation (schema-on-write) 							
			- performance: Fastest query results using higher cost storage 	
			- data quality: Highly curated data that serves as the central version of the truth 	
			- used by: Business analysts 	
			- used for: Batch reporting, BI and visualizations 

		- data lake: stores all your relational & non-relational data in one centralized repository at any scale, with data structure not defined at import time (like with clustering & other unsupervised ml methods), for SQL queries, big data analytics, full text search, real-time analytics, & machine learning

			- supports data: Non-relational/relational from IoT devices, web sites, mobile apps, social media, & corporate apps
			- schema design time: Written at the time of analysis (schema-on-read)
			- performance: Query results getting faster using low-cost storage
			- data quality: Any data that may or may not be curated (ie. raw data)
			- used by: Data scientists, Data developers, and Business analysts (using curated data)
			- used for: Machine Learning, Predictive analytics, data discovery and profiling

	- CloudFormation vs. Elastic Beanstalk

    	- CloudFormation:
    		- provisions & describes infrastructure resources in your environment
    		- supports infrastructure needs of various app types, like legacy & enterprise aps
    	- Elastic Beanstalk 
    		- provides an environment to deploy & run apps in the cloud
			- combined with dev tools to help manage app lifecycle

	- EBS vs. instance store

		- EBS: permanent encrypted storage in which the data can be restored at a later point, which stays even after the lifetime of the EC2 instance
		- Instance Store: temporary storage physically attached to a host machine, which you cannot detach from one instance & attach to another, and which is lost if any instance is stopped/terminated

	- IAM role vs. user

		- IAM role: defines permissions for requests
			- trusted entities (like IAM users, applications, or AWS services) assume roles
		- IAM user: has permanent long-term credentials, uses AWS services

	- Route 53 Latency Based Routing vs. Geo DNS

		- Geo Based DNS routing uses the geographic location of the request
			- used when you want to direct the customer to different websites based on their location
		- Latency Based Routing utilizes latency measurements between networks & AWS data centers
			- used when you want to give your customers the lowest latency possible

	- Domain vs. Hosted Zone

		- domain: describes an administrative/technical unit. For example, www.simplilearn.com is a domain and a general DNS concept.
		- hosted zone: describes how to route traffic for a domain. For example, lms.simplilearn.com is a hosted zone.

# types
	
	- elb types: 
		- network: static IPs, TCP/UDP/TLS traffic with high volume/low latency/extreme performance requirements
		- gateway: third-party virtual networking appliances for security & network analytics
		- application: for flexible application management and TLS termination, routes HTTP and HTTPS traffic to targets in a VPC
		- classic: load balancing for resources built in the EC2 classic network

	- ec2 types
	    - On-demand Instance: cheap for a short time 
	    - Spot Instance: less expensive than on-demand, can be bought through bidding
	    - Reserved Instance: less expensive for long term

        - instance type: hardware of the virtual server (optimized for memory, computing, storage)
            - T2 instances: provide moderate baseline performance & capability to burst to higher performance
	
	- ami types
		- completeness
	    	- Fully Baked AMI
	    	- Just Enough Baked AMI (JeOS AMI)
	    	- Hybrid AMI

        - storage types
            Instance-store backed
            EBS backed

	- cloud layers:
	    Cloud controller
	    Cluster controller
	    Storage Controller
	    Node Controller

	- AWS virtualization types
	    - Hardware Virtual Machine (HVM): fully virtualized hardware, where all the virtual machines act separate from each other, where the VMs boot by executing a master boot record in the root block device of your image
	    - Paravirtualization (PV): GRUB is the bootloader that boots the PV AMIs. The PV-GRUB chain loads the kernel specified in the menu
	    - Paravirtualization on HVM: helps OS use storage & network I/O available through the host

    - dynamodb consistency model types
    	- Eventual Consistency Model: maximizes your read throughput but might not reflect the results of a recently completed write but usually corrects within a second
        - Strong Consistency Model: has a delay in writing the data, but guarantees that you will always see the updated data every time you read it 


# terms/tools

	- hypervisor: software that enables Virtualization, combining combines physical hardware resources in a platform delivered virtually to users. XEN is the Hypervisor for EC2.

	- IAM managed policies: permission sets that can be attached to users/groups/roles
		- effect/action/resource attributes of the policy statement

	- logging:
		- usage example: use Amazon CloudWatch Logs, store them in Amazon S3, move into ElasticSearch with Kinesis Firehose, & use Amazon Elastic Search to visualize them
		- AWS CloudTrail, AWS Config have account-level logging
    	- monitor VPC using CloudWatch logs & VPC Flow Logs

	- Geo-Targeting: show personalized content based on user location without changing the URL

	- buffer: used to synchronize components, and balance component request transmission & processing so they work at similar/faster speeds

	- IAAS-storage cloud service (DNS/ELB)

	- Edge location: 
		- location where data like images are redundantly cached, searched first when data is requested

	- RTO (Recovery Time Objective): maximum time you can wait for a recovery after an outage
	- RPO (Recovery Point Objective): maximum amount of data loss you can accept in time

	- NAT: Network Address Translation