# uv tree

> 以树状格式显示项目依赖关系。
> 更多信息：<https://docs.astral.sh/uv/reference/cli/#uv-tree>.

- 显示当前环境的依赖树：

`uv tree`

- 显示所有环境的依赖树：

`uv tree --universal`

- 显示到指定深度的依赖树：

`uv tree {{[-d|--depth]}} {{n}}`

- 显示所有过时包的最新可用版本：

`uv tree --outdated`

- 排除开发组的依赖：

`uv tree --no-dev`

- 显示倒置的树，将子节点显示为依赖项而非依赖：

`uv tree --invert`
