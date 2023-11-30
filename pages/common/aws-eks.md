# aws eks

> CLI for Amazon EKS (Elastic Kubernetes Service).
> More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/index.html>.

- Create an EKS Cluster:

`aws eks create-cluster --name {{cluster_name}} --role-arn {{eks_service_role_arn}} --resources-vpc-config {{subnetIds={{subnet_ids}},securityGroupIds={{security_group_ids}}}}`

- Update kubeconfig to connect to the EKS Cluster:

`aws eks update-kubeconfig --name {{cluster_name}}`

- List available EKS clusters:

`aws eks list-clusters`

- Describe EKS cluster details:

`aws eks describe-cluster --name {{cluster_name}}`

- Delete an EKS Cluster:

`aws eks delete-cluster --name {{cluster_name}}`

- List nodegroups in an EKS cluster:

`aws eks list-nodegroups --cluster-name {{cluster_name}}`

- Describe nodegroup details:

`aws eks describe-nodegroup --cluster-name {{cluster_name}} --nodegroup-name {{nodegroup_name}}`
