# lxc profile

> 管理 LXD 容器的配置文件。
> 更多信息：<https://linuxcontainers.org/lxd/docs/master/profiles>。

- 列出所有可用的配置文件：

`lxc profile list`

- 显示特定配置文件的配置：

`lxc profile show {{profile_name}}`

- 使用默认编辑器编辑特定配置文件：

`lxc profile edit {{profile_name}}`

- 从文件中导入配置值以编辑特定配置文件：

`lxc profile edit {{profile_name}} < {{config.yaml}}`

- 使用特定配置文件启动新容器：

`lxc launch {{container_image}} {{container_name}} --profile {{profile1}} --profile {{profile2}}`

- 更改正在运行的容器的配置文件：

`lxc profile assign {{container_name}} {{profile1,profile2}}`