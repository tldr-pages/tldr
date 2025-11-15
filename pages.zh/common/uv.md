# uv

> 一个快速的 Python 软件包和项目管理器。
> 此命令也有关于其子命令的文件，例如：`tool` 和 `python`.
> 更多信息：<https://docs.astral.sh/uv/reference/cli>.

- 在当前目录中创建一个新的 Python 项目：

`uv init`

- 在具有指定名称的目录中创建一个新的 Python 项目：

`uv init {{项目名称}}`

- 向项目中添加一个新的软件包：

`uv add {{软件包}}`

- 从项目中移除一个软件包：

`uv remove {{软件包}}`

- 在项目的环境中运行一个脚本：

`uv run {{路径/到/脚本.py}}`

- 在项目的环境中运行一个命令：

`uv run {{命令}}`

- 从 `pyproject.toml` 更新项目的环境：

`uv sync`

- 为项目的依赖项创建一个锁定文件：

`uv lock`
