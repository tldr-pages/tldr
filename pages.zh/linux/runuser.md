# runuser

> 以特定用户和组的身份运行命令，无需输入密码（需要 root 权限）。
> 更多信息：<https://manned.org/runuser>。

- 以不同用户身份运行命令：

`runuser {{user}} {{[-c|--command]}} '{{command}}'`

- 以不同用户和组的身份运行命令：

`runuser {{user}} {{[-g|--group]}} {{group}} {{[-c|--command]}} '{{command}}'`

- 以特定用户身份启动登录 shell：

`runuser {{user}} {{[-l|--login]}}`

- 指定运行的 shell 而不是默认 shell（登录时也适用）：

`runuser {{user}} {{[-s|--shell]}} {{/bin/sh}}`

- 保留 root 的整个环境（仅在未指定 `--login` 时有效）：

`runuser {{user}} {{[-p|--preserve-environment]}} {{[-c|--command]}} '{{command}}'`
