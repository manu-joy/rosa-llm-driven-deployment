# AI Model Deployment via ArgoCD
resource "null_resource" "create_ai_model_application" {
  count      = var.deploy_ai_model && var.deploy_openshift_gitops ? 1 : 0
  depends_on = [null_resource.create_openshift_ai_application]

  provisioner "local-exec" {
    command = <<-EOT
      #!/bin/bash
      set -e
      echo "Starting AI Model application deployment..."
      
      # Login to cluster
      echo "Logging into OpenShift cluster..."
      if ! oc login --username="${module.rosa_cluster_hcp.cluster_admin_username}" --password="${module.rosa_cluster_hcp.cluster_admin_password}" "${module.rosa_cluster_hcp.cluster_api_url}" --insecure-skip-tls-verify; then
        echo "ERROR: Failed to login to OpenShift cluster"
        exit 1
      fi
      echo "Successfully logged into cluster"

      # Create AI Model Application
      echo "Proceeding to create AI Model application..."

      # Create AI Model Application
      echo "Creating AI Model ArgoCD application..."
      if ! oc apply -f - <<AI_MODEL_APP_EOF
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: ai-model
  namespace: openshift-gitops
  finalizers:
    - resources-finalizer.argocd.argoproj.io
spec:
  project: default
  source:
    repoURL: ${var.gitops_repo_url}
    targetRevision: HEAD
    path: ai-models/mistral
  destination:
    server: https://kubernetes.default.svc
    namespace: ai-models
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
      allowEmpty: false
    syncOptions:
      - CreateNamespace=true
      - RespectIgnoreDifferences=true
      - ApplyOutOfSyncOnly=true
    retry:
      limit: 5
      backoff:
        duration: 5s
        factor: 2
        maxDuration: 3m
AI_MODEL_APP_EOF
      then
        echo "ERROR: Failed to create AI Model ArgoCD application"
        exit 1
      fi

      echo "AI model application created successfully!"
    EOT
  }

  triggers = {
    cluster_id        = module.rosa_cluster_hcp.cluster_id
    admin_username    = module.rosa_cluster_hcp.cluster_admin_username
    admin_password    = module.rosa_cluster_hcp.cluster_admin_password
    api_url           = module.rosa_cluster_hcp.cluster_api_url
    gitops_repo_url   = var.gitops_repo_url
    deploy_ai_model   = var.deploy_ai_model
  }
}

# Create OpenShift AI Operator Application via ArgoCD
resource "null_resource" "create_openshift_ai_application" {
  count      = var.deploy_openshift_ai && var.deploy_openshift_gitops ? 1 : 0
  depends_on = [time_sleep.wait_for_argocd]

  provisioner "local-exec" {
    command = <<EOF
      # Login to cluster
      oc login --username="${module.rosa_cluster_hcp.cluster_admin_username}" --password="${module.rosa_cluster_hcp.cluster_admin_password}" "${module.rosa_cluster_hcp.cluster_api_url}" --insecure-skip-tls-verify

      # Create OpenShift AI Operator Application
      oc apply -f - <<OPENSHIFT_AI_APP_EOF
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: openshift-ai-operator
  namespace: openshift-gitops
  finalizers:
    - resources-finalizer.argocd.argoproj.io
spec:
  project: default
  source:
    repoURL: ${var.gitops_repo_url}
    targetRevision: HEAD
    path: operators/openshift-ai
  destination:
    server: https://kubernetes.default.svc
    namespace: redhat-ods-operator
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
      allowEmpty: false
    syncOptions:
      - CreateNamespace=true
      - RespectIgnoreDifferences=true
      - ApplyOutOfSyncOnly=true
    retry:
      limit: 5
      backoff:
        duration: 5s
        factor: 2
        maxDuration: 3m
OPENSHIFT_AI_APP_EOF

      echo "OpenShift AI operator application created"
    EOF
  }

  triggers = {
    cluster_id           = module.rosa_cluster_hcp.cluster_id
    admin_username       = module.rosa_cluster_hcp.cluster_admin_username
    admin_password       = module.rosa_cluster_hcp.cluster_admin_password
    api_url              = module.rosa_cluster_hcp.cluster_api_url
    gitops_repo_url      = var.gitops_repo_url
    deploy_openshift_ai  = var.deploy_openshift_ai
  }
}

