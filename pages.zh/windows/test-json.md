# Test-Json

> 测试字符串是否为有效的 JSON 文档。
> 注意：此命令只能通过 PowerShell 使用。
> 更多信息：<https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/test-json>.

- 测试从 `stdin` 读取的字符串是否为 JSON 格式：

`'{{string}}' | Test-Json`

- 测试字符串是否为 JSON 格式：

`Test-Json -Json '{{json_to_test}}'`

- 测试从 `stdin` 读取的字符串是否符合特定的模式文件：

`'{{string}}' | Test-Json -SchemaFile {{path\to\schema_file.json}}`
