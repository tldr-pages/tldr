# terraform output

> 导出有关 Terraform 资源的结构化数据。
> 更多信息：<https://developer.hashicorp.com/terraform/cli/commands/output>.

- 如果没有附加参数，`output` 将显示根模块的所有输出：

`terraform output`

- 仅输出特定名称的值：

`terraform output {{name}}`

- 将输出值转换为纯字符串（适用于 shell 脚本）：

`terraform output -raw`

- 将输出格式化为 JSON 对象，每个输出一个键（适用于 jq）：

`terraform output -json`
