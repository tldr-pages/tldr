# getconf

> 从您的Linux系统获取配置值。
> 更多信息：<https://manned.org/getconf.1>。

- 列出所有可用的配置值：

`getconf -a`

- 列出特定目录的配置值：

`getconf -a {{path/to/directory}}`

- 检查系统是32位还是64位：

`getconf LONG_BIT`

- 检查当前用户可以同时运行多少个进程：

`getconf CHILD_MAX`

- 列出每个配置值，然后使用`grep`命令查找模式（即每个包含MAX的值）：

`getconf -a | grep MAX`