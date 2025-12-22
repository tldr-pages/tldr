# az container

> 管理 Azure 容器实例。
> 属于 `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/container>.

- 在容器组中创建一个容器：

`az container create {{[-g|--resource-group]}} {{资源组}} {{[-n|--name]}} {{名称}} --image {{镜像名称}} {{[-os|--os-type]}} {{windows|linux}} --cpu {{CPU 核心数}} --memory {{内存（GB）}}`

- 在容器组中正在运行的容器内执行命令：

`az container exec {{[-g|--resource-group]}} {{资源组}} {{[-n|--name]}} {{容器组名称}} --exec-command "{{命令}}"`

- 查看容器组中某个容器的日志：

`az container logs {{[-n|--name]}} {{名称}} {{[-g|--resource-group]}} {{资源组}}`

- 获取容器组的详细信息：

`az container show {{[-n|--name]}} {{名称}} {{[-g|--resource-group]}} {{资源组}}`

- 启动容器组中的所有容器：

`az container start {{[-n|--name]}} {{名称}} {{[-g|--resource-group]}} {{资源组}}`

- 停止容器组中的所有容器：

`az container stop {{[-n|--name]}} {{名称}} {{[-g|--resource-group]}} {{资源组}}`

- 删除一个容器组：

`az container delete {{[-n|--name]}} {{名称}} {{[-g|--resource-group]}} {{资源组}}`
