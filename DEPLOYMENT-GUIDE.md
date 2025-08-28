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
