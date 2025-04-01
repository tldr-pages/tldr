# pulumi

> 使用熟悉的编程语言在任何云上定义基础架构。
> 某些子命令（如 `up`）有其自己的使用文档。
> 更多信息：<https://www.pulumi.com/docs/iac/cli/>.

- 使用模板创建新项目：

`pulumi new`

- 使用独立的部署目标创建新堆栈：

`pulumi stack init`

- 交互式地配置变量（例如密钥、区域等）：

`pulumi config`

- 预览并部署程序和/或基础架构的更改：

`pulumi up`

- 预览部署更改但不执行（干运行）：

`pulumi preview`

- 销毁程序及其基础架构：

`pulumi destroy`

- 在本地使用 Pulumi，独立于 Pulumi Cloud：

`pulumi login {{[-l|--local]}}`