# aws eks

> CLI for AWS eks.
> More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/index.html?highlight=eks>.

- Create an EKS Cluster:

`aws eks create-cluster --name {{cluster-name}} --role-arn {{eks-service-role-arn}} --resources-vpc-config subnetIds={{subnet-ids}},securityGroupIds={{security-group-ids}}`

- Update kubeconfig to connect to the EKS Cluster:

`aws eks update-kubeconfig --name {{cluster-name}}`

- List available EKS clusters:

`aws eks list-clusters`

- Describe EKS cluster details:

`aws eks describe-cluster --name {{cluster-name}}`

- Delete an EKS Cluster:

`aws eks delete-cluster --name {{cluster-name}}`

- List nodegroups in an EKS cluster:

`aws eks list-nodegroups --cluster-name {{cluster-name}}`

- Describe nodegroup details:

`aws eks describe-nodegroup --cluster-name {{cluster-name}} --nodegroup-name {{nodegroup-name}}`
