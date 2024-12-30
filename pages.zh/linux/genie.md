# genie

> 设置并使用“瓶子”命名空间在 WSL（Windows 子系统 Linux）下运行 systemd。
> 要从 Windows 而不是已经运行的发行版中运行这些命令，请在前面加上 `wsl`。
> 更多信息：<https://github.com/arkane-systems/genie>。

- 初始化瓶子（首次运行时）：

`genie -i`

- 在瓶子内运行登录 shell：

`genie -s`

- 在瓶子内运行指定命令：

`genie -c {{command}}`