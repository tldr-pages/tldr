# ավս եկս

> Կառավարեք Amazon Elastic Kubernetes Service (EKS) հավելումները, կլաստերները և հանգույցների խմբերը:.
> Amazon EKS-ը Kubernetes-ը AWS-ով հեշտությամբ գործարկելու ծառայություն է:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/eks/>:.

- Ստեղծեք EKS կլաստեր.:

`aws eks create-cluster --name {{cluster_name}} --role-arn {{eks_service_role_arn}} --resources-vpc-config subnetIds={{subnet_ids}},securityGroupIds={{security_group_ids}}`

- Թարմացրեք kubeconfig-ը՝ EKS կլաստերին միանալու համար.:

`aws eks update-kubeconfig --name {{cluster_name}}`

- Ցուցակեք մատչելի EKS կլաստերները.:

`aws eks list-clusters`

- Նկարագրեք EKS կլաստերի մանրամասները.:

`aws eks describe-cluster --name {{cluster_name}}`

- Ջնջել EKS կլաստերը.:

`aws eks delete-cluster --name {{cluster_name}}`

- Նշեք հանգույցների խմբերը EKS կլաստերում.:

`aws eks list-nodegroups --cluster-name {{cluster_name}}`

- Նկարագրեք հանգույցների խմբի մանրամասները.:

`aws eks describe-nodegroup --cluster-name {{cluster_name}} --nodegroup-name {{nodegroup_name}}`
