# aws eks

> Gestisce addon, cluster e gruppi di nodi di Amazon Elastic Kubernetes Service (EKS).
> Amazon EKS è un servizio per eseguire facilmente Kubernetes su AWS.
> Maggiori informazioni: <https://docs.aws.amazon.com/cli/latest/reference/eks/>.

- Crea un cluster EKS:

`aws eks create-cluster --name {{nome_cluster}} --role-arn {{arn_eks_service_role}} --resources-vpc-config subnetIds={{subnet_ids}},securityGroupIds={{security_group_ids}}`

- Aggiorna kubeconfig per connettersi al cluster EKS:

`aws eks update-kubeconfig --name {{nome_cluster}}`

- Elenca i cluster EKS disponibili:

`aws eks list-clusters`

- Descrivi i dettagli del cluster EKS:

`aws eks describe-cluster --name {{nome_cluster}}`

- Elimina un cluster EKS:

`aws eks delete-cluster --name {{nome_cluster}}`

- Elenca i nodegroup in un cluster EKS:

`aws eks list-nodegroups --cluster-name {{nome_cluster}}`

- Descrivi i dettagli del nodegroup:

`aws eks describe-nodegroup --cluster-name {{nome_cluster}} --nodegroup-name {{nome_nodegroup}}`
