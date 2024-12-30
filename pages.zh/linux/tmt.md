# tmt

> 测试管理工具，用于创建、运行和调试测试。
> 一些子命令如 `run`、`try` 等有其自己的使用文档。
> 更多信息：<https://tmt.readthedocs.io>。

- 列出可用的测试、计划和故事：

`tmt`

- 初始化 tmt 文件/项目结构：

`tmt init`

- 使用模板和链接创建新测试：

`tmt test create --template {{beakerlib}} --link {{verifies:issue#1234}}`

- 列出可用的测试、计划或故事：

`tmt {{test|plan|story}} ls {{pattern}}`

- 在给定上下文中显示详细的测试元数据：

`tmt --context {{arch=aarch64}} test show`

- 根据规范验证 tmt 文件：

`tmt lint`

- 使用过滤器：

`tmt tests ls --filter {{tag:foo}} --filter {{tier:0}}`

- 显示帮助信息：

`tmt --help`