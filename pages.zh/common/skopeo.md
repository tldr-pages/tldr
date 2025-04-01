# skopeo

> 容器镜像管理工具。
> 提供多种命令来管理远程容器镜像。
> 更多信息：<https://github.com/containers/skopeo>.

- 检查注册表中的远程镜像：

`skopeo inspect docker://{{registry_hostname}}/{{image:tag}}`

- 列出远程镜像的可用标签：

`skopeo list-tags docker://{{registry_hostname}}/{{image}}`

- 从注册表下载镜像：

`skopeo copy docker://{{registry_hostname}}/{{image:tag}} dir:{{path/to/directory}}`

- 将镜像从一个注册表复制到另一个注册表：

`skopeo copy docker://{{source_registry}}/{{image:tag}} docker://{{destination_registry}}/{{image:tag}}`

- 从注册表删除镜像：

`skopeo delete docker://{{registry_hostname}}/{{image:tag}}`

- 登录到注册表：

`skopeo login --username {{username}} {{registry_hostname}}`
