# wsl

> 从命令行管理适用于 Linux 的 Windows 子系统。
> 更多信息：<https://docs.microsoft.com/windows/wsl/reference>.

- 启动 Linux Shell（在默认发行版中）：

`wsl {{shell_命令}}`

- 在不使用 Shell 的情况下运行 Linux 命令：

`wsl --exec {{命令}} {{命令参数}}`

- 指定特定的发行版：

`wsl --distribution {{发行版}} {{shell_命令}}`

- 列出所有可用发行版：

`wsl --list`

- 将发行版导出到 .tar 文件：

`wsl --export {{发行版}} {{路径/distro_fs.tar}}`

- 从 .tar 文件导入发行版：

`wsl --import {{发行版}} {{路径/安装位置}} {{路径/distro_fs.tar}}`

- 更改指定发行版的版本：

`wsl --set-version {{发行版}} {{版本}}`

- 关闭适用于 Linux 的 Windows 子系统：

`wsl --shutdown`
