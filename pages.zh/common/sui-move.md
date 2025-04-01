# sui move

> 操作 Move 源代码。
> 更多信息：<https://docs.sui.io/references/cli/move>.

- 在指定文件夹中创建一个新的 Move 项目：

`sui move new {{project_name}}`

- 测试当前目录中的 Move 项目：

`sui move test`

- 使用覆盖率测试并获取汇总：

`sui move test --coverage; sui move coverage summary`

- 查找代码的哪些部分被测试覆盖（即解释覆盖率结果）：

`sui move coverage source --module {{module_name}}`

- 构建当前目录中的 Move 项目：

`sui move build`

- 从指定路径构建 Move 项目：

`sui move build --path {{path}}`

- 将指定路径的包迁移到 Move 2024：

`sui move migrate {{path}}`
