# sysctl

> 列出并更改内核运行时变量。
> 更多信息：<https://manned.org/sysctl.8>。

- 显示所有可用变量及其值：

`sysctl -a`

- 设置可更改的内核状态变量：

`sysctl -w {{section.tunable}}={{value}}`

- 获取当前打开的文件句柄：

`sysctl fs.file-nr`

- 获取同时打开文件的限制：

`sysctl fs.file-max`

- 应用来自 `/etc/sysctl.conf` 的更改：

`sysctl -p`
