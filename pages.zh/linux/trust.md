# trust

> 操作信任策略存储。
> 更多信息：<https://manned.org/trust>.

- 列出信任策略存储中的项目：

`trust list`

- 列出信任策略存储中特定项目的详细信息：

`trust list --filter={{blocklist|ca-anchors|certificates|trust-policy}}`

- 在信任策略存储中存储特定的信任锚：

`trust anchor {{path/to/certificate.crt}}`

- 从信任策略存储中移除特定的信任锚：

`trust anchor --remove {{path/to/certificate.crt}}`

- 从共享信任策略存储中导出信任策略：

`trust extract --format=x509-directory --filter=ca-anchors {{path/to/directory}}`

- 显示子命令的帮助信息：

`trust {{subcommand}} --help`