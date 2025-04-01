# uv add

> 向 `pyproject.toml` 文件添加包依赖。
> 包的指定遵循 <https://peps.python.org/pep-0508/>。
> 更多信息：<https://docs.astral.sh/uv/reference/cli/#uv-add>。

- 添加包的最新版本：

`uv add {{package}}`

- 添加多个包：

`uv add {{package1 package2 ...}}`

- 添加具有版本要求的包：

`uv add {{package>=1.2.3}}`

- 将包添加到可选依赖组，发布时将包含这些包：

`uv add --optional {{optional}} {{package1 package2 ...}}`

- 将包添加到本地组，发布时不会包含这些包：

`uv add --group {{group}} {{package1 package2 ...}}`

- 将包添加到 dev 组，是 `--group dev` 的快捷方式：

`uv add --dev {{package1 package2 ...}}`

- 以可编辑模式添加包：

`uv add --editable {{path/to/package/}}`

- 在安装包时启用额外功能，可以多次提供：

`uv add {{package}} --extra {{extra_feature}}`