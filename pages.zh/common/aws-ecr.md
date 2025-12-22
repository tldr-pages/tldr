# aws ecr

> 推送、拉取和管理容器镜像。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/ecr/>.

- 使用默认注册表对 Docker 进行身份验证（用户名是 AWS）：

`aws ecr get-login-password --region {{区域}} | {{docker login}} --username AWS --password-stdin {{AWS_账户_ID}}.dkr.ecr.{{区域}}.amazonaws.com`

- 创建一个仓库：

`aws ecr create-repository --repository-name {{仓库}} --image-scanning-configuration scanOnPush={{true|false}} --region {{区域}}`

- 为 ECR 标记本地镜像：

`docker tag {{容器名称}}:{{标签}} {{AWS_账户_ID}}.dkr.ecr.{{区域}}.amazonaws.com/{{容器名称}}:{{标签}}`

- 将镜像推送到仓库：

`docker push {{AWS_账户_ID}}.dkr.ecr.{{区域}}.amazonaws.com/{{容器名称}}:{{标签}}`

- 从仓库拉取镜像：

`docker pull {{AWS_账户_ID}}.dkr.ecr.{{区域}}.amazonaws.com/{{容器名称}}:{{标签}}`

- 从仓库中删除镜像：

`aws ecr batch-delete-image --repository-name {{仓库}} --image-ids imageTag={{latest}}`

- 删除一个仓库：

`aws ecr delete-repository --repository-name {{仓库}} --force`

- 列出仓库中的镜像：

`aws ecr list-images --repository-name {{仓库}}`
