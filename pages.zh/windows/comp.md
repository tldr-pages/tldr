# comp

> 比较两个文件或文件集的内容。
> 使用通配符 (*) 比较文件集。
> 更多信息: <https://learn.microsoft.com/windows-server/administration/windows-commands/comp>。

- 交互式比较文件：

`comp`

- 比较两个指定的文件：

`comp {{path\to\file1}} {{path\to\file2}}`

- 比较两个文件集：

`comp {{path\to\directory1}}\* {{path\to\directory2}}\*`

- 以 [d]ecimal 格式显示差异：

`comp /d {{path\to\file1}} {{path\to\file2}}`

- 以 [a]SCII 格式显示差异：

`comp /a {{path\to\file1}} {{path\to\file2}}`

- 显示差异的 [l]ine 号：

`comp /l {{path\to\file1}} {{path\to\file2}}`

- 不区分大小写地比较文件：

`comp /c {{path\to\file1}} {{path\to\file2}}`

- 仅比较每个文件的前 5 行：

`comp /n=5 {{path\to\file1}} {{path\to\file2}}`