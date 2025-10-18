# uv sync

> 更新项目环境，来匹配锁文件 (lockfile).
> 更多信息：<https://docs.astral.sh/uv/reference/cli/#uv-sync>.

- 将项目环境与锁文件同步：

`uv sync`

- 同步，并且包含所有的可选依赖：

`uv sync --all-extras`

- 同步，包含特定的可选依赖：

`uv sync --extra {{可选依赖_名称}}`

- 仅同步开发环境依赖：

`uv sync --only-dev`

- 同步，但排除开发环境依赖：

`uv sync --no-dev`

- 同步特定的依赖组：

`uv sync --group {{依赖组_名称}}`

- 检查环境是否已经同步（不会做出更改）：

`uv sync --check`

- 预览同步会做出的更改，但是不执行：

`uv sync --dry-run`
