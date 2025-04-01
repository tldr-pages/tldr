# nx

> 管理 `nx` 工作区。
> 更多信息：<https://nx.dev/l/r/getting-started/nx-cli>。

- 构建特定项目：

`nx build {{project}}`

- 测试特定项目：

`nx test {{project}}`

- 在特定项目上执行目标：

`nx run {{project}}:{{target}}`

- 在多个项目上执行目标：

`nx run-many --target {{target}} --projects {{project1}},{{project2}}`

- 在工作区中的所有项目上执行目标：

`nx run-many --target {{target}} --all`

- 仅在已更改的项目上执行目标：

`nx affected --target {{target}}`
