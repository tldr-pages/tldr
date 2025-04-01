# poetry

> 管理 Python 包和依赖项。
> 参见: `asdf`。
> 更多信息: <https://python-poetry.org/docs/cli/>。

- 在指定名称的目录中创建一个新的 Poetry 项目：

`poetry new {{project_name}}`

- 安装并添加一个依赖项及其子依赖项到当前目录的 `pyproject.toml` 文件中：

`poetry add {{dependency}}`

- 使用当前目录的 `pyproject.toml` 文件安装项目依赖项：

`poetry install`

- 交互式初始化当前目录为一个新的 Poetry 项目：

`poetry init`

- 获取所有依赖项的最新版本并更新 `poetry.lock`：

`poetry update`

- 在项目的虚拟环境中执行命令：

`poetry run {{command}}`

- 在 `pyproject.toml` 中提升项目的版本：

`poetry version {{patch|minor|major|prepatch|preminor|premajor|prerelease}}`

- 在项目的虚拟环境中启动一个新的 shell：

`poetry shell`
