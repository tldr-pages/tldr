# az acr

> 使用 Azure 容器注册表管理私有注册表。
> `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/acr>.

- 创建一个托管的容器注册表：

`az acr create {{[-n|--name]}} {{registry_name}} {{[-g|--resource-group]}} {{resource_group}} --sku {{sku}}`

- 登录到一个注册表：

`az acr login {{[-n|--name]}} {{registry_name}}`

- 为 ACR 标记一个本地镜像：

`docker tag {{image_name}} {{registry_name}}.azurecr.io/{{image_name}}:{{tag}}`

- 将镜像推送到注册表：

`docker push {{registry_name}}.azurecr.io/{{image_name}}:{{tag}}`

- 从注册表拉取镜像：

`docker pull {{registry_name}}.azurecr.io/{{image_name}}:{{tag}}`

- 从注册表中删除一个镜像：

`az acr repository delete {{[-n|--name]}} {{registry_name}} --repository {{image_name}}:{{tag}}`

- 删除一个托管的容器注册表：

`az acr delete {{[-n|--name]}} {{registry_name}} {{[-g|--resource-group]}} {{resource_group}} {{[-y|--yes]}}`

- 列出注册表中的镜像：

`az acr repository list {{[-n|--name]}} {{registry_name}} --output table`
