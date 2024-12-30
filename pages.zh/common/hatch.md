# hatch

> 现代、可扩展的 Python 项目管理工具。
> 另见：`poetry`。
> 更多信息：<https://hatch.pypa.io/latest/cli/reference/>.

- 创建一个新的 Hatch 项目：

`hatch new {{project_name}}`

- 为现有项目初始化 Hatch：

`hatch new --init`

- 构建一个 Hatch 项目：

`hatch build`

- 移除构建产物：

`hatch clean`

- 创建一个包含在 `pyproject.toml` 文件中定义的依赖项的默认环境：

`hatch env create`

- 以表格形式显示环境依赖项：

`hatch dep show table`