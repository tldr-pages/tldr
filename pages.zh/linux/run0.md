# run0

> 以交互方式提升权限。
> 类似于 `sudo`，但它不是 SUID 二进制文件，身份验证通过 polkit 进行，命令是从 `systemd` 服务中调用的。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/latest/run0.html>。

- 以 root 身份运行命令：

`run0 {{command}}`

- 以其他用户和/或组身份运行命令：

`run0 {{-u|--user}} {{用户名|uid}} {{-g|--group}} {{组名|gid}} {{command}}`