# aws ecr

> 推送、拉取和管理容器镜像。
> 更多信息：<https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/index.html>.

- 使用默认注册表对 Docker 进行身份验证（用户名为 AWS）：

`aws ecr get-login-password --region {{region}} | {{docker login}} --username AWS --password-stdin {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com`

- 创建仓库：

`aws ecr create-repository --repository-name {{repository}} --image-scanning-configuration scanOnPush={{true|false}} --region {{region}}`

- 为本地镜像打上 ECR 标签：

`docker tag {{container_name}}:{{tag}} {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/{{container_name}}:{{tag}}`

- 将镜像推送到仓库：

`docker push {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/{{container_name}}:{{tag}}`

- 从仓库中拉取镜像：

`docker pull {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/{{container_name}}:{{tag}}`

- 从仓库中删除镜像：

`aws ecr batch-delete-image --repository-name {{repository}} --image-ids imageTag={{latest}}`

- 删除仓库：

`aws ecr delete-repository --repository-name {{repository}} --force`

- 列出仓库中的镜像：

`aws ecr list-images --repository-name {{repository}}`
