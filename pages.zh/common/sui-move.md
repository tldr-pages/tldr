# Sui Move

> 使用 Move 源代码。
> 更多信息：<https://docs.sui.io/references/cli/move>。

- 在指定文件夹中创建一个新的 Move 项目：

`sui move new {{project_name}}`

- 在当前目录中测试 Move 项目：

`sui move test`

- 进行覆盖测试并获取摘要：

`sui move test --coverage; sui move coverage summary`

- 找出代码中哪些部分被测试覆盖（即解释覆盖结果）：

`sui move coverage source --module {{module_name}}`

- 在当前目录中构建 Move 项目：

`sui move build`

- 从指定路径构建 Move 项目：

`sui move build --path {{path}}`

- 将提供路径的包迁移到 Move 2024：

`sui move migrate {{path}}`