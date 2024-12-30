# terraform 输出

> 导出有关您的 Terraform 资源的结构化数据。
> 更多信息：<https://developer.hashicorp.com/terraform/cli/commands/output>。

- 如果没有其他参数，`output` 将显示根模块的所有输出：

`terraform output`

- 仅输出特定名称的值：

`terraform output {{name}}`

- 将输出值转换为原始字符串（对 shell 脚本很有用）：

`terraform output -raw`

- 将输出格式化为 JSON 对象，每个输出对应一个键（与 jq 配合使用时很有用）：

`terraform output -json`