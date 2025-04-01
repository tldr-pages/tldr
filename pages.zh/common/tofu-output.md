# tofu output

> 导出关于你的 OpenTofu 资源的结构化数据。
> 更多信息：<https://opentofu.org/docs/cli/commands/output/>.

- 如果没有额外的参数，`output` 将显示根模块的所有输出：

`tofu output`

- 仅输出具有特定名称的值：

`tofu output {{name}}`

- 将输出值转换为原始字符串（对于 shell 脚本非常有用）：

`tofu output -raw`

- 将输出格式化为 JSON 对象，每个输出一个键（与 `jq` 一起使用非常有用）：

`tofu output -json`
