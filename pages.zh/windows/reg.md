# reg

> 管理 Windows 注册表中的键及其值。
> 一些子命令，如 `add`，有自己的使用文档。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/reg>。

- 执行注册表命令：

`reg {{command}}`

- 查看添加和复制子键的文档：

`tldr reg {{add|copy}}`

- 查看删除键和子键的文档：

`tldr reg {{delete|unload}}`

- 查看搜索、查看和比较键的文档：

`tldr reg {{compare|query}}`

- 查看导出和导入注册表键的文档，不保留键的所有权和 ACL：

`tldr reg {{export|import}}`

- 查看保存、恢复注册表和卸载键的文档，保留键的所有权和 ACL：

`tldr reg {{save|restore|load|unload}}`

- 显示帮助：

`reg /?`

- 显示特定命令的帮助：

`reg {{command}} /?`