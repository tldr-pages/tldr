# pulumi stack

> 管理堆栈并查看堆栈状态。
> 更多信息：<https://www.pulumi.com/docs/iac/cli/commands/pulumi_stack/>.

- 创建一个新堆栈：

`pulumi stack init {{stack_name}}`

- 显示堆栈状态以及资源 URN：

`pulumi stack --show-urns`

- 列出当前项目中的堆栈：

`pulumi stack ls`

- 列出所有项目中的堆栈：

`pulumi stack ls --all`

- 选择一个活动堆栈：

`pulumi stack select {{stack_name}}`

- 删除一个堆栈：

`pulumi stack rm {{stack_name}}`

- 以明文显示堆栈输出，包括密钥：

`pulumi stack output --show-secrets`

- 将堆栈状态导出到 JSON 文件：

`pulumi stack export --file {{path/to/file.json}}`