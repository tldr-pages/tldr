# gcrane

> 容器镜像管理工具。
> 此工具实现了 `crane` 命令的一个超集，并增加了特定于 `gcr.io` 的额外命令。
> 一些子命令如 `append`、`auth`、`copy` 等有自己的使用文档，可以在 `crane` 中找到。
> 一些子命令如 `completion`、`gc`、`help` 是特定于 gcrane 的，并有自己的使用文档。
> 更多信息：<https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>。

- 执行 `gcrane` 子命令：

`gcrane {{subcommand}}`

- 允许推送不可分发（外部）层：

`gcrane --allow-nondistributable-artifacts {{subcommand}}`

- 允许在不使用 TLS 的情况下获取镜像引用：

`gcrane --insecure {{subcommand}}`

- 以 os/arch{{/variant}}{{:osversion}} 的形式指定平台（例如：linux/amd64）。 （默认是所有平台）：

`gcrane --platform {{platform}} {{subcommand}}`

- 启用调试日志：

`gcrane {{-v|--verbose}} {{subcommand}}`

- 显示帮助信息：

`gcrane {{-h|--help}}`