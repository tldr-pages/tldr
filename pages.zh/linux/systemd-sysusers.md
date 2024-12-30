# systemd-sysusers

> 创建系统用户和组。
> 如果未指定配置文件，则使用 `sysusers.d` 目录中的文件。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/systemd-sysusers.html>。

- 从特定配置文件创建用户和组：

`systemd-sysusers {{path/to/file}}`

- 处理配置文件并打印将要执行的操作，而不实际执行任何操作：

`systemd-sysusers --dry-run {{path/to/file}}`

- 打印所有配置文件的内容（在每个文件之前，文件名以注释形式打印）：

`systemd-sysusers --cat-config`