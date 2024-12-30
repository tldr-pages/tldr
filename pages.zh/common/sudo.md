# sudo

> 以超级用户或其他用户的身份执行单个命令。
> 更多信息：<https://www.sudo.ws/sudo.html>。

- 以超级用户身份运行命令：

`sudo {{less /var/log/syslog}}`

- 使用默认编辑器以超级用户身份编辑文件：

`sudo --edit {{/etc/fstab}}`

- 以其他用户和/或组的身份运行命令：

`sudo --user={{user}} --group={{group}} {{id -a}}`

- 重复上一个以 `sudo` 为前缀的命令（仅在 Bash、Zsh 等中）：

`sudo !!`

- 以超级用户权限启动默认 shell，并运行登录特定文件（`.profile`、`.bash_profile` 等）：

`sudo --login`

- 以超级用户权限启动默认 shell，而不更改环境：

`sudo --shell`

- 以指定用户的身份启动默认 shell，加载用户的环境并读取登录特定文件（`.profile`、`.bash_profile` 等）：

`sudo --login --user={{user}}`

- 列出调用用户的允许（和禁止）命令：

`sudo --list`