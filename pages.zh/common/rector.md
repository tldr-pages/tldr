# rector

> 用于更新和重构 PHP 5.3+ 代码的自动化工具。
> 更多信息：<https://github.com/rectorphp/rector>。

- 处理特定目录：

`rector process {{path/to/directory}}`

- 处理目录但不应用更改（干运行）：

`rector process {{path/to/directory}} --dry-run`

- 处理目录并应用编码标准：

`rector process {{path/to/directory}} --with-style`

- 显示可用级别的列表：

`rector levels`

- 使用特定级别处理目录：

`rector process {{path/to/directory}} --level {{level_name}}`