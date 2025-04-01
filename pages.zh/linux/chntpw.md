# chntpw

> 一个可以编辑 Windows 注册表、重置用户密码、通过修改 Windows SAM 将用户提升为管理员的工具。
> 使用如 Kali Linux 之类的启动盘启动目标机器，并以提升的权限运行。
> 更多信息：<https://pogostick.net/~pnh/ntpasswd>。

- 列出 SAM 文件中的所有用户：

`chntpw -l {{path/to/sam_file}}`

- 交互式编辑用户：

`chntpw -u {{username}} {{path/to/sam_file}}`

- 交互式使用 chntpw：

`chntpw -i {{path/to/sam_file}}`
