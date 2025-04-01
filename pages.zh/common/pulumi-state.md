# pulumi state

> 编辑当前堆栈的状态。
> 更多信息：<https://www.pulumi.com/docs/iac/cli/commands/pulumi_state/>。

- 从当前堆栈的状态中删除资源：

`pulumi state delete`

- 将资源从当前堆栈移动到另一个堆栈：

`pulumi state move {{resource_urn}} --dest {{stack_name}}`

- 重命名当前堆栈状态中的资源：

`pulumi state rename`

- 修复无效的状态：

`pulumi state repair`

- 使用 `EDITOR` 环境变量指定的编辑器编辑堆栈状态：

`pulumi state edit --stack {{stack_name}}`

- 显示帮助：

`pulumi state --help`