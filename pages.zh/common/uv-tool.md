# uv 工具

> 安装并运行由 Python 包提供的命令。
> 更多信息：<https://docs.astral.sh/uv/reference/cli/#uv-tool>。

- 从一个包中运行命令，而无需安装它：

`uv tool run {{command}}`

- 全系统范围安装一个 Python 包：

`uv tool install {{package}}`

- 升级已安装的 Python 包：

`uv tool upgrade {{package}}`

- 卸载一个 Python 包：

`uv tool uninstall {{package}}`

- 列出全系统范围安装的 Python 包：

`uv tool list`