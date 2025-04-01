# foreman

> 管理基于 Procfile 的应用程序。
> 更多信息：<https://manned.org/foreman>.

- 使用当前目录中的 Procfile 启动应用程序：

`foreman start`

- 使用指定的 Procfile 启动应用程序：

`foreman start -f {{Procfile}}`

- 启动特定的应用程序进程：

`foreman start {{process}}`

- 验证 Procfile 格式：

`foreman check`

- 使用进程环境运行一次性命令：

`foreman run {{command}}`

- 启动所有进程，但不包括名为 "worker" 的进程：

`foreman start -m all=1,{{worker}}=0`
