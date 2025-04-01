# cotton

> Markdown 测试规范运行器。
> 更多信息：<https://github.com/chonla/cotton>。

- 使用特定的基础 URL：

`cotton -u {{base_url}} {{path/to/file.md}}`

- 禁用证书验证（不安全模式）：

`cotton -u {{base_url}} -i {{path/to/file.md}}`

- 当测试失败时停止运行：

`cotton -u {{base_url}} -s {{path/to/file.md}}`
