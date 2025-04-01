# herd list

> 列出 Herd PHP 平台中可用的命令。
> 参见：`herd`。
> 更多信息：<https://herd.laravel.com>。

- 列出所有可用的命令：

`herd list`

- 列出特定命名空间中的所有可用命令：

`herd list {{namespace}}`

- 以原始格式列出所有命令（适用于嵌入命令运行器）：

`herd list --raw`

- 以指定的输出格式显示列表：

`herd list --format={{txt|xml|json|md}}`

- 列出所有命令但不显示其参数说明：

`herd list --short`