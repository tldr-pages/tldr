# genie

> 设置并使用一个 "bottle" 命名空间以在 WSL（Windows Subsystem for Linux）下运行 systemd。
> 如果从 Windows 而不是已经运行的发行版中运行这些命令，请在它们前面加上 `wsl`。
> 更多信息：<https://github.com/arkane-systems/genie>。

- 初始化 bottle（启动时运行一次）：

`genie -i`

- 在 bottle 内运行登录 shell：

`genie -s`

- 在 bottle 内运行指定的命令：

`genie -c {{command}}`
