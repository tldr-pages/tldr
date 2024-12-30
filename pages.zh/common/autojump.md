# autojump

> 快速跳转到您访问最多的目录。
> 提供像 j 或 jc 这样的别名，以减少输入。
> 更多信息：<https://github.com/wting/autojump>。

- 跳转到包含给定模式的目录：

`j {{pattern}}`

- 跳转到当前目录中包含给定模式的子目录（子文件夹）：

`jc {{pattern}}`

- 在操作系统文件管理器中打开包含给定模式的目录：

`jo {{pattern}}`

- 从 autojump 数据库中删除不存在的目录：

`j --purge`

- 显示 autojump 数据库中的条目：

`j -s`