# abbr

> 管理鱼壳中的缩写。
> 用户定义的单词在输入后会被替换为更长的短语。
> 更多信息：<https://fishshell.com/docs/current/cmds/abbr.html>。

- 添加一个新的缩写：

`abbr --add {{缩写名称}} {{命令}} {{命令参数}}`

- 重命名一个现有的缩写：

`abbr --rename {{旧名称}} {{新名称}}`

- 删除一个现有的缩写：

`abbr --erase {{缩写名称}}`

- 通过SSH导入在另一台主机上定义的缩写：

`ssh {{主机名称}} abbr --show | source`