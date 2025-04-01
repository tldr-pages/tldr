# lxc

> 使用 lxd REST API 管理 Linux 容器。
> 任何容器名称或模式都可以用远程服务器的名称作为前缀。
> 更多信息：<https://manned.org/lxc>。

- 列出与字符串匹配的本地容器。省略字符串则列出所有本地容器：

`lxc list {{match_string}}`

- 列出与字符串匹配的镜像。省略字符串则列出所有镜像：

`lxc image list [{{remote}}:]{{match_string}}`

- 从镜像创建新容器：

`lxc init [{{remote}}:]{{image}} {{container}}`

- 启动容器：

`lxc start [{{remote}}:]{{container}}`

- 停止容器：

`lxc stop [{{remote}}:]{{container}}`

- 显示容器的详细信息：

`lxc info [{{remote}}:]{{container}}`

- 对容器进行快照：

`lxc snapshot [{{remote}}:]{{container}} {{snapshot}}`

- 在容器内执行特定命令：

`lxc exec [{{remote}}:]{{container}} {{command}}`
