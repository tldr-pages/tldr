# sudo

> 以超级用户或其他用户身份执行单个命令。
> 更多信息： <https://www.sudo.ws/sudo.html>.

- 以超级用户身份运行命令：

`sudo {{less /var/log/syslog}}`

- 以超级用户身份使用默认编辑器编辑文件：

`sudo {{[-e|--edit]}} {{/etc/fstab}}`

- 以其他用户和(或)组的身份运行命令：

`sudo {{[-u|--user]}} {{用户}} {{[-g|--group]}} {{组}} {{id -a}}`

- 重复执行上一条以“sudo”为前缀的命令（仅适用于Bash、Zsh等）：

`sudo !!`

- 以超级用户权限启动默认Shell，并运行登录特定的文件（如`.profile`、`.bash_profile`等）：

`sudo {{[-i|--login]}}`

- 在不改变环境的情况下，使用超级用户权限启动默认的shell：

`sudo {{[-s|--shell]}}`

- 以指定用户的身份启动默认的shell，加载该用户的环境变量并读取登录特定的文件（如`.profile`、`.bash_profile`等）：

`sudo {{[-i|--login]}} {{[-u|--user]}} {{用户}}`

- 列出调用用户允许（和禁止）的命令：

`sudo {{[-ll|--list --list]}}`
