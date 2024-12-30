# fc

> 比较两个文件或文件集之间的差异。
> 使用通配符 (*) 来比较文件集。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/fc>。

- 比较两个指定的文件：

`fc {{path\to\file1}} {{path\to\file2}}`

- 执行不区分大小写的比较：

`fc /c {{path\to\file1}} {{path\to\file2}}`

- 将文件作为 Unicode 文本进行比较：

`fc /u {{path\to\file1}} {{path\to\file2}}`

- 将文件作为 ASCII 文本进行比较：

`fc /l {{path\to\file1}} {{path\to\file2}}`

- 将文件作为二进制进行比较：

`fc /b {{path\to\file1}} {{path\to\file2}}`

- 禁用制表符到空格的扩展：

`fc /t {{path\to\file1}} {{path\to\file2}}`

- 压缩比较中的空白字符（制表符和空格）：

`fc /w {{path\to\file1}} {{path\to\file2}}`