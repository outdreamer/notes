
    meteringmarketplace: submit usage data for custom usage dimensions for AWS marketplace sellers
    elastic-transcoder: processes pipeline jobs in insertion order, creating files for sequential interim formats

    - performance
        - braket: execute code with quantum processor
        - globalaccelerator: create accelerators to improve availability/performance of apps for local/global users
        - batch: organize similar jobs

    - other hardware (iot, satellite)
        - greengrass: extends AWS to iot devices to act locally on generated data, while using cloud for management/analytics/durable storage
        - groundstation: control & scale satellite communications/data

    - app
        appconfig: create/manage/deploy app config, with feature toggle, prod traffic testing, paid subscriber content access, & reduce impact of attacks
        application-autoscaling/insights: developer service to auto-scale AWS services other than EC2
        appmesh: monitor/control communications across microservices apps on AWS
        appstream: non-persistent app/desktop streaming service, run on optimized VMs & with streaming sessions adjusted to network conditions
        amplify: develop/deploy cloud-powered mobile/web apps
        mobile: structure/package/manage/configure desktop projects to bootstrap mobile AWS projects
        app features
            - ivs (Interactive Video Service): add live/interactive video in their mobile/web apps
            - mediaconnect/convert/live/package/package-vod/mediastore/data/mediatailor: convert/access media like video data
            - lex-models/runtime: building chatbot voice & text interfaces
            - e-commerce
                - marketplace-catalog/entitlement/commerceanalytics: list/describe/update products/offers in your catalog
            - search
                - kendra: search service using ML to enable search of content distributed across multiple locations/repositories
                - es (Elasticsearch Configuration): create, configure, and manage Elasticsearch domains
            - dependency detection
                discovery (Application Discovery Service): automatically identifies servers, VMs, & network dependencies in on-premises data centers
            - license-manager: streamlines the process of bringing software vendor licenses to the cloud
            - messaging
                - mq: message broker service for Apache ActiveMQ/RabbitMQ to set up/operate message brokers, allowing apps to communicate

    - cloud
        cloudsearch/domain: service to set up/manage/scale a search solution for a website/app, with highlighting, autocomplete, & geospatial search
        cloudtrail
            - a specially designed tool for logging/tracking API calls (account-level)
            - integrates with SNS to get notifications for api call patterns
            - helps to audit all S3 bucket accesses
            - find out who changed config
        - CloudWatch: 
            - allows administrators to view & collect metrics and set a notification alarms
            - monitor app status of AWS services & custom events, like
                State changes in EC2
                Auto-scaling lifecycle events
                Scheduled events
                AWS API calls
                Console sign-in events
            - ServiceLens
            - synthetics
                - continually monitor your services with canary scripts to monitor endpoints/APIs & check availability/latency, load time data, UI screenshots, logs, metrics, integrating with serviceLens
        CloudFormation
            - provisions & describes infrastructure resources in your environment
            - supports infrastructure needs of various app types, like legacy & enterprise aps
            - template components
                parameters
                data tables
                template version
                resources
                conditions
                outputs
    - Code Automation 
        - Honeycode: no-code app building tool
        - CodePipeline (jenkins): end-to-end dev lifecycle (includes CodeCommit, CodeBuild, CodeDeploy)
            - CodeCommit (git): store source code or artifacts
            - CodeBuild (maven): runs Install, Pre-build, Build & Post-build tasks, including tests, and stores build artifacts in s3
            - CodeDeploy (deploy to environments): deploys build artifacts from S3 to environments, including script-injection hooks like before/after install 
        codeguru-reviewer/profiler: dev tool using ML to provide recommendations for improving code quality & identifying expensive code, detecting deviations from best practices, like missing pagination/validation/error handling
        codestar/connections/notifications: develop, build, & deploy apps, managing the dev pipeline from jira task to code commit deployment
        serverlessrepo (Serverless Application Repository): 
            - quickly find/deploy serverless applications (like web/mobile backends, data processing apps, chatbots, or applications by name/publisher/event source)
   
    opsworks/cm (OpsWorks Stacks): app management service with an integrated experience for overseeing the complete app lifecycle
        - configuration management service for managing instances of Chef & Puppet (automation platforms for coding server config automation)
        - allows use of Chef/Puppet to automate how servers are configured/deployed/managed across your Amazon EC2/on-premises environments

    customer
        connect/participant: call center services
        pinpoint/email/sms-voice: outbound/inbound marketing communications/campaign service (email, SMS, push, voice)

    networking
        route53: A DNS web service
            - provides high availability & low latency with optimal anycast network & local routing to Globally Distributed Servers

        networkmanager (Transit Gateway Network Manager): create a global network to monitor AWS/on-premises networks built around transit gateways
        elb/v2: load-balancing service
        apigateway/v2/managementapi: gateway-building service
        fms (Firewall Manager)

    logging
        history
        logs
        
    troubleshooting
        support: manage support ticket metadata
        xray: APIs for managing debug traces
        sns (Simple Notification Service): push real-time notification messages to subscribers over multiple delivery protocols

    cost
        budgets
        autoscaling/plans
        pricing: Price List Service: query for services, products, & pricing information
        savingsplans: offer lower prices for guaranteed usage
        service-quotas: manage quotas (maximum values for a resource, item, or operation)
        servicecatalog: create/manage catalogs of approved AWS services (VM images, servers, software, & databases)
        appregistry/servicediscovery
        - ce: cost explorer
        - compute-optimizer: analyzes the configuration/utilization metrics of your AWS resources, generates optimization recommendations
        - cur (Cost & Usage Report): api for cost data

    storage
        - organization
            ds (Directory Service): service to setup/run/connect directories
            clouddirectory: build directories for organizing hierarchies of data along multiple dimensions
        - access frequency
            - dax: managed caching service for Amazon DynamoDB, by caching frequently-accessed data 
            - glacier: data archiving
        - hosting
            - chime: host a real-time audio/video conferencing application
        - backup
        - s3:
            - uses secure HMAC-SHA1 authentication keys
            - default storage class: Standard frequently accessed
            - Storage classes available with Amazon s3 are:
                Amazon S3 standard
                Amazon S3 standard-infrequent Access
                Amazon S3 Reduced Redundancy Storage
                Amazon Glacier
        - storagegateway: connects an on-premises software appliance with cloud-based storage
        - sqs (Simple Queue Service): 
            - hosted queue for interim message storage as they travel between applications/microservices
            - distributed queuing service that mediates between controllers
        - efs (Elastic File System)
        - fsx: service to launch/use shared file storage
        - Elastic Block Store (EBS): offers persistent storage volumes that attach to EC2 to persist data past the lifespan of a single Amazon EC2 instance
        - Amazon ElasticCache: in-memory data store service which makes it easy to deploy/scale/store data in the cloud 
    
    computing
        - elastic beanstalk
            - provides an environment to deploy & run apps in the cloud, and manage app lifecycles

        - lightsail

        - ec2 (Elastic Compute Cloud)
            - provides on-demand computing resources for hosting applications, useful in case of unpredictable workloads
            - AMI (Amazon Machine Image): a template of info (OS, application server, & applications) required to launch an instance
                - A template for the root volume for the instance
                - Launch permissions determining which AWS accounts can use the AMI
                - A block device mapping determining volumes to attach to the instance once launched
            - Launch Config
            - EC2 instance: a copy of the AMI running as a virtual server in the cloud
                - EC2 can run containers with server-level control
                - key pairs enable ssh to virtual servers using public/private key 
            - imagebuilder: build AMIs

    - containers
        - Elastic Container Registry (ECR): Store, encrypt, and manage container images
        - Elastic Container Serivce (ECS): Run containerized apps or build microservices
            - deploy, manage, & scale containerized apps using Kubernetes
        - Elastic Kubernetes Service (EKS): Manage containers with Kubernetes
        - Fargate: Run containers without managing servers
        - EC2: Run containers with server-level control
        - App2Container: Containerize & migrate existing applications
        - Copilot: Quickly launch and manage containerized applications

    - security
        - cloud9: IDE to write/run/debug your code with a browser, including a debugger/terminal
        - cloudhsm/v2 (hardware security model): generate/use encryption keys as a custom key store for KMS
        - devicefarm: test web apps on desktop browsers using Selenium, & on physical devices
        - health: resource health monitor to identify accounts affected by events or identify security vulnerabilities
        - GuardDuty: security monitoring service analyzes/processes data sources about account usage, identifying unexpected/unauthorized/malicious activity, monitoring for signs of compromise (escalations of privileges, uses of exposed credentials, communication with malicious entities, detecting compromised sensitive resources like unauthorized access/usage or unusual API calls given the implied intent)
        - acm/pca (certificate manager): allows creating, storing, & renewing public/private SSL/TLS X.509 certificates/keys to protect websites & apps
        - inspector: security assessment service that generates reports, prioritizing vulnerabilities according to severity, identifying exposure/vulnerabilities/deviations from best practices
        - kms: key management service
        - macie/2: discover sensitive information in AWS & use NLP to classify the data & provide insights
        - resource-groups/taggingapi
            - organize AWS resources such as EC2 instances, RDS databases, & S3 buckets into groups using criteria (like roles in infrastructure, lifecycle stages, regions, application layers) that you define as tags
            - automate management tasks, such as those in AWS Systems Manager Automation documents, on tag resources in AWS Systems Manager
            - quickly view a custom console in AWS Systems Manager with AWS Config compliance & other monitoring data about tag resources
        - Virtual Private Cloud - VPC
            - configure networking, through customization of an isolated network
            - includes IP address range, internet gateways, subnet & security groups. 
            - subnet: a section of IP Addresses
                - public
                - private
            - Security Groups: acts as a firewall for EC2 instances, controlling inbound/outbound traffic at the instance level
            - Network ACLs: acts as a firewall for subnets, controlling inbound/outbound traffic at the subnet level
            - Flow logs - These capture the inbound and outbound traffic from the network interfaces in your VPC
            - VPC does not support broadcast/multicast
        - IAM
            - provides enhanced security and identity management for your AWS account
            - role: provides permissions to entities which you can trust within your AWS account, similar to users but doesnt require creating any username/password to work with the resources
        identitystore
        guardduty
        frauddetector
        detective
        accessanalyzer
        cognito-identity/idp/sync
            - add user sign-up, sign-in, & ACL to your web/mobile apps quickly & easily
        secretsmanager: store, manage, and retrieve, secrets
        ram (Resource Access Manager): share resources across accounts
        organizations: 
            - AWS accounts: boundaries for permission, security, costs, and workloads
            - group AWS accounts into organizational units (OUs) for a single app/service
        
        outposts: 
            - extends AWS infrastructure, APIs, & tools to customer premises
            - build & run apps on premises like in AWS Regions, while using local compute & storage resources for lower latency & local data processing needs
        
        sso/admin/oidc (OpenID Connect): manage user access to AWS & third party SaaS & SAML-supporting SSO resources (such as user portal or applications), assigning applications/roles to users, who can get federated into applications
        sts (Security Token Service): request temporary, limited-privilege credentials for IAM users or federated users you authenticate
        cloudfront
            - speeds up transfer of your static/dynamic web content (HTML files, IMAGE files), delivering through worldwide data centers named Edge Locations
            - Geo-restriction feature helps prevent users of specific locations from accessing content distributed through a CloudFront web distribution
        waf/regional/v2: 
            - web application firewall to monitor HTTP/HTTPS requests forwarded to Amazon Gateway REST API, CloudFront distribution, AppSync GraphQL API, or Application Load Balancer
            - allows rules, rule groups, request metric logging, request samples, reusable rules
            - CloudFront/API Gateway/ALB/AppSync responds to requests with requested content or an HTTP 403 status code, based on conditions like:
                IP addresses that requests originate from.
                Country that requests originate from.
                Values in request headers.
                Strings that appear in requests, either specific strings or string that match regular expression (regex) patterns.
                Length of requests.
                Presence of SQL code that is likely to be malicious (known as SQL injection).
                Presence of a script that is likely to be malicious (known as cross-site scripting).
        shield: uses web ACLs to minimize DDoS attack effects
        securityhub: view of security/readiness/compliance state of your AWS environment/resources, analyzing security trends to identify highest priority security issues
        cloudMap: configure public DNS, private DNS, or HTTP namespaces that your microservice applications run in
            - automatically creates DNS records & an optional health check for public/private DNS namespaces
            - can auto-register service instances with CloudMap API
            - Clients submitting public/private DNS queries/HTTP requests for the microservice registered with CloudMap receive an answer with up to eight healthy records

    data
        appsync: streamlines use of GraphQL by handling secure data source connections, managing adding caches for performance, subscriptions for real-time updates, & client-side offline data store syncing
        dlm (Data Lifecycle Manager): manage lifecycle of AWS resources, creating lifecycle policies to automate operations on resources
        dms (Database Migration Service): migrate data to/from databases, supporting homogeneous/heterogeneous migrations, using object mapping to restructure original data to the desired structure of the data in DynamoDB during migration
        db
            rds: 
                - allows setting up, operating, & scaling a relational db, providing auto-backups, scaling, & config management
                - asynchronous (applies commands at times like at command call time, boot time, or during maintenance)
                - MySQL, MariaDB, PostgreSQL, Microsoft SQL Server, Oracle, or Aurora db server
                - automatic maintenance scheduling is done only for patches that are related to security and durability
                - default window is a 30-minute value & the DB instance will still be available during these events, though you might observe a minimal effect on performance
                - pi (Performance Insights): monitor & explore database load, based on data from a running RDS instance
            neptune: graph database
            sdb: 
                - providing the core database functions of data indexing and querying in the cloud
                - requiring no schema, automatically indexing data & providing a simple API for storage/access, allowing instant scaling
                - eliminates need for data modeling, index maintenance, & performance tuning
            timestream-query/write: operations for AWS time series database
            docdb
            Aurora
            dynamodb/streams
                - supports GET/PUT operations with a user-defined primary key
                - provides flexible querying on non-primary vital attributes using global/local secondary indexes
                - low latency
            qldb/session: a ledger database that provides a transparent, immutable, and cryptographically verifiable transaction log ‎owned by a central trusted authority
            managedblockchain

        - Analytics
            - Athena: Interactive analytics
            - EMR (Elastic MapReduce): Big data processing in data lakes
            - Redshift: data warehouse
                - Running SQL & complex, analytic queries against structured/unstructured data in data warehouse/lake, without unnecessary data movement
                - allows allocating capacity, monitoring & backing up cluster
            - Kinesis: Real-time analytics
            - Elasticsearch Service: Operational analytics
                - search/explore/filter/aggregate/visualize data in near real time for application monitoring, log analytics, & clickstream analytics
            - Quicksight: dashboards/visualizations

        - Data movement
            - Real-time data movement
                - kafka/Managed Streaming for Apache Kafka (MSK)
                - Kinesis Data/Video Streams/Firehose/Analytics
                    - firehose: real-time streaming data into S3, ELK, Redshift, splunk
            - MSK/Kinesis:
                - collect/process/analyze streaming data
                - load data streams into data lakes/stores/analytics services for real time responses
        - Glue: ETL (extract/transform/load) service for managing/executing etl workflows for processes like sanitization/normalization, providing a catalog of all data sets
        
            - Glue DataBrew: simplifies data preparation tasks, identifying known data issues, visualizing data & performing one-click data transformations, using ML to improve transforms/processing & identify issues & creating data dependency/flow graphs

        - Data lake
            - Object storage: S3, Lake Formation
            - Backup and archive: S3 Glacier, Backup
            - Data catalog: Glue, Lake Formation
            - Third-party data: Data Exchange

        - Predictive analytics & machine learning
            - Frameworks & interfaces: AWS Deep Learning AMIs
            - Platform services: Amazon SageMaker: build and train Machine Learning models

        - data transfer
            - appflow: transfer data between SaaS apps (Salesforce) & AWS services (S3)
            - Transfer Acceleration Service: speeds up your data transfer & CDN with optimized network paths
            - directconnect: transfer objects from your data center, when using Amazon CloudFront
            importexport
            transfer: enables the transfer of files over FTP, FTPS, SFTP into/out of S3 
            snowball: 
                - petabyte-scale data transport service using secure devices to transfer big data between your on-premises data centers & S3
                - a big data transport option to reduce networking/transport costs into/out of AWS
            dataexchange: 
                - create/update/manage/access file-based data set, accessible with granted entitlements & subscriptions
                - download/copy entitled data sets to Amazon S3
                - create/manage data sets to publish to a product
                - assets in Data Exchange are pieces of data that can be stored as an Amazon S3 object
                - jobs are asynchronous import or export operations used to create or copy assets
            datasync: managed data transfer service to automate moving data between on-premises storage & S3/EFS

        - datapipeline: 
            - configures/manages a data-driven workflow
            - handles the details of scheduling and ensuring that data dependencies are met
            - create a pipeline and define data sources, schedules, dependencies, and the transforms to be performed on the data
            - execute the default/custom task runner application to receive the next task ready for processing
            - AWS Data Pipeline Task Runner provides logic for common data management scenarios, such as performing database queries and running data analysis with EMR

    ml
        machinelearning: manage/create ml models using limited params & data processing recipes
        mturk: accessing human researchers or consultants to help solve problems on a contractual or temporary basis
        elastic-inference: helps choose instance type best suited to compute/memory needs of your training app
        comprehend/medical: document classification & entity recognizer service
        personalize/events/runtime: machine learning service that makes it easy to add individualized recommendations to customers
        forecast: uses machine learning to make predictions, automatically examining data, identifying what is meaningful, & producing a prediction model
            - provides expected accuracy to determine if more data is required
            - using associated data outside of data set
        rekognition: object classification in image/video 
    
    integration
        schemas: EventBridge Schema Registry
            - example: send load volume alerts from Datadog to EventBridge to trigger an AWS Lambda function that scales your EC2 instances to handle the expected load increase
        EventBridge: serverless event bus to connect apps with data from your apps, integrated SaaS apps, & AWS services
            - delivers a stream of real-time data from event sources (Zendesk, Datadog, or Pagerduty)
            - resources state changes auto-send events to event streams, processed by configurable routing rules to move data to handling targets

    ses/v2 (Simple Email Service): send/receive email with your own domains/addresses, using RESTFUL API call or regular SMTP
    
    migration
        sms (Server Migration Service): migrate workflows to AWS
        mgh/migrationhub-config

    config management
        ssm (Systems Manager): collecting system inventory, applying operating system (OS) patches, automating AMI creation, configuring OSs/applications at scale, remotely/securely manage instance configuration of EC2 or on-premise servers/VMs
            - includes appconfig
        configservice
        configure
        config: 
            - track configuration changes in your environment, including configuration history, configuration change notification, & relationships between AWS resources
            - records point-in-time configuration details for your AWS resources as Configuration Items (CIs) to track resource state at a time
            - can aggregate data across accounts

    logical units
        lambda: a compute service to run code in AWS Cloud without managing servers
        stepfunctions: build applications from components with visual workflows, logging state & retrying failed operations
        swf - Simple Workflow Service: using task workflows, managing intertask dependencies, scheduling, and concurrency of component tasks
    
    text operations
        speech to text
            transcribe: transcribing speech to text
            polly: web service that makes it easy to synthesize speech from text
        textract: detects & analyzes text in documents, converts it into machine-readable text
        translate: translate text between languages

    workdocs: API for file migration to AWS, plus security, backups, & analytics
    worklink: secure internal mobile site/app access without storing any internal web content on mobile devices
    workmail/messageflow: secure third-party email client service management
    workspaces: provision virtual, cloud-based Microsoft Windows and Amazon Linux desktops

