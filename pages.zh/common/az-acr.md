# az acr

> 使用 Azure 容器注册表管理私有注册表。
> 作为 `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/acr>.

- 创建一个托管的容器注册表：

`az acr create --name {{registry_name}} --resource-group {{resource_group}} --sku {{sku}}`

- 登录到注册表：

`az acr login --name {{registry_name}}`

- 为本地镜像添加 ACR 标记：

`docker tag {{image_name}} {{registry_name}}.azurecr.io/{{image_name}}:{{tag}}`

- 将镜像推送到注册表：

`docker push {{registry_name}}.azurecr.io/{{image_name}}:{{tag}}`

- 从注册表拉取镜像：

`docker pull {{registry_name}}.azurecr.io/{{image_name}}:{{tag}}`

- 从注册表中删除镜像：

`az acr repository delete --name {{registry_name}} --repository {{image_name}}:{{tag}}`

- 删除托管的容器注册表：

`az acr delete --name {{registry_name}} --resource-group {{resource_group}} --yes`

- 列出注册表中的镜像：

`az acr repository list --name {{registry_name}} --output table`