# crane auth

> 登录或访问凭据。
> 更多信息：<https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_auth.md>。

- 执行 `crane auth` 子命令：

`crane auth {{subcommand}}`

- 实现凭据助手：

`crane auth get {{registry_address}} {{-h|--help}}`

- 登录到注册表：

`crane auth login {{registry_address}} {{-h|--help}} {{-p|--password}} {{password}} {{-password-stdin}} {{-u|--username}} {{username}}`

- 从注册表注销：

`crane auth logout {{registry_address}} {{-h|--help}}`

- 为远程仓库检索令牌：

`crane auth token {{registry_address}} {{-H|--header}} {{-h|--help}} {{-m|--mount}} {{scope1 scope2 ...}} --push`

- 显示帮助信息：

`crane auth {{-h|--help}}`