# Create OpenShift Serverless Operator Application via ArgoCD
resource "null_resource" "create_openshift_serverless_application" {
  count      = local.deploy_openshift_serverless && var.deploy_openshift_gitops ? 1 : 0
  depends_on = [time_sleep.wait_for_argocd]

  provisioner "local-exec" {
    command = <<EOF
      # Login to cluster
      oc login --username="${module.rosa_cluster_hcp.cluster_admin_username}" --password="${module.rosa_cluster_hcp.cluster_admin_password}" "${module.rosa_cluster_hcp.cluster_api_url}" --insecure-skip-tls-verify

      # Create OpenShift Serverless Operator Application
      oc apply -f - <<OPENSHIFT_SERVERLESS_APP_EOF
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: openshift-serverless-operator
  namespace: openshift-gitops
  finalizers:
    - resources-finalizer.argocd.argoproj.io
spec:
  project: default
  source:
    repoURL: ${var.gitops_repo_url}
    targetRevision: HEAD
    path: operators/openshift-serverless
  destination:
    server: https://kubernetes.default.svc
    namespace: openshift-serverless
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
      allowEmpty: false
    syncOptions:
      - CreateNamespace=true
      - RespectIgnoreDifferences=true
      - ApplyOutOfSyncOnly=true
    retry:
      limit: 5
      backoff:
        duration: 5s
        factor: 2
        maxDuration: 3m
OPENSHIFT_SERVERLESS_APP_EOF

      echo "OpenShift Serverless operator application created"
    EOF
  }

  triggers = {
    cluster_id                    = module.rosa_cluster_hcp.cluster_id
    admin_username                = module.rosa_cluster_hcp.cluster_admin_username
    admin_password                = module.rosa_cluster_hcp.cluster_admin_password
    api_url                       = module.rosa_cluster_hcp.cluster_api_url
    gitops_repo_url               = var.gitops_repo_url
    deploy_openshift_serverless   = local.deploy_openshift_serverless
  }
}

# Create OpenShift Service Mesh Operator Application via ArgoCD
resource "null_resource" "create_openshift_servicemesh_application" {
  count      = local.deploy_openshift_servicemesh && var.deploy_openshift_gitops ? 1 : 0
  depends_on = [time_sleep.wait_for_argocd]

  provisioner "local-exec" {
    command = <<EOF
      # Login to cluster
      oc login --username="${module.rosa_cluster_hcp.cluster_admin_username}" --password="${module.rosa_cluster_hcp.cluster_admin_password}" "${module.rosa_cluster_hcp.cluster_api_url}" --insecure-skip-tls-verify

      # Create OpenShift Service Mesh Operator Application
      oc apply -f - <<OPENSHIFT_SERVICEMESH_APP_EOF
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: openshift-servicemesh-operator
  namespace: openshift-gitops
  finalizers:
    - resources-finalizer.argocd.argoproj.io
spec:
  project: default
  source:
    repoURL: ${var.gitops_repo_url}
    targetRevision: HEAD
    path: operators/openshift-servicemesh
  destination:
    server: https://kubernetes.default.svc
    namespace: istio-system
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
      allowEmpty: false
    syncOptions:
      - CreateNamespace=true
      - RespectIgnoreDifferences=true
      - ApplyOutOfSyncOnly=true
    retry:
      limit: 5
      backoff:
        duration: 5s
        factor: 2
        maxDuration: 3m
OPENSHIFT_SERVICEMESH_APP_EOF

      echo "OpenShift Service Mesh operator application created"

      # Wait for SMCP object to be created and ready
 #     echo "Waiting for ServiceMeshControlPlane to be created..."
 #     timeout 600 bash -c 'until oc get smcp data-science-smcp -n istio-system 2>/dev/null; do echo "Waiting for SMCP..."; sleep 10; done'

      # Apply authorino patch to SMCP
 #     echo "Patching ServiceMeshControlPlane with authorino configuration..."
 #     oc patch smcp data-science-smcp --type merge -n istio-system --patch-file ${path.module}/authorino.yml

 #     echo "ServiceMeshControlPlane patched with authorino configuration"
    EOF
  }

  triggers = {
    cluster_id                      = module.rosa_cluster_hcp.cluster_id
    admin_username                  = module.rosa_cluster_hcp.cluster_admin_username
    admin_password                  = module.rosa_cluster_hcp.cluster_admin_password
    api_url                         = module.rosa_cluster_hcp.cluster_api_url
    gitops_repo_url                 = var.gitops_repo_url
    deploy_openshift_servicemesh    = local.deploy_openshift_servicemesh
    authorino_patch                 = fileexists("${path.module}/authorino.yml") ? file("${path.module}/authorino.yml") : ""
  }
}

