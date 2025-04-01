# hatch

> 现代、可扩展的 Python 项目管理工具。
> 参见: `poetry`。
> 更多信息: <https://hatch.pypa.io/latest/cli/reference/>。

- 创建一个新的 Hatch 项目:

`hatch new {{project_name}}`

- 为现有项目初始化 Hatch:

`hatch new --init`

- 构建一个 Hatch 项目:

`hatch build`

- 删除构建产物:

`hatch clean`

- 使用 `pyproject.toml` 文件中定义的依赖项创建默认环境:

`hatch env create`

- 以表格形式显示环境依赖项:

`hatch dep show table`