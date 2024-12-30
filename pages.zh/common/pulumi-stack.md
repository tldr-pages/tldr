# pulumi 堆栈

> 管理堆栈并查看堆栈状态。
> 更多信息：<https://www.pulumi.com/docs/iac/cli/commands/pulumi_stack/>

- 创建一个新的堆栈：

`pulumi stack init {{stack_name}}`

- 查看堆栈状态：

`pulumi stack`

- 列出当前项目中的堆栈：

`pulumi stack ls`

- 列出所有项目中的堆栈：

`pulumi stack ls --all`

- 选择一个活动堆栈：

`pulumi stack select {{stack_name}}`

- 以明文形式显示堆栈输出，包括机密：

`pulumi stack output --show-secrets`

- 将堆栈状态导出到 JSON 文件：

`pulumi stack export --file {{path/to/file.json}}`

- 显示帮助信息：

`pulumi stack --help`