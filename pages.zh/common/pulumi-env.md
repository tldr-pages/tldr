# pulumi env

> 管理 Pulumi 环境。
> 更多信息：<https://www.pulumi.com/docs/iac/cli/commands/pulumi_env/>.

- 列出所有环境：

`pulumi env ls`

- 创建一个环境：

`pulumi env init {{environment_name}}`

- 在环境中设置一个值：

`pulumi env set {{environment_name}} {{key}} {{value}}`

- 编辑环境定义：

`pulumi env edit {{environment_name}}`

- 从环境中删除一个值：

`pulumi env rm {{environment_name}} {{key}}`

- 完全删除一个环境：

`pulumi env rm {{environment_name}}`

- 显示帮助：

`pulumi env --help`