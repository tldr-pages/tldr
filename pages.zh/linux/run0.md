# run0

> 以交互方式提升权限。
> 与 `sudo` 类似，但它不是一个 SUID 二进制文件，认证通过 polkit 进行，命令从 `systemd` 服务中调用。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/latest/run0.html>.

- 以 root 身份运行命令：

`run0 {{command}}`

- 以其他用户和/或组的身份运行命令：

`run0 {{[-u|--user]}} {{username|uid}} {{[-g|--group]}} {{group_name|gid}} {{command}}`