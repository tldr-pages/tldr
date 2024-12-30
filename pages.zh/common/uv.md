# uv

> 一个快速的 Python 包和项目管理器。
> 一些子命令，如 `tool` 和 `python` 有自己的使用文档。
> 更多信息：<https://docs.astral.sh/uv/reference/cli>。

- 在当前目录创建一个新的 Python 项目：

`uv init`

- 在指定名称的目录中创建一个新的 Python 项目：

`uv init {{project_name}}`

- 向项目添加一个新包：

`uv add {{package}}`

- 从项目中移除一个包：

`uv remove {{package}}`

- 在项目的环境中运行一个脚本：

`uv run {{path/to/script.py}}`

- 在项目的环境中运行一个命令：

`uv run {{command}}`

- 从 `pyproject.toml` 更新项目的环境：

`uv sync`

- 为项目的依赖项创建一个锁文件：

`uv lock`