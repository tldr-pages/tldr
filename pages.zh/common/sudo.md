# sudo

> 以超级用户或其他用户身份执行单个命令。
> 更多信息：<https://www.sudo.ws/sudo.html>.

- 以超级用户身份运行命令：

`sudo {{less /var/log/syslog}}`

- 以超级用户身份使用默认编辑器编辑文件：

`sudo {{[-e|--edit]}} {{/etc/fstab}}`

- 以另一个用户和/或组的身份运行命令：

`sudo {{[-u|--user]}} {{user}} {{[-g|--group]}} {{group}} {{id -a}}`

- 在 Bash、Zsh 等中重复上一条命令，但加上 `sudo` 前缀：

`sudo !!`

- 以超级用户权限启动默认 shell 并运行登录相关文件（`.profile`、`.bash_profile` 等）：

`sudo {{[-i|--login]}}`

- 以超级用户权限启动默认 shell 但不更改环境：

`sudo {{[-s|--shell]}}`

- 以指定用户身份启动默认 shell，加载用户的环境并读取登录相关文件（`.profile`、`.bash_profile` 等）：

`sudo {{[-i|--login]}} {{[-u|--user]}} {{user}}`

- 列出调用用户允许（和禁止）的命令：

`sudo {{[-l|--list]}}`
