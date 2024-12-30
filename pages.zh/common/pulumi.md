# pulumi

> 使用熟悉的编程语言定义任何云上的基础设施。
> 一些子命令，例如 `up`，有其自己的使用文档。
> 更多信息：<https://www.pulumi.com/docs/cli>。

- 使用模板创建一个新项目：

`pulumi new`

- 使用隔离的部署目标创建一个新堆栈：

`pulumi stack init`

- 交互式配置变量（例如，密钥、区域等）：

`pulumi config`

- 预览并部署对程序和/或基础设施的更改：

`pulumi up`

- 在不执行它们的情况下预览部署更改（干运行）：

`pulumi preview`

- 销毁一个程序及其基础设施：

`pulumi destroy`

- 在本地使用 Pulumi，独立于 Pulumi Cloud：

`pulumi login {{-l|--local}}`