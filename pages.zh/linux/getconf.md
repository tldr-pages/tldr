# getconf

> 从您的 Linux 系统中获取配置值。
> 更多信息：<https://manned.org/getconf.1>.

- 列出所有可用的配置值：

`getconf -a`

- 列出特定目录的配置值：

`getconf -a {{path/to/directory}}`

- 检查系统是 32 位还是 64 位：

`getconf LONG_BIT`

- 检查当前用户可以同时运行的进程数量：

`getconf CHILD_MAX`

- 列出所有配置值并使用 `grep` 命令查找模式（例如，所有包含 MAX 的值）：

`getconf -a | grep MAX`
