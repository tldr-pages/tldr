# assoc

> 显示或更改文件扩展名与文件类型之间的关联。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/assoc>。

- 列出所有文件扩展名与文件类型之间的关联：

`assoc`

- 显示特定扩展名的关联文件类型：

`assoc {{.txt}}`

- 设置特定扩展名的关联文件类型：

`assoc .{{txt}}={{txtfile}}`

- 逐屏查看 `assoc` 的输出：

`assoc | {{more}}`