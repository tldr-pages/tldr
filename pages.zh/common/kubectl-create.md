# kubectl create

> 从文件或标准输入创建资源。
> 更多信息：<https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#create>.

- 使用资源定义文件创建资源：

`kubectl create -f {{path/to/file.yml}}`

- 从标准输入创建资源：

`kubectl create -f -`

- 创建部署：

`kubectl create deployment {{deployment_name}} --image={{image}}`

- 创建带有副本的部署：

`kubectl create deployment {{deployment_name}} --image={{image}} --replicas={{number_of_replicas}}`

- 创建服务：

`kubectl create service {{service_type}} {{service_name}} --tcp={{port}}:{{target_port}}`

- 创建命名空间：

`kubectl create namespace {{namespace_name}}`
