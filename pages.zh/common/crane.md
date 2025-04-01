# crane

> 容器镜像管理工具。
> 一些子命令如 `pull`、`push`、`copy` 等有自己的使用文档。
> 更多信息：<https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane.md/>。

- 执行 `crane` 子命令：

`crane {{subcommand}}`

- 允许推送不可分发（外部）层：

`crane --allow-nondistributable-artifacts {{subcommand}}`

- 允许在不使用 TLS 的情况下获取镜像引用：

`crane --insecure {{subcommand}}`

- 指定平台形式为 os/arch{{/variant}}{{:osversion}}（例如 linux/amd64）。默认为所有平台：

`crane --platform {{platform}} {{subcommand}}`

- 为子命令启用调试日志：

`crane {{[-v|--verbose]}} {{subcommand}}`

- 显示子命令的帮助信息：

`crane {{[-h|--help]}} {{subcommand}}`