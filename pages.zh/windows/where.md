# where

> 显示与搜索模式匹配的文件的位置。
> 在默认情况下，搜索是在当前目录和 PATH 环境变量指定的路径中执行的。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/where>.

- 显示匹配的文件的位置：

`where {{文件模式}}`

- 显示匹配的文件的位置、大小和日期：

`where /T {{文件模式}}`

- 在指定的路径下递归搜索要匹配的文件：

`where /R {{目录的路径}} {{文件模式}}`

- 只返回退出代码，不显示匹配文件列表：

`where /Q {{文件模式}}`
