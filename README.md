# AI Assistant Supported ROSA & AI Components Deployment

Comprehensive automation suite for deploying Red Hat OpenShift Service on AWS (ROSA) HCP clusters with integrated AI capabilities including OpenShift AI, Llama Stack, and agentic AI demonstrations using AI code assistants like Cursor.

## 📋 Table of Contents

- [Overview](#overview)
- [AI-Powered Deployment with Code Assistants](#ai-powered-deployment-with-code-assistants)
- [Terraform Automation](#terraform-automation)
- [Complete AI Stack Deployment](#complete-ai-stack-deployment)
- [Getting Started](#getting-started)

## Overview

This repository provides AI-powered deployment approaches for the complete ROSA + AI stack:

### Deployment Methods
1. **🤖 AI Assistant-Led Terraform** - Production-ready IaC deployment through Cursor
2. **⚡ AI Assistant-Led CLI** - Quick CLI-based deployment through Cursor

### What You Can Deploy
3. **☸️ ROSA HCP Clusters** - Red Hat OpenShift Service on AWS with Hosted Control Plane
4. **🧠 OpenShift AI Platform** - Complete AI/ML platform with GPU support
5. **🦙 Llama Stack** - LLM inference infrastructure with vLLM/TGI backends
6. **🎯 Agentic AI Demo** - Pre-built agentic AI demonstration with MCP servers

---

## 🤖 AI-Powered Deployment with Code Assistants

### Using ROSA Cluster Creation with Cursor or Other AI Code Assistants

This repository includes comprehensive documentation that enables AI code assistants like **Cursor**, **GitHub Copilot**, or other LLM-based coding tools to automatically deploy complete ROSA clusters with OpenShift AI, Llama Stack, and agentic AI demonstrations.

#### 📖 Key Documentation Files

##### 1. **ROSA Cluster Creation Agent Instructions** 
📄 [`ROSA Cluster creation agent instructions.md`](./ROSA%20Cluster%20creation%20agent%20instructions.md)

**Purpose**: Comprehensive instructions for LLM agents to act as ROSA deployment experts

**What It Enables**:
- ✅ Automated ROSA HCP cluster creation through conversational AI
- ✅ Input validation and prerequisite checking
- ✅ Step-by-step guided deployment with error handling
- ✅ Support for both Terraform and CLI deployment methods
- ✅ Context preservation during long-running deployments
- ✅ Network configuration options (Public, Private, Zero Egress)
- ✅ Complete resource inventory and cleanup instructions

**Usage**:
```bash
# In Cursor or your AI code assistant:
"Create a ROSA HCP cluster in Singapore with 3 m5.4xlarge worker nodes. 
Use the instructions in 'ROSA Cluster creation agent instructions.md'"

# The AI assistant will:
# 1. Read the comprehensive instructions
# 2. Validate prerequisites (AWS credentials, ROSA CLI, etc.)
# 3. Guide you through configuration options
# 4. Execute deployment commands
# 5. Monitor progress and handle errors
# 6. Provide complete cluster access details
```

**Key Features**:
- **Validation Catalog**: Mandatory and optional parameter validation rules
- **Error Handling Protocol**: Strict rules for handling deployment failures
- **Multiple Deployment Methods**: Terraform (production) or CLI (quick)
- **Network Flexibility**: Public, Private, or Zero Egress cluster configurations
- **Resource Naming Conventions**: Consistent naming for all AWS resources
- **Comprehensive Prerequisites**: AWS and ROSA setup checklist with verification commands

##### 2. **OpenShift AI Setup Guide**
📄 [`OpenShift AI setup.md`](./OpenShift%20AI%20setup.md)

**Purpose**: Complete deployment guide for adding OpenShift AI capabilities to ROSA clusters

**What It Enables**:
- ✅ Deploy OpenShift AI operator on ROSA
- ✅ Configure GPU support for ML workloads
- ✅ Set up data science workbenches
- ✅ Deploy model serving infrastructure
- ✅ Configure S3 storage for models and artifacts

**Usage with AI Assistant**:
```bash
# After ROSA cluster is deployed:
"Deploy OpenShift AI on my ROSA cluster using the OpenShift AI setup.md guide"

# The AI assistant will:
# 1. Verify ROSA cluster is ready
# 2. Check prerequisites for OpenShift AI
# 3. Deploy the operator and components
# 4. Configure storage and GPU support
# 5. Set up workbench environments
# 6. Verify installation success
```

##### 3. **Llama Stack Integration Guide**
📄 [`Llama Stack OpenShift AI Integration Guide.md`](./Llama%20Stack%20OpenShift%20AI%20Integration%20Guide.md)

**Purpose**: Deploy Meta's Llama Stack for LLM inference on OpenShift AI

**What It Enables**:
- ✅ Llama Stack server deployment on OpenShift
- ✅ Model serving with vLLM or TGI backends
- ✅ Integration with OpenShift AI
- ✅ MCP (Model Context Protocol) server support
- ✅ Connection to agentic AI frameworks

**Usage with AI Assistant**:
```bash
"Deploy Llama Stack on my ROSA cluster following the Llama Stack integration guide"

# The AI assistant will:
# 1. Deploy Llama Stack server pods
# 2. Configure model serving endpoints
# 3. Set up inference routes
# 4. Connect to OpenShift AI workbenches
# 5. Verify model serving capabilities
```

##### 4. **Agentic AI Demo**
📁 [`rhai-agentic-demo/`](./rhai-agentic-demo/)

**Purpose**: Complete working demonstration of agentic AI with MCP servers

**What It Includes**:
- 🎯 **UI**: Streamlit-based chat interface for agent interactions
- 🔧 **MCP Servers**: CRM, PDF, and Slack integration servers
- 🗄️ **Database**: PostgreSQL for CRM data storage
- 🤖 **Agent Scripts**: ReAct agent with multi-MCP support
- 📊 **Notebooks**: Jupyter notebooks for experimentation
- ☸️ **Kubernetes Manifests**: Complete deployment configurations

**Usage with AI Assistant**:
```bash
"Deploy the agentic AI demo from rhai-agentic-demo/ on my ROSA cluster"

# The AI assistant will:
# 1. Deploy PostgreSQL database with sample CRM data
# 2. Deploy MCP servers (CRM, PDF, Slack)
# 3. Deploy Llama Stack for LLM inference
# 4. Deploy UI application
# 5. Configure networking and routes
# 6. Provide access URLs and usage instructions
```

#### 🚀 Complete End-to-End Deployment with AI Assistant

Here's how to deploy the entire stack using an AI code assistant like Cursor:

**Step 1: Initial Setup**
```bash
# In your AI code assistant terminal:
"Set up my environment for ROSA deployment:
1. Verify AWS CLI is configured with account 371594374265
2. Verify ROSA CLI is installed and authenticated
3. Check prerequisites using 'ROSA Cluster creation agent instructions.md'"
```

**Step 2: Create ROSA Cluster**
```bash
"Create a ROSA HCP cluster with these requirements:
- Name: ai-demo-cluster
- Region: Singapore (ap-southeast-1)
- Worker nodes: 3 x m5.4xlarge
- Network: Public API and ingress
- Use the agent instructions for deployment"
```

**Step 3: Deploy OpenShift AI**
```bash
"Now deploy OpenShift AI on the ai-demo-cluster following 
the OpenShift AI setup.md guide"
```

**Step 4: Deploy Llama Stack**
```bash
"Deploy Llama Stack using the Llama Stack OpenShift AI Integration Guide"
```

**Step 5: Deploy Agentic AI Demo**
```bash
"Deploy the complete agentic AI demo from rhai-agentic-demo/ 
including all MCP servers, database, and UI"
```

#### 📊 What Gets Deployed Automatically

When using the AI assistant with these instructions, you get:

**Infrastructure Layer**:
- ☸️ ROSA HCP Cluster with 3 worker nodes
- 🌐 VPC with public/private subnets
- 🔐 IAM roles and OIDC provider
- 🔒 Security groups and network policies

**AI/ML Platform**:
- 🧠 OpenShift AI Operator
- 📚 Data Science workbenches
- 🎯 Model serving infrastructure
- 💾 S3 storage configuration

**Llama Stack**:
- 🦙 Llama Stack server
- ⚡ vLLM/TGI model serving
- 🔌 Inference API endpoints
- 📡 MCP server integration

**Agentic AI Demo**:
- 🎨 Streamlit UI for agent chat
- 🔧 MCP Servers (CRM, PDF, Slack)
- 🗄️ PostgreSQL with sample data
- 🤖 ReAct agent framework
- 📊 Jupyter notebooks for exploration

#### 🎯 Benefits of AI-Assisted Deployment

1. **Zero Manual Configuration**: AI assistant reads the comprehensive instructions and handles all steps
2. **Error Recovery**: Built-in error handling and context preservation across failures
3. **Prerequisites Validation**: Automatic checking of all requirements before deployment
4. **Progress Monitoring**: Real-time status updates during 20-30 minute deployments
5. **Complete Documentation**: Every resource is documented and explained
6. **Cleanup Support**: Guided teardown when you're done
7. **Best Practices**: Follows Red Hat and AWS recommended configurations

#### ⚠️ Important Notes for AI-Assisted Deployment

**Prerequisites**:
- ✅ AWS account with ROSA enabled
- ✅ AWS CLI configured with credentials
- ✅ ROSA CLI installed and authenticated
- ✅ Billing account linked to Red Hat (for HCP clusters)
- ✅ Sufficient AWS quotas (100+ vCPUs)

**Token Management**:
- Use persistent offline token from https://console.redhat.com/openshift/token
- DO NOT use `rosa token` output (expires during deployment)
- Set `export RHCS_TOKEN="<your-persistent-token>"` before Terraform deployments

**Deployment Time**:
- ROSA Cluster: 20-30 minutes
- OpenShift AI: 10-15 minutes
- Llama Stack: 5-10 minutes
- Agentic Demo: 5-10 minutes
- **Total**: ~45-65 minutes for complete stack

#### 📖 Reading Order for Manual Reference

If you want to understand the process before using AI assistance:

1. Read [`ROSA Cluster creation agent instructions.md`](./ROSA%20Cluster%20creation%20agent%20instructions.md) - Understand ROSA deployment
2. Read [`OpenShift AI setup.md`](./OpenShift%20AI%20setup.md) - Learn about AI platform setup
3. Read [`Llama Stack OpenShift AI Integration Guide.md`](./Llama%20Stack%20OpenShift%20AI%20Integration%20Guide.md) - Understand LLM serving
4. Explore [`rhai-agentic-demo/README.md`](./rhai-agentic-demo/README.md) - See demo architecture

---

## 🧠 Complete AI Stack Deployment

### Full Stack Architecture

When deploying the complete AI stack, you get a production-ready environment for running agentic AI applications:

```
┌─────────────────────────────────────────────────────────────────┐
│                         ROSA HCP Cluster                         │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │                    OpenShift AI Platform                  │  │
│  │  ┌─────────────────────────────────────────────────────┐  │  │
│  │  │            Llama Stack (LLM Inference)             │  │  │
│  │  │  ┌──────────────────────────────────────────────┐  │  │  │
│  │  │  │         Agentic AI Demo Application          │  │  │  │
│  │  │  │                                               │  │  │  │
│  │  │  │  ┌────────────┐  ┌────────────┐             │  │  │  │
│  │  │  │  │ Streamlit  │  │ PostgreSQL │             │  │  │  │
│  │  │  │  │     UI     │  │  Database  │             │  │  │  │
│  │  │  │  └────────────┘  └────────────┘             │  │  │  │
│  │  │  │                                               │  │  │  │
│  │  │  │  ┌──────────────────────────────────────┐   │  │  │  │
│  │  │  │  │        MCP Servers                    │   │  │  │  │
│  │  │  │  │  • CRM Integration                    │   │  │  │  │
│  │  │  │  │  • PDF Processing                     │   │  │  │  │
│  │  │  │  │  • Slack Integration                  │   │  │  │  │
│  │  │  │  └──────────────────────────────────────┘   │  │  │  │
│  │  │  └──────────────────────────────────────────────┘  │  │  │
│  │  └─────────────────────────────────────────────────────┘  │  │
│  └───────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

### Deployment Approaches

**Option 1: AI Assistant-Led Terraform Deployment (Recommended for Production)**
- AI code assistant (Cursor) handles Terraform automation
- Infrastructure as Code with version control
- Repeatable, declarative deployments
- State management and drift detection
- Best for: Production environments, enterprise deployments, long-term infrastructure management

**Option 2: AI Assistant-Led CLI Deployment (Recommended for Quick Start)**
- AI code assistant (Cursor) executes ROSA CLI commands
- Faster initial deployment (no Terraform setup)
- Direct interaction with ROSA APIs
- Real-time progress monitoring
- Best for: Development, testing, learning, proof-of-concepts

Both approaches leverage AI assistants to:
- ✅ Validate prerequisites automatically
- ✅ Handle errors and provide solutions
- ✅ Preserve context during long-running deployments
- ✅ Provide complete documentation of created resources

---

## 🚀 Getting Started

### Quick Start (5 Minutes to Deployment)

**Using Cursor or AI Code Assistant**:

1. **Clone this repository**:
   ```bash
   git clone https://github.com/yourusername/rosa-automation
   cd rosa-automation
   ```

2. **Set up credentials** (add to your long-term context or `.env`):
   ```bash
   export AWS_ACCESS_KEY_ID="your-aws-key"
   export AWS_SECRET_ACCESS_KEY="your-aws-secret"
   export RHCS_TOKEN="your-persistent-ocm-token"
   ```

3. **Ask your AI assistant**:
   ```
   "Deploy a complete ROSA cluster with OpenShift AI, Llama Stack, 
   and the agentic demo in Singapore region. Use the agent instructions 
   in this repository."
   ```

4. **Wait 45-65 minutes** while the AI assistant:
   - Validates prerequisites
   - Creates ROSA cluster
   - Deploys OpenShift AI
   - Sets up Llama Stack
   - Deploys agentic demo
   - Provides access URLs

5. **Access your environment**:
   - OpenShift Console: `https://console-openshift-console.apps.{cluster-domain}`
   - Agentic UI: `https://ui-route-{namespace}.apps.{cluster-domain}`
   - Llama Stack API: `https://llama-stack-{namespace}.apps.{cluster-domain}`

### Prerequisites Checklist

Before starting any deployment:

- [ ] **AWS Account**
  - [ ] Account enabled for ROSA
  - [ ] AWS CLI installed and configured
  - [ ] Sufficient quotas (100+ vCPUs)
  - [ ] ELB service-linked role created

- [ ] **Red Hat Account**
  - [ ] Red Hat account created
  - [ ] ROSA CLI installed
  - [ ] OCM token obtained from https://console.redhat.com/openshift/token
  - [ ] Billing account linked (for HCP clusters)

- [ ] **Local Tools**
  - [ ] Terraform installed (for Terraform deployment)
  - [ ] OpenShift CLI (oc) installed
  - [ ] Git installed
  - [ ] Code assistant (Cursor recommended) or manual deployment tools

### Verification Commands

```bash
# Verify AWS access
aws sts get-caller-identity

# Verify ROSA CLI
rosa whoami

# Verify ROSA quotas
rosa verify quota --region ap-southeast-1

# Verify ROSA permissions
rosa verify permissions

# Check OpenShift CLI
oc version
```

---

## 🔧 Terraform Automation

### Traditional Terraform Module Deployment

This module serves as a comprehensive solution for deploying, configuring and managing Red Hat OpenShift on AWS (ROSA) Hosted Control Plane (HCP) clusters within your AWS environment. With a focus on simplicity and efficiency, this module streamlines the process of setting up and maintaining ROSA HCP clusters, enabling users to use the power of OpenShift on AWS infrastructure effortlessly.

### Example Usage

```
module "hcp" {
  source = "terraform-redhat/rosa-hcp/rhcs"
  version = "1.6.2"

  cluster_name           = "my-cluster"
  openshift_version      = "4.14.24"
  machine_cidr           = "10.0.0.0/16"
  aws_subnet_ids         = ["subnet-1", "subnet-2"]
  aws_availability_zones = ["us-west-2a"]
  replicas               = 2

  // STS configuration
  create_account_roles  = true
  account_role_prefix   = "my-cluster-account"
  create_oidc           = true
  create_operator_roles = true
  operator_role_prefix  = "my-cluster-operator"
}
```

## Sub-modules

Sub-modules included in this module:

- account-iam-resource: Handles the provisioning of Identity and Access Management (IAM) resources required for managing access and permissions in the AWS account associated with the ROSA HCP cluster.
- idp: Responsible for configuring Identity Providers (IDPs) within the ROSA HCP cluster, faciliting seamless integration with external authentication system such as Github (GH), GitLab, Google, HTPasswd, LDAP and OpenID Connect (OIDC).
- machine-pool: Facilitates the management of machine pools within the ROSA HCP cluster, enabling users to scale resources and adjust specifications based on workload demands.
- oidc-config-and-provider: Manages the configuration of OpenID Connect (OIDC) hosted files and providers for ROSA HCP clusters, enabling secure authentication and access control mechanisms for operator roles.
- operator-roles: Oversees the management of roles assigned to operators within the ROSA HCP cluster, enabling to perform required actions with appropriate permissions on the lifecyle of a cluster.
- rosa-cluster-hcp: Handles the core configuration and provisioning of the ROSA HCP cluster, including cluster networking, security settings and other essential components.
- vpc: Handles the configuration and provisioning of the Virtucal Private Cloud (VPC) infrastracture required for hosting the ROSA HCP cluster and it's associated resources.

The primary sub-modules responsible for ROSA HCP cluster creation includes optional configurations for setting up account roles, operator roles and OIDC config/provider. This comprehensive module handles the entire process of provisioning and configuring ROSA HCP clusters in your AWS environment.

## Pre-requisites

* [Terraform CLI](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli) (1.4.6+) must be installed.
* An [AWS account](https://aws.amazon.com/free/?all-free-tier) and the [associated credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html) that allow you to create resources. These credentials must be configured for the AWS provider (see [Authentication and Configuration](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#authentication-and-configuration) section in AWS terraform provider documentation.)
* The [ROSA getting started AWS prerequisites](https://console.redhat.com/openshift/create/rosa/getstarted) must be completed.
* A valid [OpenShift Cluster Manager API Token](https://console.redhat.com/openshift/token) must be configured (see [Authentication and configuration](https://registry.terraform.io/providers/terraform-redhat/rhcs/latest/docs#authentication-and-configuration) for more information).

We recommend you install the following CLI tools:

* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
* [ROSA CLI](https://docs.openshift.com/rosa/cli_reference/rosa_cli/rosa-get-started-cli.html)
* [Openshift CLI (oc)](https://docs.openshift.com/rosa/cli_reference/openshift_cli/getting-started-cli.html)

<!-- BEGIN_AUTOMATED_TF_DOCS_BLOCK -->
## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_terraform"></a> [terraform](#requirement\_terraform) | >= 1.0 |
| <a name="requirement_aws"></a> [aws](#requirement\_aws) | >= 5.38.0 |
| <a name="requirement_null"></a> [null](#requirement\_null) | >= 3.0.0 |
| <a name="requirement_rhcs"></a> [rhcs](#requirement\_rhcs) | >= 1.6.2 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_aws"></a> [aws](#provider\_aws) | >= 5.38.0 |
| <a name="provider_null"></a> [null](#provider\_null) | >= 3.0.0 |
| <a name="provider_rhcs"></a> [rhcs](#provider\_rhcs) | >= 1.6.2 |

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_account_iam_resources"></a> [account\_iam\_resources](#module\_account\_iam\_resources) | ./modules/account-iam-resources | n/a |
| <a name="module_oidc_config_and_provider"></a> [oidc\_config\_and\_provider](#module\_oidc\_config\_and\_provider) | ./modules/oidc-config-and-provider | n/a |
| <a name="module_operator_roles"></a> [operator\_roles](#module\_operator\_roles) | ./modules/operator-roles | n/a |
| <a name="module_rhcs_hcp_kubelet_configs"></a> [rhcs\_hcp\_kubelet\_configs](#module\_rhcs\_hcp\_kubelet\_configs) | ./modules/kubelet-configs | n/a |
| <a name="module_rhcs_hcp_machine_pool"></a> [rhcs\_hcp\_machine\_pool](#module\_rhcs\_hcp\_machine\_pool) | ./modules/machine-pool | n/a |
| <a name="module_rhcs_identity_provider"></a> [rhcs\_identity\_provider](#module\_rhcs\_identity\_provider) | ./modules/idp | n/a |
| <a name="module_rosa_cluster_hcp"></a> [rosa\_cluster\_hcp](#module\_rosa\_cluster\_hcp) | ./modules/rosa-cluster-hcp | n/a |

## Resources

| Name | Type |
|------|------|
| [null_resource.validations](https://registry.terraform.io/providers/hashicorp/null/latest/docs/resources/resource) | resource |
| [rhcs_dns_domain.dns_domain](https://registry.terraform.io/providers/terraform-redhat/rhcs/latest/docs/resources/dns_domain) | resource |
| [aws_caller_identity.current](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/caller_identity) | data source |


# ROSA Cluster Deployment Guide

## 🚀 Quick Start

### 1. Set RHCS Credentials
```bash
export RHCS_CLIENT_ID="your-rhcs-client-id"
export RHCS_CLIENT_SECRET="your-rhcs-client-secret"
```

### 2. Configure Deployment
```bash
cp terraform.tfvars.example terraform.tfvars
# Edit terraform.tfvars with your settings
```

### 3. Deploy
```bash
terraform init
terraform plan
terraform apply
```

## ✅ Works with Standard Terraform

The configuration now works seamlessly with standard `terraform plan` and `terraform apply` commands - no custom scripts needed!

## 📊 View Results
```bash
terraform output cluster_api_url
terraform output cluster_console_url
```

## 🔧 Configuration Options

- **New VPC**: Set `create_vpc = true` (default) - automatically creates both public and private subnets
- **Existing VPC**: Set `create_vpc = false` and provide `aws_subnet_ids` (must include both public and private subnets)
- **Machine Pools**: Set `create_additional_machine_pools = true`
- **GitOps**: Set `deploy_openshift_gitops = true` (default)

## ⚠️ Important: Subnet Requirements

ROSA HCP clusters require **both public and private subnets**:
- **Public subnets**: For load balancers and internet access
- **Private subnets**: For worker nodes and internal services

When `create_vpc = true`, this is handled automatically. When using existing VPC, ensure you provide both types of subnets in `aws_subnet_ids`.


## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_account_role_prefix"></a> [account\_role\_prefix](#input\_account\_role\_prefix) | User-defined prefix for all generated AWS resources (default "account-role-<random>") | `string` | `null` | no |
| <a name="input_additional_trust_bundle"></a> [additional\_trust\_bundle](#input\_additional\_trust\_bundle) | A string containing a PEM-encoded X.509 certificate bundle that will be added to the nodes' trusted certificate store. | `string` | `null` | no |
| <a name="input_admin_credentials_password"></a> [admin\_credentials\_password](#input\_admin\_credentials\_password) | Admin password that is created with the cluster. The password must contain at least 14 characters (ASCII-standard) without whitespaces including uppercase letters, lowercase letters, and numbers or symbols. | `string` | `null` | no |
| <a name="input_admin_credentials_username"></a> [admin\_credentials\_username](#input\_admin\_credentials\_username) | Admin username that is created with the cluster. auto generated username - "cluster-admin" | `string` | `null` | no |
| <a name="input_autoscaler_max_node_provision_time"></a> [autoscaler\_max\_node\_provision\_time](#input\_autoscaler\_max\_node\_provision\_time) | Maximum time cluster-autoscaler waits for node to be provisioned. | `string` | `null` | no |
| <a name="input_autoscaler_max_nodes_total"></a> [autoscaler\_max\_nodes\_total](#input\_autoscaler\_max\_nodes\_total) | Maximum number of nodes in all node groups. Cluster autoscaler will not grow the cluster beyond this number. | `number` | `null` | no |
| <a name="input_autoscaler_max_pod_grace_period"></a> [autoscaler\_max\_pod\_grace\_period](#input\_autoscaler\_max\_pod\_grace\_period) | Gives pods graceful termination time before scaling down. | `number` | `null` | no |
| <a name="input_autoscaler_pod_priority_threshold"></a> [autoscaler\_pod\_priority\_threshold](#input\_autoscaler\_pod\_priority\_threshold) | To allow users to schedule 'best-effort' pods, which shouldn't trigger Cluster Autoscaler actions, but only run when there are spare resources available. | `number` | `null` | no |
| <a name="input_aws_additional_allowed_principals"></a> [aws\_additional\_allowed\_principals](#input\_aws\_additional\_allowed\_principals) | The additional allowed principals to use when installing the cluster. | `list(string)` | `null` | no |
| <a name="input_aws_additional_compute_security_group_ids"></a> [aws\_additional\_compute\_security\_group\_ids](#input\_aws\_additional\_compute\_security\_group\_ids) | The additional security group IDs to be added to the default worker machine pool. | `list(string)` | `null` | no |
| <a name="input_aws_availability_zones"></a> [aws\_availability\_zones](#input\_aws\_availability\_zones) | The AWS availability zones where instances of the default worker machine pool are deployed. Leave empty for the installer to pick availability zones | `list(string)` | `[]` | no |
| <a name="input_aws_billing_account_id"></a> [aws\_billing\_account\_id](#input\_aws\_billing\_account\_id) | The AWS billing account identifier where all resources are billed. If no information is provided, the data will be retrieved from the currently connected account. | `string` | `null` | no |
| <a name="input_aws_subnet_ids"></a> [aws\_subnet\_ids](#input\_aws\_subnet\_ids) | The Subnet IDs to use when installing the cluster. | `list(string)` | n/a | yes |
| <a name="input_base_dns_domain"></a> [base\_dns\_domain](#input\_base\_dns\_domain) | Base DNS domain name previously reserved, e.g. '1vo8.p3.openshiftapps.com'. | `string` | `null` | no |
| <a name="input_cluster_autoscaler_enabled"></a> [cluster\_autoscaler\_enabled](#input\_cluster\_autoscaler\_enabled) | Enable Autoscaler for this cluster. This resource is currently unavailable and using will result in error 'Autoscaler configuration is not available' | `bool` | `false` | no |
| <a name="input_cluster_name"></a> [cluster\_name](#input\_cluster\_name) | Name of the cluster. After the creation of the resource, it is not possible to update the attribute value. | `string` | n/a | yes |
| <a name="input_compute_machine_type"></a> [compute\_machine\_type](#input\_compute\_machine\_type) | Identifies the Instance type used by the default worker machine pool e.g. `m5.xlarge`. Use the `rhcs_machine_types` data source to find the possible values. | `string` | `null` | no |
| <a name="input_create_account_roles"></a> [create\_account\_roles](#input\_create\_account\_roles) | Create the aws account roles for rosa | `bool` | `false` | no |
| <a name="input_create_admin_user"></a> [create\_admin\_user](#input\_create\_admin\_user) | To create cluster admin user with default username `cluster-admin` and generated password. It will be ignored if `admin_credentials_username` or `admin_credentials_password` is set. (default: false) | `bool` | `null` | no |
| <a name="input_create_dns_domain_reservation"></a> [create\_dns\_domain\_reservation](#input\_create\_dns\_domain\_reservation) | Creates reserves a dns domain domain for the cluster. This value will be created by the install step if not pre created via this configuration. | `bool` | `false` | no |
| <a name="input_create_oidc"></a> [create\_oidc](#input\_create\_oidc) | Create the oidc resources. This value should not be updated, please create a new resource instead or utilize the submodule to create a new oidc config | `bool` | `false` | no |
| <a name="input_create_operator_roles"></a> [create\_operator\_roles](#input\_create\_operator\_roles) | Create the aws account roles for rosa | `bool` | `false` | no |
| <a name="input_default_ingress_listening_method"></a> [default\_ingress\_listening\_method](#input\_default\_ingress\_listening\_method) | Listening Method for ingress. Options are ["internal", "external"]. Default is "external". When empty is set based on private variable. | `string` | `""` | no |
| <a name="input_destroy_timeout"></a> [destroy\_timeout](#input\_destroy\_timeout) | Maximum duration in minutes to allow for destroying resources. (Default: 60 minutes) | `number` | `null` | no |
| <a name="input_disable_waiting_in_destroy"></a> [disable\_waiting\_in\_destroy](#input\_disable\_waiting\_in\_destroy) | Disable addressing cluster state in the destroy resource. Default value is false, and so a `destroy` will wait for the cluster to be deleted. | `bool` | `null` | no |
| <a name="input_ec2_metadata_http_tokens"></a> [ec2\_metadata\_http\_tokens](#input\_ec2\_metadata\_http\_tokens) | Should cluster nodes use both v1 and v2 endpoints or just v2 endpoint of EC2 Instance Metadata Service (IMDS). Available since OpenShift 4.11.0. | `string` | `"optional"` | no |
| <a name="input_etcd_encryption"></a> [etcd\_encryption](#input\_etcd\_encryption) | Add etcd encryption. By default etcd data is encrypted at rest. This option configures etcd encryption on top of existing storage encryption. | `bool` | `null` | no |
| <a name="input_etcd_kms_key_arn"></a> [etcd\_kms\_key\_arn](#input\_etcd\_kms\_key\_arn) | The key ARN is the Amazon Resource Name (ARN) of a CMK. It is a unique, fully qualified identifier for the CMK. A key ARN includes the AWS account, Region, and the key ID. | `string` | `null` | no |
| <a name="input_host_prefix"></a> [host\_prefix](#input\_host\_prefix) | Subnet prefix length to assign to each individual node. For example, if host prefix is set to "23", then each node is assigned a /23 subnet out of the given CIDR. | `number` | `null` | no |
| <a name="input_http_proxy"></a> [http\_proxy](#input\_http\_proxy) | A proxy URL to use for creating HTTP connections outside the cluster. The URL scheme must be http. | `string` | `null` | no |
| <a name="input_https_proxy"></a> [https\_proxy](#input\_https\_proxy) | A proxy URL to use for creating HTTPS connections outside the cluster. | `string` | `null` | no |
| <a name="input_identity_providers"></a> [identity\_providers](#input\_identity\_providers) | Provides a generic approach to add multiple identity providers after the creation of the cluster. This variable allows users to specify configurations for multiple identity providers in a flexible and customizable manner, facilitating the management of resources post-cluster deployment. For additional details regarding the variables utilized, refer to the [idp sub-module](./modules/idp). For non-primitive variables (such as maps, lists, and objects), supply the JSON-encoded string. | `map(any)` | `{}` | no |
| <a name="input_ignore_machine_pools_deletion_error"></a> [ignore\_machine\_pools\_deletion\_error](#input\_ignore\_machine\_pools\_deletion\_error) | Ignore machine pool deletion error. Assists when cluster resource is managed within the same file for the destroy use case | `bool` | `false` | no |
| <a name="input_kms_key_arn"></a> [kms\_key\_arn](#input\_kms\_key\_arn) | The key ARN is the Amazon Resource Name (ARN) of a CMK. It is a unique, fully qualified identifier for the CMK. A key ARN includes the AWS account, Region, and the key ID. | `string` | `null` | no |
| <a name="input_kubelet_configs"></a> [kubelet\_configs](#input\_kubelet\_configs) | Provides a generic approach to add multiple kubelet configs after the creation of the cluster. This variable allows users to specify configurations for multiple kubelet configs in a flexible and customizable manner, facilitating the management of resources post-cluster deployment. For additional details regarding the variables utilized, refer to the [idp sub-module](./modules/kubelet-configs). For non-primitive variables (such as maps, lists, and objects), supply the JSON-encoded string. | `map(any)` | `{}` | no |
| <a name="input_machine_cidr"></a> [machine\_cidr](#input\_machine\_cidr) | Block of IP addresses used by OpenShift while installing the cluster, for example "10.0.0.0/16". | `string` | `null` | no |
| <a name="input_machine_pools"></a> [machine\_pools](#input\_machine\_pools) | Provides a generic approach to add multiple machine pools after the creation of the cluster. This variable allows users to specify configurations for multiple machine pools in a flexible and customizable manner, facilitating the management of resources post-cluster deployment. For additional details regarding the variables utilized, refer to the [machine-pool sub-module](./modules/machine-pool). For non-primitive variables (such as maps, lists, and objects), supply the JSON-encoded string. | `map(any)` | `{}` | no |
| <a name="input_managed_oidc"></a> [managed\_oidc](#input\_managed\_oidc) | OIDC type managed or unmanaged oidc. Only active when create\_oidc also enabled. This value should not be updated, please create a new resource instead | `bool` | `true` | no |
| <a name="input_no_proxy"></a> [no\_proxy](#input\_no\_proxy) | A comma-separated list of destination domain names, domains, IP addresses or other network CIDRs to exclude proxying. | `string` | `null` | no |
| <a name="input_oidc_config_id"></a> [oidc\_config\_id](#input\_oidc\_config\_id) | The unique identifier associated with users authenticated through OpenID Connect (OIDC) within the ROSA cluster. If create\_oidc is false this attribute is required. | `string` | `null` | no |
| <a name="input_oidc_endpoint_url"></a> [oidc\_endpoint\_url](#input\_oidc\_endpoint\_url) | Registered OIDC configuration issuer URL, added as the trusted relationship to the operator roles. Valid only when create\_oidc is false. | `string` | `null` | no |
| <a name="input_openshift_version"></a> [openshift\_version](#input\_openshift\_version) | Desired version of OpenShift for the cluster, for example '4.1.0'. If version is greater than the currently running version, an upgrade will be scheduled. | `string` | n/a | yes |
| <a name="input_operator_role_prefix"></a> [operator\_role\_prefix](#input\_operator\_role\_prefix) | User-defined prefix for generated AWS operator policies. Use "account-role-prefix" in case no value provided. | `string` | `null` | no |
| <a name="input_path"></a> [path](#input\_path) | The arn path for the account/operator roles as well as their policies. Must begin and end with '/'. | `string` | `"/"` | no |
| <a name="input_permissions_boundary"></a> [permissions\_boundary](#input\_permissions\_boundary) | The ARN of the policy that is used to set the permissions boundary for the IAM roles in STS clusters. | `string` | `""` | no |
| <a name="input_pod_cidr"></a> [pod\_cidr](#input\_pod\_cidr) | Block of IP addresses from which Pod IP addresses are allocated, for example "10.128.0.0/14". | `string` | `null` | no |
| <a name="input_private"></a> [private](#input\_private) | Restrict master API endpoint and application routes to direct, private connectivity. (default: false) | `bool` | `false` | no |
| <a name="input_properties"></a> [properties](#input\_properties) | User defined properties. | `map(string)` | `null` | no |
| <a name="input_replicas"></a> [replicas](#input\_replicas) | Number of worker nodes to provision. This attribute is applicable solely when autoscaling is disabled. Single zone clusters need at least 2 nodes, multizone clusters need at least 3 nodes. Hosted clusters require that the number of worker nodes be a multiple of the number of private subnets. (default: 2) | `number` | `null` | no |
| <a name="input_service_cidr"></a> [service\_cidr](#input\_service\_cidr) | Block of IP addresses for services, for example "172.30.0.0/16". | `string` | `null` | no |
| <a name="input_tags"></a> [tags](#input\_tags) | Apply user defined tags to all cluster resources created in AWS. After the creation of the cluster is completed, it is not possible to update this attribute. | `map(string)` | `null` | no |
| <a name="input_upgrade_acknowledgements_for"></a> [upgrade\_acknowledgements\_for](#input\_upgrade\_acknowledgements\_for) | Indicates acknowledgement of agreements required to upgrade the cluster version between minor versions (e.g. a value of "4.12" indicates acknowledgement of any agreements required to upgrade to OpenShift 4.12.z from 4.11 or before). | `string` | `null` | no |
| <a name="input_version_channel_group"></a> [version\_channel\_group](#input\_version\_channel\_group) | Desired channel group of the version [stable, candidate, fast, nightly]. | `string` | `"stable"` | no |
| <a name="input_wait_for_create_complete"></a> [wait\_for\_create\_complete](#input\_wait\_for\_create\_complete) | Wait until the cluster is either in a ready state or in an error state. The waiter has a timeout of 20 minutes. (default: true) | `bool` | `true` | no |
| <a name="input_wait_for_std_compute_nodes_complete"></a> [wait\_for\_std\_compute\_nodes\_complete](#input\_wait\_for\_std\_compute\_nodes\_complete) | Wait until the initial set of machine pools to be available. The waiter has a timeout of 60 minutes. (default: true) | `bool` | `true` | no |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_account_role_prefix"></a> [account\_role\_prefix](#output\_account\_role\_prefix) | The prefix used for all generated AWS resources. |
| <a name="output_account_roles_arn"></a> [account\_roles\_arn](#output\_account\_roles\_arn) | A map of Amazon Resource Names (ARNs) associated with the AWS IAM roles created. The key in the map represents the name of an AWS IAM role, while the corresponding value represents the associated Amazon Resource Name (ARN) of that role. |
| <a name="output_cluster_admin_password"></a> [cluster\_admin\_password](#output\_cluster\_admin\_password) | The password of the admin user. |
| <a name="output_cluster_admin_username"></a> [cluster\_admin\_username](#output\_cluster\_admin\_username) | The username of the admin user. |
| <a name="output_cluster_api_url"></a> [cluster\_api\_url](#output\_cluster\_api\_url) | The URL of the API server. |
| <a name="output_cluster_console_url"></a> [cluster\_console\_url](#output\_cluster\_console\_url) | The URL of the console. |
| <a name="output_cluster_current_version"></a> [cluster\_current\_version](#output\_cluster\_current\_version) | The currently running version of OpenShift on the cluster, for example '4.11.0'. |
| <a name="output_cluster_domain"></a> [cluster\_domain](#output\_cluster\_domain) | The DNS domain of cluster. |
| <a name="output_cluster_id"></a> [cluster\_id](#output\_cluster\_id) | Unique identifier of the cluster. |
| <a name="output_cluster_state"></a> [cluster\_state](#output\_cluster\_state) | The state of the cluster. |
| <a name="output_oidc_config_id"></a> [oidc\_config\_id](#output\_oidc\_config\_id) | The unique identifier associated with users authenticated through OpenID Connect (OIDC) generated by this OIDC config. |
| <a name="output_oidc_endpoint_url"></a> [oidc\_endpoint\_url](#output\_oidc\_endpoint\_url) | Registered OIDC configuration issuer URL, generated by this OIDC config. |
| <a name="output_operator_role_prefix"></a> [operator\_role\_prefix](#output\_operator\_role\_prefix) | Prefix used for generated AWS operator policies. |
| <a name="output_operator_roles_arn"></a> [operator\_roles\_arn](#output\_operator\_roles\_arn) | List of Amazon Resource Names (ARNs) for all operator roles created. |
| <a name="output_path"></a> [path](#output\_path) | The arn path for the account/operator roles as well as their policies. |
<!-- END_AUTOMATED_TF_DOCS_BLOCK -->

---

## 📚 Additional Resources

### Documentation Files in This Repository

#### Core Deployment Guides
- **[ROSA Cluster Creation Agent Instructions](./ROSA%20Cluster%20creation%20agent%20instructions.md)** - Comprehensive LLM agent instructions for automated ROSA deployment
- **[OpenShift AI Setup Guide](./OpenShift%20AI%20setup.md)** - Complete guide for deploying OpenShift AI on ROSA clusters
- **[Llama Stack Integration Guide](./Llama%20Stack%20OpenShift%20AI%20Integration%20Guide.md)** - Deploy and integrate Llama Stack for LLM inference

#### Demo Applications
- **[Agentic AI Demo](./rhai-agentic-demo/)** - Complete working demonstration with MCP servers, UI, and agent framework
  - [Deployment Documentation](./rhai-agentic-demo/README.md)
  - [Local Deployment Guide](./rhai-agentic-demo/docs/deploy-demo-local.md)
  - [Llama Stack Setup](./rhai-agentic-demo/docs/run-llama-stack.md)

#### Deployment Examples
- [ROSA HCP Public Cluster](./examples/rosa-hcp-public/)
- [ROSA HCP Private Cluster](./examples/rosa-hcp-private/)
- [ROSA HCP with Multiple Machine Pools and IDPs](./examples/rosa-hcp-public-with-multiple-machinepools-and-idps/)
- [ROSA HCP with Shared VPC](./examples/rosa-hcp-private-shared-vpc/)
- [ROSA HCP with Unmanaged OIDC](./examples/rosa-hcp-public-unmanaged-oidc/)

### External Resources

#### Official Documentation
- [Red Hat OpenShift Service on AWS (ROSA)](https://docs.openshift.com/rosa/)
- [ROSA Getting Started Guide](https://console.redhat.com/openshift/create/rosa/getstarted)
- [ROSA CLI Reference](https://docs.openshift.com/rosa/cli_reference/rosa_cli/rosa-get-started-cli.html)
- [OpenShift AI Documentation](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed)
- [Terraform RHCS Provider](https://registry.terraform.io/providers/terraform-redhat/rhcs/latest/docs)

#### AWS Resources
- [AWS ROSA Prerequisites](https://docs.aws.amazon.com/ROSA/latest/userguide/rosa-getting-started-prerequisites.html)
- [AWS Service Quotas](https://console.aws.amazon.com/servicequotas/)
- [AWS EC2 Instance Types](https://aws.amazon.com/ec2/instance-types/)

#### Learning Resources
- [Red Hat OpenShift AI Workshops](https://redhatquickcourses.github.io/llm-on-rhoai/)
- [Meta Llama Stack Documentation](https://llama-stack.readthedocs.io/)
- [Model Context Protocol (MCP) Specification](https://modelcontextprotocol.io/)

---

## 🎯 Use Cases

This automation suite supports various deployment scenarios:

### 1. **Development & Testing**
```bash
"Create a minimal ROSA cluster for testing:
- 2 worker nodes (m5.xlarge)
- Public access
- No GPU support
- Development/testing tags"
```

### 2. **AI/ML Workloads**
```bash
"Deploy a ROSA cluster for machine learning:
- 3 GPU worker nodes (g5.4xlarge)
- OpenShift AI with GPU operator
- S3 integration for model storage
- Data science workbenches"
```

### 3. **Agentic AI Applications**
```bash
"Deploy complete agentic AI stack:
- ROSA HCP cluster
- OpenShift AI platform
- Llama Stack for inference
- MCP servers (CRM, PDF, Slack)
- Sample agentic UI"
```

### 4. **Production Workloads**
```bash
"Create production-ready ROSA cluster:
- Private cluster with PrivateLink
- High availability (multi-AZ)
- Enterprise security (zero egress)
- Custom machine pools
- Monitoring and logging"
```

### 5. **Hybrid Cloud**
```bash
"Deploy ROSA with existing infrastructure:
- Use existing VPC
- Integrate with on-prem LDAP
- Custom networking configuration
- Shared OIDC provider"
```

---

## 🔒 Security Considerations

### Network Security
- **Public Clusters**: API and ingress accessible from internet (good for dev/test)
- **Private Clusters**: API accessible only within VPC (recommended for production)
- **Zero Egress**: No outbound internet (highest security, requires VPC endpoints)

### Identity & Access
- AWS IAM roles and policies follow least-privilege principles
- OpenShift RBAC for cluster access control
- OIDC integration for federated authentication
- Optional integration with enterprise identity providers

### Data Protection
- Optional etcd encryption at rest
- EBS volume encryption
- Network encryption in transit
- S3 bucket encryption for AI models and artifacts

### Compliance
- Consistent resource tagging for audit trails
- Complete deployment documentation
- Infrastructure-as-Code for reproducibility
- Automated cleanup procedures

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for:
- Bug fixes
- Documentation improvements
- New features or examples
- AI assistant instruction enhancements

---

## 📄 License

See the LICENSE file for details.

---

## 💬 Support

For issues and questions:
- **ROSA Issues**: [Red Hat Customer Portal](https://access.redhat.com/)
- **Repository Issues**: [GitHub Issues](https://github.com/yourusername/rosa-automation/issues)
- **Community**: [OpenShift Community](https://www.openshift.com/community)

---

## 🎓 Quick Reference

### Essential Commands

```bash
# ROSA Cluster Management
rosa list clusters
rosa describe cluster <cluster-name>
rosa delete cluster <cluster-name>

# OpenShift CLI
oc login <api-url> -u <username> -p <password>
oc get nodes
oc get pods --all-namespaces
oc projects

# AWS Resources
aws ec2 describe-vpcs --region <region>
aws iam list-roles --query 'Roles[?contains(RoleName, `rosa`)]'
aws resourcegroupstaggingapi get-resources --tag-filters Key=rosa_cluster,Values=<cluster-name>

# Terraform Management
terraform init
terraform plan
terraform apply
terraform destroy
terraform output cluster_console_url
```

### Common Troubleshooting

**Issue: Token expired during deployment**
```bash
# Solution: Use persistent offline token
export RHCS_TOKEN="<get-from-console.redhat.com/openshift/token>"
```

**Issue: Insufficient AWS quotas**
```bash
# Solution: Check and request quota increases
rosa verify quota --region <region>
aws service-quotas list-service-quotas --service-code ec2
```

**Issue: Billing account not linked**
```bash
# Solution: Complete setup via Red Hat Console
# Visit: https://console.redhat.com/openshift/create/rosa/getstarted
```

**Issue: Network connectivity problems**
```bash
# Solution: Verify VPC and subnet configuration
aws ec2 describe-subnets --filters "Name=vpc-id,Values=<vpc-id>"
rosa describe cluster <cluster-name> | grep -E "Subnet|VPC"
```

---

**🚀 Ready to Deploy?**

Choose your AI-assisted deployment method:
- **Option 1 (Production)**: Ask Cursor to deploy using Terraform with the agent instructions for IaC benefits
- **Option 2 (Quick Start)**: Ask Cursor to deploy using CLI commands for faster deployment

**Need Help?** Refer to the comprehensive guides in this repository or use your AI code assistant with the included instructions!
