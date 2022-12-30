# abbr

> 管理 fish shell 的缩写。
> 用户定义的词在输入后会被较长的短语替换。
> 更多信息：<https://fishshell.com/docs/current/cmds/abbr.html>.

- 添加一个新缩写：

`abbr --add {{缩写名}} {{命令}} {{命令参数}}`

- 重命名一个已有的缩写：

`abbr --rename {{旧缩写名}} {{新缩写名}}`

- 清除一个已有的缩写：

`abbr --erase {{缩写名}}`

- 用 SSH 导入另一台主机上定义的缩写：

`ssh {{主机名}} abbr --show | source`
