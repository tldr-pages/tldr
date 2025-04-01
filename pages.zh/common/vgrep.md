# vgrep

> 用于 grep 的用户友好分页器。
> 参见: `ugrep`, `rg`。
> 更多信息：<https://github.com/vrothberg/vgrep>。

- 递归搜索当前目录中的模式并缓存结果：

`vgrep {{search_pattern}}`

- 显示缓存的内容：

`vgrep`

- 在默认编辑器中打开缓存中的第“4”个匹配项：

`vgrep --show {{4}}`

- 为缓存中的每个匹配项显示“3”行上下文：

`vgrep --show=context{{3}}`

- 显示树中每个目录的匹配项数量：

`vgrep --show=tree`

- 显示树中每个文件的匹配项数量：

`vgrep --show=files`

- 以缓存的匹配项启动交互式 shell：

`vgrep --interactive`
