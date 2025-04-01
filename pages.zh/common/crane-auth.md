# crane auth

> 登录或访问凭证。
> 更多信息：<https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_auth.md>.

- 执行 `crane auth` 子命令：

`crane auth {{subcommand}}`

- 实现凭证助手：

`crane auth get {{registry_address}} {{[-h|--help]}}`

- 登录到一个仓库：

`crane auth login {{registry_address}} {{[-h|--help]}} {{[-p|--password]}} {{password}} {{-password-stdin}} {{[-u|--username]}} {{username}}`

- 从仓库登出：

`crane auth logout {{registry_address}} {{[-h|--help]}}`

- 获取远程仓库的令牌：

`crane auth token {{registry_address}} {{[-H|--header]}} {{[-h|--help]}} {{[-m|--mount]}} {{scope1 scope2 ...}} --push`

- 显示帮助：

`crane auth {{[-h|--help]}}`
