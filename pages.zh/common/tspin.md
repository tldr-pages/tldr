# tspin

> 一个基于 `less` 分页器的日志文件高亮工具，基本上表现得像任何分页器。
> 更多信息：<https://github.com/bensadeh/tailspin>。

- 从文件读取并在 `less` 中查看：

`tspin {{path/to/application.log}}`

- 从另一个命令读取并打印到标准输出：

`journalctl -b --follow | tspin`

- 从文件读取并打印到标准输出：

`tspin {{path/to/application.log}} --print`

- 从标准输入读取并打印到标准输出：

`echo "2021-01-01 12:00:00 [INFO] This is a log message" | tspin`