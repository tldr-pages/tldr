# tmt

> 创建、运行和调试测试的测试管理工具。
> 诸如`运行`、`尝试`等子命令，均有相应的用法文档。
> 更多信息：<https://tmt.readthedocs.io/en/stable/examples.html>.

- 列举可用的测试、计划和用户故事：

`tmt`

- 初始化测试管理工具的文件/项目结构：

`tmt init`

- 基于模板和链接创建新的测试：

`tmt test create --template {{beakerlib}} --link {{verifies:issue#1234}}`

- 列出可用的测试、计划和用户故事：

`tmt {{test|plan|story}} ls {{pattern}}`

- 在给定的上下文中显示详细的测试元数据：

`tmt --context {{arch=aarch64}} test show`

- 根据说明书验证测试管理工具文件的有效性：

`tmt lint`

- 使用筛选条件：

`tmt tests ls --filter {{tag:foo}} --filter {{tier:0}}`

- 显示帮助：

`tmt --help`
