# skopeo

> 容器镜像管理工具箱。
> 提供各种实用命令来管理远程容器镜像。
> 更多信息：<https://github.com/containers/skopeo>。

- 从注册中心检查远程镜像：

`skopeo inspect docker://{{registry_hostname}}/{{image:tag}}`

- 列出远程镜像的可用标签：

`skopeo list-tags docker://{{registry_hostname}}/{{image}}`

- 从注册中心下载镜像：

`skopeo copy docker://{{registry_hostname}}/{{image:tag}} dir:{{path/to/directory}}`

- 从一个注册中心复制镜像到另一个注册中心：

`skopeo copy docker://{{source_registry}}/{{image:tag}} docker://{{destination_registry}}/{{image:tag}}`

- 从注册中心删除镜像：

`skopeo delete docker://{{registry_hostname}}/{{image:tag}}`

- 登录到注册中心：

`skopeo login --username {{username}} {{registry_hostname}}`