# wsl

> 管理 Windows 子系统 Linux。
> 更多信息：<https://learn.microsoft.com/windows/wsl/reference>。

- 启动一个 Linux shell（在默认发行版中）：

`wsl {{shell_command}}`

- 无需使用 shell 运行 Linux 命令：

`wsl --exec {{command}} {{command_arguments}}`

- 指定特定的发行版：

`wsl --distribution {{distribution}} {{shell_command}}`

- 列出可用的发行版：

`wsl --list`

- 将发行版导出为 `.tar` 文件：

`wsl --export {{distribution}} {{path\to\distro_file.tar}}`

- 从 `.tar` 文件导入发行版：

`wsl --import {{distribution}} {{path\to\install_location}} {{path/to/distro_file.tar}}`

- 更改指定发行版使用的 wsl 版本：

`wsl --set-version {{distribution}} {{version}}`

- 关闭 Windows 子系统 Linux：

`wsl --shutdown`