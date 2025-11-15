# aws eks

> Amazon Elastic Kubernetes Service (EKS) 애드온, 클러스터 및 노드 그룹 관리.
> Amazon EKS는 AWS에서 Kubernetes를 쉽게 실행하기 위한 서비스.
> 더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/index.html>.

- EKS 클러스터 생성:

`aws eks create-cluster --name {{클러스터_이름}} --role-arn {{eks_service_role_arn}} --resources-vpc-config subnetIds={{subnet_ids}},securityGroupIds={{security_group_ids}}`

- EKS 클러스터에 연결하기 위한 kubeconfig를 업데이트:

`aws eks update-kubeconfig --name {{클러스터_이름}}`

- 사용 가능한 EKS 클러스터 목록 나열:

`aws eks list-clusters`

- Describe EKS 클러스터 세부정보 나열:

`aws eks describe-cluster --name {{클러스터_이름}}`

- EKS 클러스터 삭제:

`aws eks delete-cluster --name {{클러스터_이름}}`

- EKS 클러스터의 노드그룹 나열:

`aws eks list-nodegroups --cluster-name {{클러스터_이름}}`

- 노드 그룹 세부 정보 표시:

`aws eks describe-nodegroup --cluster-name {{클러스터_이름}} --nodegroup-name {{노드그룹_이름}}`
