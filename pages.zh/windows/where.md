# where

> 显示匹配搜索模式的文件位置。
> 默认情况下为当前工作目录和 PATH 环境变量中的路径。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/where>。

- 显示文件模式的位置：

`where {{file_pattern}}`

- 显示包括文件大小和日期的文件模式位置：

`where /T {{file_pattern}}`

- 在指定路径下递归搜索文件模式：

`where /R {{path\to\directory}} {{file_pattern}}`

- 安静地返回文件模式位置的错误代码：

`where /Q {{file_pattern}}`