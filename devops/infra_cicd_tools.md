- Example CI/CD pipeline, starting from git commit hook:
		- Jenkins pulls code from repo with Git plugin
		- Jenkins builds it using tools like Ant/Maven
		- Config mgmt tools deploy/provision testing environment
		- Jenkins releases code on test environment
		- testing tools like selenium/docker conduct testing
		- Once code is tested, Jenkins sends it for deployment on prod server 
		- After deployment, tools like Nagios continuously monitor the deployed resources


- CICD: Terraform/Ansible, CICD pipeline, Jenkins

	- Terraform vs. ansible
		- both have plugin architecture
		- terraform:
			- declarative, good for defining requirements like target state
			- for orchestration & configing services/infra
			- oriented around maintaining a target state, adjusting resources as needed to maintain it
			- calculates current/desired state
			- deploy load balancers, vpc's, dns
			- terraform figures out steps after parsing config, whereas ansible requires explicit steps
			- different repair mechanism than ansible
			- helps integrating services from different providers

		- ansible: 
			- imperative/procedural (set of steps), good for importing existing config/install/admin scripts
			- for managing server config
			- maintains each component in a working state
			- less integrated analysis & lifecycle managemnt
			- agentless (dont have to manage agent) & serverless
			- supports modules for Windows/UNIX-like hosts, depends on SSH/PowerShell sessions for conducting the configuration tasks
			- inefficient at scaling & service orchestration
			- good for automation/migration/tracking/applying changes
			- repairs by prioritizing specialized fix rather than replacing whole infra
			- better for packaging/templating

	- Terraform: a tool for creating, changing, and versioning infrastructure with higher safety and efficiency
		- cross-platform
		- graphing features to visualize infrastructure
		- unified syntax allowing writing config once & storing it in one place
		- helps understand resource relationships
		- allows breaking down configuration into components to help with organization/maintenance
		- building/versioning/changing infra
		- use cases:
			- setting up demo environments
			- deploying on multiple cloud environments
			- resource scheduling
			- add infrastructure blueprints for sharing/re-use/streamlining
			- develop organized execution plans, before application
			- Change Automation, applying complex changesets 
			- scaling

		- features
			- callbacks
			- modules allow code compartmentalization for re-use, in a separate dir from root config dir
			- some providers allow on-premise infrastructure
			- supports github, gitlab, bucket
			- declarative coding tool
			- uses a high-level config language HCL to describe target “end-state” infrastructure
			- generates a plan for reaching target end-state
			- executes the plan to provision infrastructure
			- can manage instances/storage/networking, including DNS entries & SaaS features
			- can alter state without applying a plan change (like deleting a resource manually)
			- define environments as workspaces, can use the same config across envs if you include env as a variable
			- can provide variable values at runtime, using env var/command-line parameters
			- can import existing resources into terraform
			- can use remote terraform state as a data source

		- components:

			- Terraform Core: 
				- discovers/loads plugins, and utilizes remote procedure calls (RPCs) for communicating with Terraform Plugins
				- statically-compiled binary written in go
				- manages resource state, executes plans, communicates with plugins through rpc, constructs resource graph, parses config
			
			- Terraform Plugins: 
				- tools to access a third party service (bash, AWS, provisioner) and specify functionality within tools
				- providers & provisioners of terraform functionality
				- provider plugins handle authentication, defining resource-service mappings, initializing libraries to access API
				- provisioner plugins execute commands/scripts on a particular resource on creation/destruction (like aws cft ec2 userdata)
				- plugins
					- built-in provisioners (always included in bin)
					- providers from HashiCorp (automatically download)
					- providers/provisioners from third parties

			- policies

				- Sentinel policies: governance as code
					- defines rules restricting resource provisioning by Terraform config
					- enforces policies between the plan/apply phases, unless overridden by an authorized user

				- policy types
					- tfplan: uses tfplan import to restrict specific resource/data source attributes
					- tfconfig: uses tfconfig import to restrict Terraform module/variable/resource/data source/provider/provisioner/output config
					- tfstate: uses tfstate import to check if previously provisioned resources/data sources/outputs have attribute values restricted by governance policies

				- example use case: require terraform-generated keys to use a pgp key

		- commands
			- lint config: terraform fmt
			- create execution plan to change state: terraform plan
			- apply execution plan: terraform apply
			- state file: updated with new values (creations, deletions, updates) for defined/computed values
			- init: reads config in directory, finds/loads/downloads required plugins, locks plugin versions
			- plan
			- apply
			- destroy
			- workspace new ws
			- state
			- terraform import resource.name resource.name.name
			- terraform output

		- rules:
			- one provider per directory
			- to rollback, reset to a prior commit with correct config
			- if state file is corrupt, use state file rollback feature
			- check povray version, check functional install "povray+l tf_land.pov"
			- cannot add policies to the open-source version of Terraform Enterprise
			- make sure regions/availability zones are handled across multi-cloud location definitions

		- examples

			- ignore var changes

				lifecycle {
			    	ignore_changes = ["source_image"]
			  	}

			- create before destroy

			  	lifecycle {
				    create_before_destroy = true
				}
			- prevent resource destroy

				  lifecycle {
				    prevent_destroy = true
				  }

			- use cli params: terraform apply -var var1=value
			- use env var: TF_VAR_var1=value terraform apply
			- use a particular var file: terraform apply -var-file=production.tf

			- import existing resources into terraform

			 - import means adding resources to its state
			 - write the relevant Terraform config, then run “apply” so Terraform adds them to the state 

			- change value based on env workspace
				- disk_size_gb = "${terraform.workspace == "production" ? 200 : 50}"

			- upgrade plugins

				- ‘terraform init -upgrade’
				- rechecks releases.hashicorp.com to find & download new acceptable provider versions as defined in automatic downloads directory (.terraform/plugins/<OS>_<ARCH>)

			- lock module versions

				- with source: Terraform module registry:
					- use module ‘version’ attribute in Terraform config file

				- with source: github repo:
					- specify branch/versions/query string with ‘?ref’

			- add an ec2

				provider "aws" {
					region = "ap-south-1"
				}
				resource "aws_instance" {
					"example" {
						ami = "ami-4fc58420"
						instance_type = "t2.micro"
						tags {
						 Name = "terraform-example"
						}
					}
				}

			- using output in another module from another directory

				- originalResourceWithOutput directory

					- setting variables in vars.tf
							variable "location" {
							  default     = "West US"
							}

					- using variables in same directory's vars.tf
							location = "${var.location}"

					- setting output in output.tf
							output "output_name" {
							  value = "${azurerm_resource_group.res_group.name}"
							}

				- other directory using output

					module "resourceGroup" {
					  source = "../originalResourceWithOutput"
					  name = "output_name"
					}
				    resource_group_name = "${module.resourceGroup.output_name}"     