# Create NodeFileDiscovery Operator Application via ArgoCD (GitOps Catalog)
resource "null_resource" "create_nfd_gitops_application" {
  count      = local.deploy_nfd_application && var.deploy_openshift_gitops ? 1 : 0
  depends_on = [time_sleep.wait_for_argocd]

  provisioner "local-exec" {
    command = <<-EOT
      #!/bin/bash
      set -e
      echo "Creating NodeFileDiscovery operator application via GitOps catalog..."
      
      # Login to cluster
      echo "Logging into OpenShift cluster..."
      if ! oc login --username="${module.rosa_cluster_hcp.cluster_admin_username}" --password="${module.rosa_cluster_hcp.cluster_admin_password}" "${module.rosa_cluster_hcp.cluster_api_url}" --insecure-skip-tls-verify; then
        echo "ERROR: Failed to login to OpenShift cluster"
        exit 1
      fi
      echo "Successfully logged into cluster"

      # Create NodeFileDiscovery Operator Application
      echo "Creating NodeFileDiscovery ArgoCD application..."
      if ! oc apply -f - <<NFD_GITOPS_APP_EOF
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: nfd-gitops
  namespace: openshift-gitops
  finalizers:
    - resources-finalizer.argocd.argoproj.io
spec:
  project: default
  source:
    repoURL: https://github.com/sureshgaikwad/gitops-catalog
    targetRevision: HEAD
    path: operators/node-file-discovery-operator
  destination:
    server: https://kubernetes.default.svc
    namespace: openshift-nfd
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
      allowEmpty: false
    syncOptions:
      - CreateNamespace=true
      - RespectIgnoreDifferences=true
      - ApplyOutOfSyncOnly=true
    retry:
      limit: 5
      backoff:
        duration: 5s
        factor: 2
        maxDuration: 3m
NFD_GITOPS_APP_EOF
      then
        echo "ERROR: Failed to create NodeFileDiscovery GitOps ArgoCD application"
        exit 1
      fi

      echo "NodeFileDiscovery GitOps operator application created successfully!"
    EOT
  }

  triggers = {
    cluster_id                = module.rosa_cluster_hcp.cluster_id
    admin_username            = module.rosa_cluster_hcp.cluster_admin_username
    admin_password            = module.rosa_cluster_hcp.cluster_admin_password
    api_url                   = module.rosa_cluster_hcp.cluster_api_url
    gitops_repo_url           = "https://github.com/sureshgaikwad/gitops-catalog"
    deploy_nfd_application    = local.deploy_nfd_application
  }
}

# Create NVIDIA GPU Operator Application via ArgoCD (GitOps Catalog)
resource "null_resource" "create_nvidia_gpu_gitops_application" {
  count      = local.deploy_nvidia_gpu_operator_application && var.deploy_openshift_gitops ? 1 : 0
  depends_on = [time_sleep.wait_for_argocd]

  provisioner "local-exec" {
    command = <<-EOT
      #!/bin/bash
      set -e
      echo "Creating NVIDIA GPU operator application via GitOps catalog..."
      
      # Login to cluster
      echo "Logging into OpenShift cluster..."
      if ! oc login --username="${module.rosa_cluster_hcp.cluster_admin_username}" --password="${module.rosa_cluster_hcp.cluster_admin_password}" "${module.rosa_cluster_hcp.cluster_api_url}" --insecure-skip-tls-verify; then
        echo "ERROR: Failed to login to OpenShift cluster"
        exit 1
      fi
      echo "Successfully logged into cluster"

      # Create NVIDIA GPU Operator Application
      echo "Creating NVIDIA GPU ArgoCD application..."
      if ! oc apply -f - <<NVIDIA_GPU_GITOPS_APP_EOF
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: nvidia-gpu-operator-gitops
  namespace: openshift-gitops
  finalizers:
    - resources-finalizer.argocd.argoproj.io
spec:
  project: default
  source:
    repoURL: https://github.com/sureshgaikwad/gitops-catalog
    targetRevision: HEAD
    path: operators/nvidia-gpu-operator
  destination:
    server: https://kubernetes.default.svc
    namespace: nvidia-gpu-operator
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
      allowEmpty: false
    syncOptions:
      - CreateNamespace=true
      - RespectIgnoreDifferences=true
      - ApplyOutOfSyncOnly=true
    retry:
      limit: 5
      backoff:
        duration: 5s
        factor: 2
        maxDuration: 3m
NVIDIA_GPU_GITOPS_APP_EOF
      then
        echo "ERROR: Failed to create NVIDIA GPU GitOps ArgoCD application"
        exit 1
      fi

      echo "NVIDIA GPU GitOps operator application created successfully!"
    EOT
  }

  triggers = {
    cluster_id                             = module.rosa_cluster_hcp.cluster_id
    admin_username                         = module.rosa_cluster_hcp.cluster_admin_username
    admin_password                         = module.rosa_cluster_hcp.cluster_admin_password
    api_url                                = module.rosa_cluster_hcp.cluster_api_url
    gitops_repo_url                        = "https://github.com/sureshgaikwad/gitops-catalog"
    deploy_nvidia_gpu_operator_application = local.deploy_nvidia_gpu_operator_application
  }
}
