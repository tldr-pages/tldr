# runuser

> 以不同用户和组的身份运行命令，无需输入密码（需要root权限）。
> 更多信息：<https://manned.org/runuser>。

- 以不同用户身份运行命令：

`runuser {{user}} -c '{{command}}'`

- 以不同用户和组身份运行命令：

`runuser {{user}} -g {{group}} -c '{{command}}'`

- 以特定用户身份启动登录shell：

`runuser {{user}} -l`

- 指定一个shell来运行，而不是默认的shell（也适用于登录）：

`runuser {{user}} -s {{/bin/sh}}`

- 保留root的整个环境（仅在未指定`--login`时）：

`runuser {{user}} --preserve-environment -c '{{command}}'`